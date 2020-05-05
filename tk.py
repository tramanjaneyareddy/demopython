from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pymysql
class student:
    def __init__(self,win):
        self.win=win
        self.win.title('ram')
        self.win.geometry('1350x700+0+0')
        #variables
        self.rollno=StringVar()
        self.name=StringVar()
        self.branch=StringVar()
        self.phoneno=StringVar()

        title=Label(self.win,text="SCHOOL MANAGEMENT SYSTEM",font=('serif',20,'bold'),bg='green',fg='white',relief=GROOVE)
        title.pack(side=TOP,fill=X)
        #frame1
        frame1=Frame(self.win,bd=10,relief=RIDGE)
        frame1.place(x=20,y=70,height=600,width=400)
        title=Label(frame1,text='STUDENT REGESTRAITION').grid(row=0,columnspan=7)
        l_rollno=Label(frame1,text='ROLL NO').grid(row=1,column=0)
        rollnotext=Entry(frame1,bd=5,relief=GROOVE,textvariable=self.rollno).grid(row=1,column=2)
        l_name = Label(frame1, text='NAME').grid(row=2, column=0)
        nametext = Entry(frame1, bd=5, relief=GROOVE, textvariable=self.name).grid(row=2, column=2)
        l_branch=Label(frame1,text='BRANCH').grid(row=3,column=0)
        branchtext=Entry(frame1,bd=5,relief=GROOVE,textvariable=self.branch).grid(row=3,column=2)
        l_phone= Label(frame1, text='PHONE NO').grid(row=4, column=0)
        phonetext = Entry(frame1, bd=5, relief=GROOVE, textvariable=self.phoneno).grid(row=4, column=2)

        #buttonframe
        btn_frame = Frame(frame1, bd=5, relief=RIDGE,bg='red')
        btn_frame.place(x=5, y=200,width=370)
        # btn_frame.place(x=10, y=200,width=370)
        add=Button(btn_frame,text='add',command=self.add,width=6).grid(row=0,column=0,padx=4)
        update=Button(btn_frame,text='update',command=self.update,width=6).grid(row=0,column=1,padx=4)
        delete=Button(btn_frame,text='delete',command=self.delete_date,width=6).grid(row=0,column=2,padx=4)
        clear=Button(btn_frame,text='clear',width=6,command=self.clear).grid(row=0,column=3,padx=4)
        exit=Button(btn_frame,text='exit',width=6,command=self.extit).grid(row=0,column=4,padx=4)

        #show data frame
        frame2=Frame(self.win,bd=10,relief=RIDGE)
        frame2.place(x=430,y=70,height=600,width=900)
        l_serch=Label(frame2,text='serch by',font=('serif',20,'bold'),fg='red').grid(row=0,column=0)
        comb_serch=ttk.Combobox(frame2,font=('serif',20,'bold'),state='readonly')
        comb_serch['values'] =('ROLL NO',)
        comb_serch.grid(row=0,column=1)
        text_srech=Entry(frame2,textvariable=self.rollno,font=('sanserif',20,'bold')).grid(row=0,column=4,padx=10)
        serach_button=Button(frame2,text='serach',command=self.get).grid(row=0,column=5)
        show_button=Button(frame2,text='show all',command=self.fetch_data).grid(row=0,column=6,padx=10)



        #tableframe

        tableframe = Frame(frame2, bd=10, relief=RIDGE)
        tableframe.place(x=20, y=70, height=500, width=700)
        scroll_x=Scrollbar(tableframe,orient=HORIZONTAL)
        scroll_y=Scrollbar(tableframe,orient=VERTICAL)
        self.student_table=ttk.Treeview(tableframe,columns=('ROLL NO','NAME','BRANCH','PHONE NO'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        self.student_table.heading('ROLL NO',text='ROLL NO')
        self.student_table.heading('NAME',text='NAME')
        self.student_table.heading('BRANCH',text='BRANCH')
        self.student_table.heading('PHONE NO',text='PHONE NO')
        self.student_table['show']='headings'
        self.student_table.column('ROLL NO',width=100)
        self.student_table.column('NAME',width=100)
        self.student_table.column('BRANCH',width=100)
        self.student_table.column('PHONE NO',width=100)
        self.student_table.pack(fill=BOTH,expand=1)
        self.fetch_data()
        self.student_table.bind("<ButtonRelease-1>",self.get_cursor)


    def add(self):
       if self.rollno.get()=='' or self.name.get()=='' or self.branch.get()=='':
           messagebox.showinfo('info','all feilds required')
       else:
        con=pymysql.connect(host='localhost',user='root',password='',database='std')
        cur=con.cursor()
        cur.execute("insert into student values(%s,%s,%s,%s)",(self.rollno.get(),self.name.get(),self.branch.get(),self.phoneno.get()))
        con.commit()
        messagebox.showinfo('add status','inserted successfully')
        self.fetch_data()
        self.clear()
        con.close()
    def fetch_data(self):
       con=pymysql.connect(host='localhost',user='root',password='',database='std')
       cur=con.cursor()
       cur.execute("select * from student")
       rows=cur.fetchall()
       if len(rows)!= 0:
           self.student_table.delete(*self.student_table.get_children())
           for row in rows:
               self.student_table.insert('',END,values=row)
           con.commit()
       con.close()

    def clear(self):
        self.rollno.set('')
        self.name.set('')
        self.branch.set('')
        self.phoneno.set('')

    def get_cursor(self,ev):
        cursor_row=self.student_table.focus()
        content=self.student_table.item(cursor_row)
        row=content['values']
        self.rollno.set(row[0])
        self.name.set(row[1])
        self.branch.set(row[2])
        self.phoneno.set(row[3])

    def update(self):
        if self.name.get()=='' or self.branch.get()=='' or self.rollno.get()=='':
            messagebox.showinfo('info',"update all feilds")
        else:
         con = pymysql.connect(host='localhost', user='root', password='', database='std')
         cur = con.cursor()
         cur.execute("update student set name='" + self.name.get() + "',branch='" + self.branch.get() + "',phoneno='"+ self.phoneno.get() +"' WHERE rollno='"+ self.rollno.get() +"'")
         con.commit()
         messagebox.showinfo('update','insereted successfully')
         self.fetch_data()
         self.clear()
         con.close()

    def delete_date(self):
        if id=='':
            messagebox.showinfo('del status','id feild is manadatary')
        else:
          con = pymysql.connect(host='localhost', user='root', password='', database='std')
          cur = con.cursor()
          cur.execute("delete from student where rollno=%s",self.rollno.get())
          con.commit()
          messagebox.showinfo('delete status','insereted successfully')
          self.clear()
          self.fetch_data()
          con.close()
    def get(self):
        con = pymysql.connect(host='localhost', user='root', password='', database='std')
        cur = con.cursor()
        cur.execute("select * from student where rollno=%s ", self.rollno.get())
        rows=cur.fetchall()
        for row in rows:
            self.rollno.initialize(row[0])
            self.name.initialize(row[1])
            self.branch.initialize(row[2])
            self.phoneno.initialize(row[3])
        con.close()
    def extit(self):
        exit()

          

win=Tk()
ob=student(win)
win.mainloop()


