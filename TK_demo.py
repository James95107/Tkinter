from tkinter import *
import tkinter.messagebox as messagebox

class TkDemo():
    def __init__(self):
        master = Tk()
        master.title('TK学习')
        # 创建菜单栏 (Menu)
        menubar = Menu(master)
        master.config(menu=menubar)
        # 创建文件下拉菜单
        filemenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="文件", menu=filemenu)
        filemenu.add_command(label="新建···", command=self.newfile)
        filemenu.add_command(label="打开···", command=self.openfile)
        filemenu.add_command(label="保存", command=self.savefile)
        filemenu.add_command(label="关闭填写", command=master.quit)
        # 创建编辑下拉菜单
        editmenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="编辑", menu=editmenu)
        editmenu.add_command(label="红色", command=self.red)
        editmenu.add_command(label="蓝色", command=self.blue)
        editmenu.add_command(label="黄色", command=self.yellow)
        editmenu.add_command(label="正常", command=self.nomal)
        # 创建帮助下拉菜单
        helpmenu = Menu(menubar,tearoff=0)
        menubar.add_cascade(label='帮助', menu=helpmenu)
        helpmenu.add_command(label='操作说明', command=self.description)
        helpmenu.add_command(label='关于', command=self.about)

        textmenu = Menu(menubar,tearoff=0)
        menubar.add_cascade(label='<---请先阅读帮助栏中的说明!!!', menu=helpmenu)

        # 文字 (Label)
        title = Label(master, text='这是一份无趣的调查问卷--建文大帝编', font='15', bg='white', fg='red')
        title.pack()

        # 问题1放在frame1中 (Frame)
        frame1 = Frame(master)
        frame1.pack(fill=X)
        # 问题
        label1 = Label(frame1, text='1、您的花名：   ')
        label1.grid(row=1, column=0)
        # 输入框 (Entry)
        self.name = StringVar()
        entryname = Entry(frame1, textvariable=self.name)
        entryname.grid(row=1, column=1)
        # 按钮  (Button)
        getname = Button(frame1, text='点击确认', command=self.getname)
        getname.grid(row=1, column=3)

        # 问题2放在frame2中
        frame2 = Frame(master)
        frame2.pack(fill=X)
        # 问题
        label2 = Label(frame2, text='2、您的性别：   ')
        label2.grid(row=1, column=0)
        # 选择按钮 (Radiobutton)
        self.sex = StringVar()
        sex_male = Radiobutton(frame2, text='男', fg='blue', variable=self.sex, value='男', command=self.getsex)
        sex_male.grid(row=1, column=2)
        sex_female = Radiobutton(frame2, text='女', fg='red', variable=self.sex, value='女', command=self.getsex)
        sex_female.grid(row=1, column=4)

        # 问题3放在frame3中
        frame3 = Frame(master)
        frame3.pack(fill=X)
        # 问题
        label2 = Label(frame3, text='3、您的年龄：   ')
        label2.grid(row=1, column=0)
        # 滑动条 (Scale)
        self.age = Scale(frame3, from_=0, to=100, orient=HORIZONTAL, resolution=1)   # 默认垂直
        self.age.grid(row=1, column=1)
        # 按钮  (Button)
        getage = Button(frame3, text='点击确认', command=self.getage)
        getage.grid(row=1, column=2)

        # 问题4放在frame4中
        frame4 = Frame(master)
        frame4.pack(fill=X)
        # 问题
        label4 = Label(frame4, text='4、请删除您不会的编程语言：   ')
        label4.grid(row=1, column=0)
        # 列表  (Listbox)
        self.listbox = Listbox(frame4)
        self.listbox.grid(row=1, column=1)
        for item in ["C", "C++", 'JAVA', 'Python', 'R', 'SQL', 'JS']:
            self.listbox.insert(END, item)
        # 删除按钮
        DELE = Button(frame4, text="删除", command=lambda listbox=self.listbox: listbox.delete(ANCHOR))
        DELE.grid(row=1, column=2)
        # 确定按钮
        language = Button(frame4, text="确定", command=self.getlanguage)
        language.grid(row=2, column=1)

        # 问题5放在frame5中
        frame5 = Frame(master)
        frame5.pack(fill=X)
        # 问题
        label5 = Label(frame5, text='5、您喜欢哪种图案：   ')
        label5.grid(row=1, column=0)
        # 画板  (Canvas)
        self.canvas = Canvas(frame5, width=200, height=100, bg="White")
        self.canvas.grid(row=1, column=1)
        self.pattern = StringVar()
        # 图案选择按钮
        btRectangle = Button(frame5, text = "长方形", command = self.displayRect)
        btOval = Button(frame5, text="椭 圆", command=self.displayOval)
        btArc = Button(frame5, text = "圆 弧", command = self.displayArc)
        btPolygon = Button(frame5, text="多边形", command=self.displayPolygon)
        btLine = Button(frame5, text=" 线 ", command=self.displayLine)
        btString = Button(frame5, text="确定", command=self.displayString)
        btClear = Button(frame5, text="清 空", command=self.clearCanvas)
        btRectangle.grid(row = 2, column = 6)
        btOval.grid(row=2, column=2)
        btArc.grid(row=2, column=3)
        btPolygon.grid(row=2, column=4)
        btLine.grid(row=2, column=5)
        btString.grid(row=2, column=1)
        btClear.grid(row=2, column=7)

        # 问题6放在frame6中
        frame6 = Frame(master)
        frame6.pack(fill=X)
        # 问题
        label6 = Label(frame6, text='6、您喜欢的NBA球星号：   ')
        label6.grid(row=1, column=0)
        # 滚轮 (Scrollbar)
        scrollbar = Scrollbar(frame6)
        scrollbar.grid(row=1, column=2)
        # 列表
        self.listbox2 = Listbox(frame6,height=5, yscrollcommand=scrollbar.set)
        for i in range(99):
            self.listbox2.insert(END, str(i))
        self.listbox2.grid(row=1, column=1)
        scrollbar.config(command=self.listbox2.yview)
        # 确定按钮
        star = Button(frame6, text='确定', command=self.getstar)
        star.grid(row=2, column=1)

        # 问题7放在frame7中
        frame7 = Frame(master)
        frame7.pack(fill=X)
        # 问题
        label7 = Label(frame7, text='7、您最喜欢的数字是：   ')
        label7.grid(row=1, column=0)
        # (Spinbox)
        self.number = Spinbox(frame7, from_=0, to=10)
        self.number.grid(row=1, column=1)
        # 确定按钮
        number = Button(frame7, text='确定', command=self.getnumber)
        number.grid(row=1, column=2)

        # 空格
        separator = Frame(master, height=30, bg='black', relief=SUNKEN)
        separator.pack(fill=X, padx=5, pady=5)

        # frame8
        frame8 = Frame(master)
        frame8.pack()
        self.agree = StringVar()
        # 勾择按钮（Checkbutton）
        agree = Checkbutton(frame8, text="我确定此调查问卷信息准确无误", variable=self.agree, onvalue='确定', offvalue='不确定', command=self.getagree)  # 产生选择按钮
        agree.grid()

        # frame9
        frame9 = Frame(master)
        frame9.pack()
        submit = Button(frame9, text='提交', command=self.allsubmit)
        submit.grid()

        # frame10
        frame10 = Frame(master)
        frame10.pack()
        # 容器框 （LabelFrame）
        self.group = LabelFrame(frame10, text="特别鸣谢", padx=5, pady=5)
        self.group.grid()
        w = Label(self.group, text='本学习项目由衷感谢http://effbot.org/tkinterbook')
        w.pack()

        master.mainloop()

  # 属性
    # 文件栏
    def newfile(self):
        self.file = open(r'test.txt', 'w')
        self.file.close()
        messagebox.showinfo('新建文件','您已成功创建个人资料文档')   # 显示对话框
    def openfile(self):
        f = open(r'test.txt', 'r')
        try:
            f_read=f.read()
            #f_read_decode=f_read.decode('utf-8')
            print(f_read)
        finally:
            f.close()
    def savefile(self):
        messagebox.showwarning('保存文件', '亲，提交即保存哦！')    # 显示对话框

    # 编辑栏
    def red(self):
        self.group['bg'] = 'red'
    def blue(self):
        self.group['bg'] = 'blue'
    def yellow(self):
        self.group['bg'] = 'yellow'
    def nomal(self):
        self.group['bg'] = 'SystemButtonFace'

    # 帮助栏
    def description(self):
        messagebox.showinfo('Description', '1.新建您的个人资料\n2.填写调查问卷\n3.点击提交 ')   # 显示对话框
    def about(self):
        messagebox.showinfo('about', '本调查问卷是python小白建文大帝用来学习TK模块的，涵盖TK模块所有GUI界面 \n                                                              ----1.0版')   # 显示对话框

    # 名字
    def getname(self):
        name = self.name.get()
        print(name)

    # 性别
    def getsex(self):
        sex = self.sex.get()
        print(sex)

    # 年龄
    def getage(self):
        print(self.age.get())

    # 语言
    def getlanguage(self):
        print(self.listbox.get(0, END))

    # 图案
    def displayRect(self):
        self.canvas.create_rectangle(10, 10, 190, 90, tags = "rect")
        self.pattern = '长方形'
    def displayOval(self):
        self.canvas.create_oval(10, 10, 190, 90, tags = "oval", fill = "red")
        self.pattern = '椭圆'
    def displayArc(self):
        self.canvas.create_arc(10, 10, 190, 90, start = 0, extent = 90, width = 8, fill = "red", tags = "arc")
        self.pattern = '圆弧'
    def displayPolygon(self):
        self.canvas.create_polygon(10, 10, 190, 90, 30, 50, tags = "polygon")
        self.pattern = '多边形'
    def displayLine(self):
        self.canvas.create_line(10, 10, 190, 90, fill = 'red', tags = "line")
        self.canvas.create_line(10, 90, 190, 10, width = 9, arrow = "last", activefill = "blue", tags = "line")
        self.pattern = '线'
    def displayString(self):
        self.canvas.create_text(60, 40, text = "您真棒！！！", font = "Tine 10 bold underline", tags = "string")
        print(self.pattern)
    def clearCanvas(self):
        self.canvas.delete("rect", "oval", "arc", "polygon", "line", "string")

    # 球星
    def getstar(self):
        print(self.listbox2.get(ACTIVE))

    # 数字
    def getnumber(self):
        print(self.number.get())

    # 同意
    def getagree(self):
        print(self.agree.get())

    # 提交
    def allsubmit(self):
        with open(r'test.txt', 'w') as f:
            f.write('您的花名是：')
            f.write(self.name.get())
            f.write('\n您的性别为:')
            f.write(self.sex.get())
            f.write('\n您的年龄是：')
            f.write(str(self.age.get()))
            f.write('\n您会这么多编程语言：')
            for i in self.listbox.get(0, END):
                f.write(i)
                f.write(" ,")
            f.write('\n您喜欢的图案是：')
            f.write(self.pattern)
            f.write('\n您喜欢的球星号为：')
            f.write(self.listbox2.get(ACTIVE))
            f.write('\n您喜欢的数字为：')
            f.write(self.number.get())
            f.write('\n')
            f.write(self.agree.get())
            f.write('本调查问卷的真实性')
        messagebox.showinfo('Success', '恭喜您已成功提交 ')   # 显示对话框

TkDemo()

