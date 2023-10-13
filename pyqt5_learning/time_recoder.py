import tkinter as tk
import time

root = tk.Tk()
root.title("Time Recorder")
root.geometry("400x400")
font_time = ("Arial", 30, "bold")
label = tk.Label(root, text="00:00:00",height=5, bd=15,pady=0,font=font_time)

label.pack(side=tk.TOP, fill=tk.X)

start_time = None

def start_timer():
    global start_time
    start_time = time.time()  # 记录开始时间
    update_timer()  # 开始更新 Label

def stop_timer():
    label.configure(text="00:00:00",bg="white", fg="red")  # 停止时显示 00:00:00
    global start_time
    start_time=None


def update_timer():
    if start_time:
        seconds = int(time.time() - start_time)  # 计算经过的秒数
        hh = seconds // 3600  # 计算小时数
        mm = (seconds % 3600) // 60  # 计算分钟数
        ss = seconds % 60  # 计算秒数
        # 格式化输出
        label.configure(text="{:02d}:{:02d}:{:02d}".format(hh, mm, ss),bg="green", fg="yellow")
        # 每隔一秒钟更新一次 Label
        label.after(1000, update_timer)

# 创建计时器控件

font = ("Courier", 10, "bold")
relief_list =['flat','groove','raised','ridge','solid','sunken']
start_btn = tk.Button(root, text="Start",height=3,width=10, command=start_timer, font=font,relief=relief_list[4],activebackground="green",disabledforeground="grey")
stop_btn = tk.Button(root, text="Stop", height=3, command=stop_timer)
start_btn.pack(side=tk.TOP, fill=tk.X)
stop_btn.pack(side=tk.BOTTOM, fill=tk.X)

root.mainloop()