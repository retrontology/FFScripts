def main():
    init()
    if(os.path.isfile(targ)):
        recodeSubs(targ)
    elif(os.path.isdir(targ)):
        scanner(targ)
        multiEncodeAudio(4)

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

def recodeAudio(target):
    fulltarget = os.path.abspath(target)
    target = os.path.basename(fulltarget)
    cwdir = os.path.dirname(fulltarget)
    probe = ffmpeg.probe(fulltarget)
    conv = False
    for i in probe['streams']:
        if (i['codec_type'] == 'audio' and i['codec_name'] != 'ac3'):
            conv = True
            break;
    if conv:
        format = probe['format']['format_long_name']
        if format == 'QuickTime / MOV':
            format = 'mp4'
        elif format == 'Matroska / WebM':
            format = 'matroska'
        cmd = 'ffmpeg -y -i \"' + target + '\" -map 0 -c copy -c:a ac3 -f ' + format + ' \"' + target + '.temp\"'
        p = subprocess.run(cmd, cwd=cwdir, shell=True)
        if p.returncode == 0:
            shutil.move(fulltarget + '.temp', fulltarget)

def multiEncodeAudio(hwcount):
    threads = []
    for g in range(0, hwcount):
        if(len(video_files) > 0):
            try:
                t = threading.Thread(target=encodeAudioFromList)
                threads.append(t)
                t.start()
                time.sleep(1)
            except Exception as e:
                print('Error: unable to start thread - ' + str(e))
        else:
            break
    while(any(t.is_alive() for t in threads)):
        time.sleep(1)

def encodeAudioFromList():
    while(len(video_files) > 0):
        file = video_files[0]
        del video_files[0]
        try:
            recodeAudio(file)
        except Exception as e:
            print('Error: Could not encode from list - ' + str(e))

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

if __name__ == '__main__':
    main()