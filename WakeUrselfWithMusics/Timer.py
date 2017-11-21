# coding: utf-8
from apscheduler.schedulers.blocking import BlockingScheduler
from moviepy.editor import VideoFileClip
import os
import time
'''def display():
    f=os.popen('ls')
    for i in f.readlines():
        video=VideoFileClip(i[:-1])
        time=video.duration
        os.system('open '+i[:-1])
        time.sleep(time)
'''
def display():
    f=os.popen('ls')
    list=f.readlines()
    while(1):
        for i in list:
            if i[:-1][-4:] == '.mp4':
                try:
                    video=VideoFileClip(i[:-1])
                    durationTime=int(video.duration)
                    os.system('open '+i[:-1])
                    time.sleep(durationTime)
                    print 'Displaying '+i[:-1]
                except:
                    continue
            #if i[:-1][-4:] =='.mp3':
            #   os.system('open '+i[:-1]+' -F'+' -n')
scheduler = BlockingScheduler()
scheduler.add_job(display, 'cron', hour = 9)
scheduler.start()

