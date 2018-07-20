BDSup2Sub = '/home/retrontology/git/BDSup2Sub/target/BDSup2Sub512.jar'
ISO = {'lao': 'lo', 'fas': 'fa', 'ces': 'cs', 'yid': 'yi', 'ibo': 'ig', 'epo': 'eo', 'ido': 'io', 'cat': 'ca', 'run': 'rn', 'xho': 'xh', 'vie': 'vi', 'sun': 'su', 'iku': 'iu', 'slv': 'sl', 'roh': 'rm', 'bam': 'bm', 'chv': 'cv', 'kaz': 'kk', 'ave': 'ae', 'eus': 'eu', 'cos': 'co', 'ven': 've', 'tah': 'ty', 'uig': 'ug', 'swa': 'sw', 'lin': 'ln', 'her': 'hz', 'jav': 'jv', 'nau': 'na', 'bul': 'bg', 'hun': 'hu', 'bod': 'bo', 'ukr': 'uk', 'kor': 'ko', 'ndo': 'ng', 'kal': 'kl', 'pli': 'pi', 'glv': 'gv', 'kom': 'kv', 'mar': 'mr', 'khm': 'km', 'hau': 'ha', 'nbl': 'nr', 'bos': 'bs', 'ful': 'ff', 'ssw': 'ss', 'jpn': 'ja', 'fra': 'fr', 'ara': 'ar', 'kat': 'ka', 'isl': 'is', 'tso': 'ts', 'kin': 'rw', 'msa': 'ms', 'tgl': 'tl', 'som': 'so', 'smo': 'sm', 'mya': 'my', 'glg': 'gl', 'zul': 'zu', 'por': 'pt', 'deu': 'de', 'mkd': 'mk', 'kua': 'kj', 'lat': 'la', 'twi': 'tw', 'srp': 'sr', 'sqi': 'sq', 'que': 'qu', 'wol': 'wo', 'fij': 'fj', 'kon': 'kg', 'abk': 'ab', 'tsn': 'tn', 'lug': 'lg', 'kir': 'ky', 'sin': 'si', 'est': 'et', 'cor': 'kw', 'kur': 'ku', 'sme': 'se', 'spa': 'es', 'nav': 'nv', 'nde': 'nd', 'ltz': 'lb', 'fao': 'fo', 'ell': 'el', 'mah': 'mh', 'ava': 'av', 'fry': 'fy', 'arg': 'an', 'san': 'sa', 'bre': 'br', 'orm': 'om', 'nor': 'no', 'mri': 'mi', 'sag': 'sg', 'gle': 'ga', 'amh': 'am', 'ewe': 'ee', 'ori': 'or', 'uzb': 'uz', 'ind': 'id', 'nld': 'nl', 'cha': 'ch', 'wln': 'wa', 'nya': 'ny', 'fin': 'fi', 'aym': 'ay', 'hbs': 'sh', 'bis': 'bi', 'heb': 'he', 'bel': 'be', 'hmo': 'ho', 'dzo': 'dz', 'afr': 'af', 'kik': 'ki', 'bak': 'ba', 'yor': 'yo', 'cre': 'cr', 'lav': 'lv', 'hin': 'hi', 'lit': 'lt', 'hye': 'hy', 'guj': 'gu', 'ipk': 'ik', 'snd': 'sd', 'mlg': 'mg', 'aze': 'az', 'tir': 'ti', 'asm': 'as', 'tel': 'te', 'mlt': 'mt', 'oci': 'oc', 'ita': 'it', 'pan': 'pa', 'sna': 'sn', 'hat': 'ht', 'tam': 'ta', 'che': 'ce', 'kas': 'ks', 'zho': 'zh', 'lub': 'lu', 'ton': 'to', 'sot': 'st', 'rus': 'ru', 'kau': 'kr', 'ron': 'ro', 'nno': 'nn', 'nob': 'nb', 'tgk': 'tg', 'tha': 'th', 'zha': 'za', 'iii': 'ii', 'pol': 'pl', 'swe': 'sv', 'mal': 'ml', 'grn': 'gn', 'ile': 'ie', 'tur': 'tr', 'ina': 'ia', 'lim': 'li', 'kan': 'kn', 'dan': 'da', 'eng': 'en', 'aka': 'ak', 'gla': 'gd', 'slk': 'sk', 'hrv': 'hr', 'oss': 'os', 'urd': 'ur', 'vol': 'vo', 'tat': 'tt', 'mon': 'mn', 'tuk': 'tk', 'chu': 'cu', 'pus': 'ps', 'nep': 'ne', 'aar': 'aa', 'ben': 'bn', 'srd': 'sc', 'cym': 'cy', 'oji': 'oj', 'div': 'dv', 'alb': 'sq', 'arm': 'hy', 'baq': 'eu', 'bur': 'my', 'chi': 'zh', 'cze': 'cs', 'dut': 'nl', 'fre': 'fr', 'geo': 'ka', 'ger': 'de', 'gre': 'el', 'ice': 'is', 'mac': 'mk', 'may': 'ms', 'mao': 'mi', 'per': 'fa', 'rum': 'ro', 'slo': 'sk', 'tib': 'bo', 'wel': 'cy'}

def main():
    init()
    if(os.path.isfile(targ)):
        recodeSubs(targ)
    elif(os.path.isdir(targ)):
        scanner(targ)
        multiEncodeSubs(1)

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

def recodeSubs(target):
    fulltarget = os.path.abspath(target)
    target = os.path.basename(fulltarget)
    cwdir = os.path.dirname(fulltarget)
    probe = ffmpeg.probe(fulltarget)
    submap = []
    threads = []
    for i in probe['streams']:
        if (i['codec_name'] == 'hdmv_pgs_subtitle'):
            submap.append(i)
    for i in submap:
        try:
            t = threading.Thread(target=convSubStream, args=(fulltarget, i, ))
            threads.append(t)
            t.start()
        except Exception as e:
            print('Error: unable to start thread - ' + str(e))
    while(any(t.is_alive() for t in threads)):
        time.sleep(1)
        #convSubStream(fulltarget, i)
    if(len(submap)>0):
        comFfmpeg = 'ffmpeg -i \"' + target + '\" '
        for i in submap:
            name = target[:-3] + i['tags']['language'] + '.' + str(i['index'])
            comFfmpeg += '-i \"' + name + '.srt\" '
        comFfmpeg = comFfmpeg + '-map 0 '
        for i in submap:
            comFfmpeg = comFfmpeg + '-map -0:' + str(i['index']) + ' '
        for i in range(1, len(submap) + 1):
            comFfmpeg = comFfmpeg + '-map ' + str(i) + ' '
        comFfmpeg = comFfmpeg + '-c copy -f matroska \"' + target + '.temp\"'
        p = subprocess.run(comFfmpeg, cwd=cwdir, shell=True)
        print(p)
        if(p.returncode == 0):
            shutil.move(fulltarget + '.temp', fulltarget)
            for i in submap:
                name = target[:-3] + i['tags']['language'] + '.' + str(i['index'])
                if os.path.isfile(os.path.join(cwdir, name + '.srt')):
                    os.remove(os.path.join(cwdir, name + '.srt'))

def convSubStream(target, stream):
    fulltarget = os.path.abspath(target)
    target = os.path.basename(fulltarget)
    cwdir = os.path.dirname(fulltarget)
    lang3 = stream['tags']['language']
    lang2 = ISO[lang3]
    name = target[:-3] + lang3 + '.' + str(stream['index'])
    comExtract = 'mkvextract tracks \"' + target + '\" \"' + str(stream['index']) + ':' + name + '.sup\"'
    comSup2Sub = 'java -jar \"' + BDSup2Sub + '\" -l ' + lang2 + ' -o \"' + name + '.sub\" \"' + name + '.sup\"'
    comSub2Srt = 'vobsub2srt -l ' + lang2 + ' \"' + name + '\"'
    #com = comExtract + ' && ' + comSup2Sub + ' && ' + comSub2Srt
    p = subprocess.run(comExtract, cwd=cwdir, shell=True)
    print(p)
    p = subprocess.run(comSup2Sub, cwd=cwdir, shell=True)
    print(p)
    p = subprocess.run(comSub2Srt, cwd=cwdir, shell=True)
    print(p)
    if os.path.isfile(os.path.join(cwdir, name + '.sup')):
        os.remove(os.path.join(cwdir, name + '.sup'))
    if os.path.isfile(os.path.join(cwdir, name + '.sub')):
        os.remove(os.path.join(cwdir, name + '.sub'))
    if os.path.isfile(os.path.join(cwdir, name + '.idx')):
        os.remove(os.path.join(cwdir, name + '.idx'))

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

def multiEncodeSubs(hwcount):
    threads = []
    for g in range(0, hwcount):
        if(len(video_files) > 0):
            try:
                t = threading.Thread(target=encodeSubsFromList)
                threads.append(t)
                t.start()
                time.sleep(1)
            except Exception as e:
                print('Error: unable to start thread - ' + str(e))
        else:
            break
    while(any(t.is_alive() for t in threads)):
        time.sleep(1)

def encodeSubsFromList():
    while(len(video_files) > 0):
        file = video_files[0]
        del video_files[0]
        try:
            recodeSubs(file)
        except Exception as e:
            print('Error: Could not encode from list - ' + str(e))

if __name__ == '__main__':
    main()
