import tkinter as tk
import time
import tkinter.messagebox as msg

class Todo(tk.Tk):
    def __init__(self, tasks=None):
        super().__init__()
        if not tasks:
            self.tasks = []
        else:
            self.tasks = tasks

        self.tasks_canvas = tk.Canvas(self) #画布控件；显示图形元素如线条或文本
        self.tasks_frame = tk.Frame(self.tasks_canvas)#框架控件；在屏幕上显示一个矩形区域，多用来作为容器
        self.text_frame = tk.Frame(self)
        self.scrollbar = tk.Scrollbar(self.tasks_canvas, orient="vertical", command=self.tasks_canvas.yview())
        #Scrollbar 滚动条控件，当内容超过可视化区域时使用，如列表框
        #xview
        # .xview(tk.MOVETO, fraction) 此方法相对于其图像滚动画布，旨在绑定到相关滚动条的命令选项。 画布水平滚动到偏移指定的位置，其中 0.0 将画布移动到最左边的位置，1.0 移动到最右边的位置。
        # .xview(tk.SCROLL, n, what) 此方法向左或向右移动画布：what 参数指定移动多少，可以是 tk.UNITS 或 tk.PAGES，n 表示相对于其图像向右移动画布多少个单位（或向左， 如果为负）
        self.tasks_canvas.configure(yscrollcommand=self.scrollbar.set)
        self.title("To-DO List v2")
        self.geometry("300x500")

        self.task_create = tk.Text(self.text_frame, height=3, bg="white", fg="black")

        self.tasks_canvas.pack(side=tk.TOP, fill = tk.BOTH, expand = 1)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.canvas_frame = self.tasks_canvas.create_window((0,0), window=self.tasks_frame, anchor="n")
        self.task_create.pack(side=tk.BOTTOM, fill=tk.X)
        self.text_frame.pack(side=tk.BOTTOM, fill=tk.X)
        self.task_create.focus_set()

        todo1 = tk.Label(self.tasks_frame, text="---  Add Items Here ---", bg="lightgrey", fg="black", pady=10)
        todo1.bind("<Button-1>", self.remove_task)
        self.tasks.append(todo1)


        for tasks in self.tasks:
            tasks.pack(side=tk.BOTTOM, fill=tk.X)

        self.bind("<Return>", self.add_task)

    def add_task(self, event=None):
        task_text=self.task_create.get(1.0,tk.END).strip()
        if len(task_text) > 0:
            new_task = tk.Label(self.tasks_frame, text=task_text, pady=10)
            self.set_task_colour(len(self.tasks), new_task)
            new_task.bind("<Button-1>", self.remove_task)
            new_task.pack(side=tk.TOP, fill=tk.X)
            self.tasks.append(new_task)
        self.task_create.delete(1.0, tk.END)


    def remove_task(self, event=None):
        task = event.widget
        if msg.askyesno("Really Delete?", "Delete "+ task.cget("text") + "?"):
            self.tasks.remove(event.widget)
            event.widget.destroy()
            #self.recolour_tasks()

    def recolour_tasks(self):
        for index, task in enumerate(self.tasks):
            self.set_task_colour(index, task)

    def set_task_colour(self, position, task):
        _, task_style_choice=divmod(position,2)
        my_scheme_choice=self.colour_schemes[task_style_choice]

        task.configure(bg=my_scheme_choice["bg"])
        task.configure(fg=my_scheme_choice["fg"])

    def on_frame_configure(self,event=None):
        self.tasks_canvas.configure(scrollregion=self.tasks_canvas.bbox("all"))


    def task_width(self,event):
        canvas_width = event.widget
        self.tasks_canvas.itemconfig(self.canvas_frame, width=canvas_width)


    def mouse_scroll(self,event):
        if event.delta:
            self.tasks_canvas.yview_scroll(int(-1*(event.delta/120)),"units")
        else:
            if event.num==5:
                move =1
            else:
                move=-1
            self.tasks_canvas.yview_scroll(move,"units")

if __name__ == '__main__':
    todo = Todo()
    todo.mainloop()