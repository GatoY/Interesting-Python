##1 目的

设置程序从设定时间开始播放音乐，以使自己起床（当然你设置的歌不对也可能起反作用）

##2 硬件

我的是Mac，在系统偏好设置的节能器中可以设置睡眠定时唤醒，在你设置的时间唤醒电脑即可，因为在睡眠状态下任何软件都是无法运行的。

##3 APScheduler定时框架

APScheduler库是python的定时任务框架，使用方便，功能完整，能实现基于日期，固定间隔，crontab类型的任务执行，以daemon方式运行运用；也能在程序运行中进行任务的添加与删除

####下载

```
$ pip install apscheduler  //权限问题就在前面加 sudo
```

####APScheduler四个组件
APScheduler 四个组件分别为：触发器(trigger)，作业存储(job store)，执行器(executor)，调度器(scheduler)。

####定时模块编写
```
from apscheduler.schedulers.blocking import BlockingScheduler
scheduler = BlockingScheduler()
scheduler.add_job(display, 'cron', hour = 9)
scheduler.start()
```

display为播放函数，hour=9表示早上9点钟运行display函数。

##4 编写播放函数
####使用os库获取特定文件夹下音乐文件

```
import os
f=os.popen('ls')
list=f.readlines()
```
list保存为当前文件夹下所有文件名的数组
####利用Moviepy库获取视频文件的播放信息
我们选定默认打开方式为暴风影音（因为QuickTime Player打开后不会自动播放），由于用Python控制播放列表，于是需要获取视频的时长信息，此处使用Moviepy。

```
from moviepy.editor import VideoFileClip
video=VideoFileClip('filename')
durationTime=int(video.duration)
```
获取了时长以后，在打开一个音乐视频文件以后，time.sleep(durationTime)，使播放完上一首音乐后直接播放下一首。

##5所有代码

```
# coding: utf-8
from apscheduler.schedulers.blocking import BlockingScheduler
from moviepy.editor import VideoFileClip
import os
import time
def display():
    f=os.popen('ls')
    list=f.readlines()
    while(1):
        for i in list:
            if i[:-1][-4:] == '.mp4':
                #print i[:-1][-4:]
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
#   time.sleep(5)
scheduler = BlockingScheduler()
scheduler.add_job(display, 'cron', hour = 9)
scheduler.start()


```
