# Retrontology's ffmpeg scripts

### Description
A small collection of python 3scripts I used to use for my personal video collection. I do not recommend using them as they are poorly written and will not be updated by myself any time soon.

### Requirements
- Python 3
- ffmpeg (with Nvidia card and HW acceleration enabled)
- BDSup2Sub

---

## `4kred.py`

### Description
A script used to reduce the bitrate of a video file if it's over a specified limit

### Setup
Ensure `maxrate` is set to the bitrate threshold of your choosing

### Usage
```
python3 4kred.py <target-video-file>
```

---

## `audio.py`

### Description
A script to recode the audio in a video file to `ac3`

### Usage
```
python3 audio.py <target-video-file>
```

---

## `subs.py`

### Description
A script that recodes PGS subs to SRT using BDSup2Sub

### Setup
Change the `BDSup2Sub` variable to point to the location ofhte BDSup2Sub.jar file

### Usage
```
python3 subs.py <target-video-file>
```