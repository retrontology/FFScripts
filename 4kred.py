maxrate = '16000k'

def main():
    init()
    if(os.path.isfile(targ)):
        encode(targ, 0)
    elif(os.path.isdir(targ)):
        scanner(targ)
        multiEncode(2)
        #print(video_files)

def install_and_import(package):
    import importlib
    try:
        importlib.import_module(package)
    except ImportError:
        import pip
        if(package == 'ffmpeg'):
            package = 'ffmpeg-python'
        pip.main(['install', package])
    finally:
        globals()[package] = importlib.import_module(package)

def init():
    install_and_import('sys')
    install_and_import('os')
    if(len(sys.argv) > 2):
        sys.exit('This script only takes one file at a time')
    elif(len(sys.argv) == 1):
        sys.exit('Please pass a file to this script')
    else:
        global targ
        targ = os.path.abspath(sys.argv[1])
    if(os.path.isfile(targ) != True and os.path.isdir(targ) != True):
        print(targ)
        sys.exit('The provided file/directory does not exist')
    else:
        global video_files
        video_files = []
        install_and_import('ffmpeg')
        install_and_import('subprocess')
        install_and_import('threading')
        install_and_import('time')
        install_and_import('shutil')

def encode(target, hwdev):
    print('Target: ' + target)
    probe = ffmpeg.probe(target)
    codec = probe['streams'][0]['codec_name']
    hwdec = True
    hwdev = str(hwdev)
    cwdir = os.path.dirname(target)
    command = 'ffmpeg -y -hwaccel_device ' + hwdev + ' -hwaccel cuvid'
    if(codec == 'h264'):
        command += ' -c:v h264_cuvid'
    elif(codec == 'hevc'):
        command += ' -c:v hevc_cuvid'
    else:
        hwdec = False
    command += ' -i \"' + target + '\" -map 0 -c copy -c:v:0 hevc_nvenc -b:v ' + maxrate + ' -maxrate ' + maxrate + ' -c:a ac3 -f matroska -passlogfile \"' + target[:-3] + '\"'
    for i in range(1, len(probe['streams'])):
        if(probe['streams'][i]['codec_name'] == 'hevc' or probe['streams'][i]['codec_name'] == 'h264'):
            command += ' -map -0:' + str(i)
    pass_1 = command + ' -pass 1 NUL'
    pass_2 = command + ' -pass 2 \"' + target[:-3] + '\"16M.mkv'
    # Run it
    p1 = subprocess.run(pass_1 + ' && ' + pass_2, cwd=cwdir, shell=True)
    print(p1.returncode)
    if(p1.returncode == 1 and hwdec == True):
        hwdec = False
        pass_1 = 'ffmpeg -y -hwaccel_device ' + hwdev + ' -hwaccel cuvid -i \"' + target + '\" -map 0 -c copy -c:v:0 hevc_nvenc -b:v ' + maxrate + ' -maxrate ' + maxrate + ' -c:a ac3 -f matroska -passlogfile \"' + target[:-3] + '\" -pass 1 NUL'
        pass_2 = 'ffmpeg -y -hwaccel_device ' + hwdev + ' -hwaccel cuvid -i \"' + target + '\" -map 0 -c copy -c:v:0 hevc_nvenc -b:v ' + maxrate + ' -maxrate ' + maxrate + ' -c:a ac3 -f matroska -passlogfile \"' + target[:-3] + '\" -pass 2 \"' + target[:-3] + '\"16M.mkv'
        p1 = subprocess.run(pass_1 + ' && ' + pass_2, cwd=cwdir, shell=True)
    if(p1.returncode == 0):
        os.remove(target)

def scanner(dir):
    dir = os.path.abspath(dir)
    files = os.scandir(dir)
    for file in files:
        if(file.is_dir()):
            scanner(file.path)
        elif(file.is_file()):
            name, ext = os.path.splitext(file.name)
            if ext in ['.mp4', '.mkv', '.avi', '.flv']:
                video_files.append(file.path)

def multiEncode(hwcount):
    threads = []
    for g in range(0, hwcount):
        if(len(video_files) > 0):
            try:
                t = threading.Thread(target=encodeFromList, args=(g, ))
                threads.append(t)
                t.start()
                time.sleep(1)
            except Exception as e:
                print('Error: unable to start thread - ' + str(e))
        else:
            break
    while(any(t.is_alive() for t in threads)):
        time.sleep(1)

def encodeFromList(hwdev):
    while(len(video_files) > 0):
        file = video_files[0]
        del video_files[0]
        try:
            encode(file, hwdev)
        except Exception as e:
            print('Error: Could not encode from list - ' + str(e))

if __name__ == '__main__':
    main()
