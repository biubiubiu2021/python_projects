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
        #A Canvas is a powerful general-use widget with many capabilities (usually graphical). We are using it here for its ability
        #to scroll, which we need if we want to add a lot of apps to our list.
        self.tasks_frame = tk.Frame(self.tasks_canvas)#框架控件；在屏幕上显示一个矩形区域，多用来作为容器, this frame is parented to the canvas
        #A Frame is a layout component which can be used to group together multiple other widgets.
        self.text_frame = tk.Frame(self) # this frame is parented to the main window
        self.scrollbar = tk.Scrollbar(self.tasks_canvas, orient="vertical", command=self.tasks_canvas.yview)
        self.scrollbar2 = tk.Scrollbar(self.tasks_canvas, orient="horizontal", command=self.tasks_canvas.xview)
        #set the orientation and command to tell tkinter that we want a vertical scrollbar, scrolling in the y direction.
        #Scrollbar 滚动条控件，当内容超过可视化区域时使用，如列表框
        #xview
        # .xview(tk.MOVETO, fraction) 此方法相对于其图像滚动画布，旨在绑定到相关滚动条的命令选项。 画布水平滚动到偏移指定的位置，其中 0.0 将画布移动到最左边的位置，1.0 移动到最右边的位置。
        # .xview(tk.SCROLL, n, what) 此方法向左或向右移动画布：what 参数指定移动多少，可以是 tk.UNITS 或 tk.PAGES，n 表示相对于其图像向右移动画布多少个单位（或向左， 如果为负）
        self.tasks_canvas.configure(yscrollcommand=self.scrollbar.set)
        self.tasks_canvas.configure(xscrollcommand=self.scrollbar2.set)
        #configure the canvas to accept the Scrollbar’s values.
        self.title("To-DO List v2")
        #set the title of the main window
        self.geometry("300x500")
        #set the size of the main window
        self.task_create = tk.Text(self.text_frame, height=3, bg="white", fg="black")
        #Create a Text widget and be parented to one of the frames (which will be packed to the bottom)

        self.tasks_canvas.pack(side=tk.TOP, fill = tk.BOTH, expand = 1)
        #The Canvas is packed with instruction to fill all available space and expand as big as it can
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.scrollbar2.pack(side=tk.BOTTOM,fill=tk.X)
        #The Scrollbar follows,filling up the vertical space

        self.canvas_frame = self.tasks_canvas.create_window((0,0), window=self.tasks_frame, anchor="nw")
        #We use our Canvas to create a new window inside itself, which is
        #our Frame holding the tasks. We create it at the coordinates (0,0) and anchor it to the top of the Canvas
        #(the "n" here is for "north", so top-left would require "nw", and so on). One thing to note is that we do
        #not pack our tasks_frame, as it will not appear, and we will be left scratching our heads as to where it is.
        #This is something I learned the hard way!
        self.task_create.pack(side=tk.BOTTOM, fill=tk.X)
        self.text_frame.pack(side=tk.BOTTOM, fill=tk.X)
        self.task_create.focus_set()

        todo1 = tk.Label(self.tasks_frame, text="---  Add Items Here ---", bg="lightgrey", fg="black", pady=10)
        todo1.bind("<Button-1>", self.remove_task)
        self.tasks.append(todo1)#create a default task

        self.colour_schemes=[{"bg":"lightgrey","fg":"black"},{"bg":"grey","fg":"white"}]

        for tasks in self.tasks:
            tasks.pack(side=tk.TOP, fill=tk.X)

        self.bind("<Return>", self.add_task)
        self.bind("<Configure>", self.on_frame_configure)
        self.bind("<MouseWheel>", self.mouse_scroll)
        self.bind("<Button-4>", self.mouse_scroll)
        self.bind("<Button-5>", self.mouse_scroll)
        self.tasks_canvas.bind("<Configure>",self.task_width)

    def add_task(self, event=None):
        task_text=self.task_create.get(1.0,tk.END).strip()
        if len(task_text) > 0:
            new_task = tk.Label(self.tasks_frame, text=task_text, pady=10)
            self.set_task_colour(len(self.tasks), new_task)
            new_task.bind("<Button-1>", self.remove_task)
            new_task.pack(side=tk.TOP, fill=tk.BOTH)
            self.tasks.append(new_task)
        self.task_create.delete(1.0, tk.END)


    def remove_task(self, event=None):
        task = event.widget
        if msg.askyesno("Really Delete?", "Delete "+ task.cget("text") + "?"):
            self.tasks.remove(event.widget)
            event.widget.destroy()
            self.recolour_tasks()
        #To avoid accidental removal, we use an askyesno pop-up message to double-check
        # with the user that they wanted to delete that task (make sure you don’t miss the new import tkinter.
        # messagebox as msg statement at the top of the file). This will create a small notice with the title "Really
        # Delete?" and the message "Delete <task>?" (where <task> will be the text within the Label) with the
        # options "yes" and "no". Using the if statement around this means the indented code will only happen if the
        # user presses "yes". Upon deletion, we recolour all remaining tasks in our alternating pattern, as otherwise
        # the pattern would be broken by the removal.

    def recolour_tasks(self):
        for index, task in enumerate(self.tasks):
            self.set_task_colour(index, task)
    #set_task_colour - so that it can be re-used after deleting tasks.

    def set_task_colour(self, position, task):
        _, task_style_choice=divmod(position,2)
        my_scheme_choice=self.colour_schemes[task_style_choice]

        task.configure(bg=my_scheme_choice["bg"])
        task.configure(fg=my_scheme_choice["fg"])

    def on_frame_configure(self,event=None):
        self.tasks_canvas.configure(scrollregion=self.tasks_canvas.bbox("all"))
    #Our on_frame_configure method is bound to our root’s <Configure> action, and will be called whenever
        # the window is resized. It sets the scrollable region for our canvas, and uses the bbox (bounding box) to
        # specify that we want the entire canvas to be scrollable.

    def task_width(self,event):
        canvas_width = event.widget
        self.tasks_canvas.itemconfig(self.canvas_frame, width=canvas_width)
        #The task_width method is bound to the Canvas’s
        # <Configure>, and is responsible for ensuring the task Labels stay at the full width of the canvas, even after
        # stretching the window.

    def mouse_scroll(self,event):
        if event.delta:
            self.tasks_canvas.yview_scroll(int(-1*(event.delta/120)),"units")
        else:
            if event.num==5:
                move =1
            else:
                move=-1
            self.tasks_canvas.yview_scroll(move,"units")
        #Our final method, mouse_scroll, is how we bind scrolling to the mouse wheel as well as the scrollbar. This
        # is bound to <MouseWheel> for Windows and OSX, and to <Button-4> and <Button-5> for Linux. We then
        # simply call the Canvas’ yview_scroll method based upon whether we receive a delta or a num within the
        # event. Here on Linux I get a num. The delta is usually 120 or -120, so is divided by 120 for more precise
        # scrolling, and multiplied by -1 to adjust the direction
        #

if __name__ == '__main__':
    todo = Todo()
    todo.mainloop()