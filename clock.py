import datetime as d
import time
import easygui as g
while True:
    time = tuple()
    time = d.datetime.now()
    year,month,day,hour,minute,second = time.year,time.month,time.day,time.hour,time.minute,time.second
    output = f"Year:{year} Month:{month} day:{day} Time: {hour}：{minute}:{second}"
    g.textbox(msg="time",title="time",text=output)
