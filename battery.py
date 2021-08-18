#pip install psutil
import psutil

battery=psutil.sensors_battery()
plugged=battery.power_plugged
percent=battery.percent
  
if percent>=30:
    #pip install py-notifier
    #pip install win10toast
    from pynotifier import Notification
    #duration in seconds
    Notification(title="Battery Low",description=str(percent)+"%Battery remain!!",duration=5).send()
