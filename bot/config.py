#    Copyright (c) 2021 Danish_00
#    Improved By @Zylern

from decouple import config

try:
    API_ID = environ.get('API_ID',cast=int"16621664") 
    API_HASH = environ.get('API_HASH',"8b283f2943729318995738b5963f0bcc") 
    BOT_TOKEN = environ.get('BOT_TOKEN',"6614340340:AAFlzPQITbWoH9BYYKpWPfNb6xygI2IXWDI")
    DEV = 6561715152
    OWNER = config("OWNER","6561715152")
    ffmpegcode = ["-preset faster -c:v libx265 -s 854x480 -x265-params 'bframes=8:psy-rd=1:ref=3:aq-mode=3:aq-strength=0.8:deblock=1,1' -metadata 'title=Encoded By TGVid-Comp (https://github.com/Zylern/TGVid-Comp)' -pix_fmt yuv420p -crf 30 -c:a libopus -b:a 32k -c:s copy -map 0 -ac 2 -ab 32k -vbr 2 -level 3.1 -threads 1"]
    THUMBNAIL = config("THUMBNAIL", default="https://telegra.ph/file/f9e5d783542906418412d.jpg")
except Exception as e:
    print("Environment vars Missing! Exiting App.")
    print(str(e))
    exit(1)
