# m3u8Downloader

This will let you download a video thats made available through a m3u8 playlist file that will look somewhat like this:

#EXTM3U
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=763904,RESOLUTION=854x480,NAME="480p"
hls-480p.m3u8?2fhzC1POpPanuy9sVGqZ7B3s5y
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=1327104,RESOLUTION=1280x720,NAME="720p"
hls-720p.m3u8?2fhzC1POpPanuy9sVGqZ7B3s5ydPkeLoQCE1OQpln5FFGJ8
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=423936,RESOLUTION=640x360,NAME="360p"
hls-360p.m3u8?2fhzC1POpPanuy9sVGqZ7B3s5ydPkeLoQCE1OQpln5FFG
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=155648,RESOLUTION=444x250,NAME="250p"
hls-250p.m3u8?2fhzC1POpPanuy9sVGqZ7B3s5ydPkeLoQCE1OQpln5FFGJ

The script automatically picks the best video quality stream and starts downloading the different part files, finally merging them together into a single .ts file. The script uses my m3u8 parser for python (https://github.com/HWask/m3u8ParserPython).

Usage: 
- set the filename of the m3u8 file in m3u8Downloader.py
- run m3u8Downloader.py

