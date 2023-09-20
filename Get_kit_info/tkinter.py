import tkinter as tk
import time

class Todo(tk.Tk):
    def __init__(self, tasks = None):#如果使用可变数据类型，如列表，最好将默认参数设为None, 并且在__init__中将它转为列表，防止传入空列表导致错误
        super().__init__()

        if not tasks:
            self.tasks = []
        else:
            self.tasks = tasks

        self.title("To-DO App v1")#设置页面的主题和尺寸
        self.geometry("300x500")

        todo1=tk.Label(self, text="--- Add Items Here ---", bg="green", fg="yellow", pady=3) #创建一个提示标签， Text
        self.tasks.append(todo1)
        print("----->",self.tasks)
        #todo1.pack(side=tk.BOTTOM)

        for task in self.tasks: #使用一个for循环来将所有的task 打包在页面底部，使用X 参数来让水平自动填充
            task.pack(side=tk.BOTTOM, fill=tk.X)

        self.task_create = tk.Text(self, height=3, bg="white", fg="black") #创建一个text 输入框，默认高度改成3
        self.task_create.pack(side=tk.BOTTOM, fill = tk.X)#打包到页面底部
        self.task_create.focus_set() #使鼠标光标直接出现在文本输入框里

        self.bind("<Return>", self.add_task) #绑定回车键，回车键按下调用add_task 函数， 注意： 这里函数名不能带（），不然就成了函数的返回值了
        self.color_schemes = [{"bg":"lightgrey", "fg":"black"},{"bg":"grey","fg":"white"}] #定义主题列表，主题里是两个字典，对应两种主题


    def add_task(self, event=None):
        task_text = self.task_create.get(1.0, tk.END).strip()#get 方法获取task_create的输入，参数定义获取多少， 1.0 表示从第一个字符开始，是个索引， END表示到Text窗口的最后， strip 去除行末换行符
                                                                    # 1.1 从第二个字符开始
        if len(task_text) >0: #输入非空
            new_task = tk.Label(self, text=task_text, pady=10) #创建新的task， task的label用输入传入
            _, task_style_choice = divmod(len(self.tasks),2) # divmod 计算商和余数，这里将task的数量除以2， 余数不是1就是0，奇数偶数分开
            #变量名为下划线_,表示这个变量会被丢弃不再使用
            print("--->",_)
            print(task_style_choice)
            my_scheme_choice = self.color_schemes[task_style_choice]#从主题列表里选，因为上一步余数只是0和1，主题列表也只有0和1元素
            new_task.configure(bg=my_scheme_choice["bg"])# configure方法是痛苦inter。Label的所属方法之一，用来config lable的属性， label.configure([option=value, ...])， 可以动态改变属性
            new_task.configure(fg=my_scheme_choice["fg"])

            new_task.pack(side=tk.TOP, fill = tk.X) #打包新创建的task到页面的顶部
            self.tasks.append(new_task)#将新创建的task 加入task list里
        self.task_create.delete(1.0, tk.END)#删除文本框里的内容

if __name__ == "__main__":
    todo = Todo()
    todo.mainloop()