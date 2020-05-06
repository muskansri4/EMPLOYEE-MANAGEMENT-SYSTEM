from tkinter import*
from PIL import ImageTk,Image
import mysql.connector
from tkinter import ttk
from PIL import ImageTk,Image 
root=Tk()

root.title("EMPLOYEE MANAGEMENT SYSTEM-----LOGIN")
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Muskan@1999",database="ems"
)


root.geometry("1370x790")
#root.iconbitmap("icon.png")

#;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;MAIN WINDOW;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
def open():
    top=Toplevel()

    top.title("EMPLOYEE MANAGEMENT SYSTEM----MENU")
    top.configure(bg='#03fcca')
    top.geometry("1370x790")
#    image1=ImageTk.PhotoImage(Image.open("empp.PNG"))
#    label20=Label(top,image=image1)
#    label20.grid(row=1,column=0)
#;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;NEW_EMPLOYEE;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    def new_employee():
         top1=Toplevel()
         top1.title("EMPLOYEE MANAGEMENT SYSTEM----NEW EMPLOYEE")
         top1.configure(bg='#03fcca')
         top1.geometry("1370x790")
         label=Label(top1,text="Please enter the details",width=70,font=50)
         label.grid(row=1,column=0)
         label=Label(top1,text="",width=90,font=50)
         label.grid(row=1,column=1)

         #details
         name=Label(top1,text="Enter your name :",width=40,font=50)
         name.grid(row=2,column=0,padx=8,pady=4)

         age=Label(top1,text="Enter your age:",width=40,font=50)
         age.grid(row=3,column=0,padx=8,pady=4)

         gender=Label(top1,text="Enter your gender :",width=40,font=50)
         gender.grid(row=4,column=0,padx=8,pady=4)

         adhar=Label(top1,text="Enter your adhar card number :",width=40,font=50)
         adhar.grid(row=5,column=0,padx=8,pady=4)
         
         father=Label(top1,text="Enter your father name :",width=40,font=50)
         father.grid(row=6,column=0,padx=8,pady=4)
         
         mother=Label(top1,text="Enter your mother name :",width=40,font=50)
         mother.grid(row=7,column=0,padx=8,pady=4)
         
         date=Label(top1,text="Enter your  date of birth :",width=40,font=50)
         date.grid(row=8,column=0,padx=8,pady=4)
         
         address=Label(top1,text="Enter your address :",width=40,font=50)
         address.grid(row=9,column=0,padx=8,pady=4)         
 
         contactno=Label(top1,text="Enter your contact number :",width=40,font=50)
         contactno.grid(row=10,column=0,padx=8,pady=4)      
         
         mail=Label(top1,text="Enter your mailId:",width=40,font=50)
         mail.grid(row=11,column=0,padx=8,pady=4)   
         
         salary=Label(top1,text="Enter your salary :",width=40,font=50)
         salary.grid(row=12,column=0,padx=8,pady=4)    
         
         namev=StringVar()
         namee=Entry(top1,width=70,textvariable=namev,bg='#97bfbd')
         namee.grid(row=2,column=1,padx=8,pady=4)
         
         agev=StringVar()
         agee=Entry(top1,width=70,textvariable=agev,bg='#97bfbd')
         agee.grid(row=3,column=1,padx=4,pady=4)
         
         genderv=StringVar()
         gendere=Entry(top1,width=70,textvariable=genderv,bg='#97bfbd')
         gendere.grid(row=4,column=1,padx=4,pady=4)
         
         adharv=StringVar()
         adhare=Entry(top1,width=70,textvariable=adharv,bg='#97bfbd')
         adhare.grid(row=5,column=1,padx=4,pady=4)
        
         fatherv=StringVar()
         fathere=Entry(top1,width=70,textvariable=fatherv,bg='#97bfbd')
         fathere.grid(row=6,column=1,padx=4,pady=4)
         
         motherv=StringVar()
         mothere=Entry(top1,width=70,textvariable=motherv,bg='#97bfbd')
         mothere.grid(row=7,column=1,padx=4,pady=4)
        
         dobv=StringVar()
         datee=Entry(top1,width=70,textvariable=dobv,bg='#97bfbd')
         datee.grid(row=8,column=1,padx=4,pady=4)
         
         addressv=StringVar()
         addresse=Entry(top1,width=70,textvariable=addressv,bg='#97bfbd')
         addresse.grid(row=9,column=1,padx=4,pady=4)
         
         contactv=StringVar()
         contactnoe=Entry(top1,width=70,textvariable=contactv,bg='#97bfbd')
         contactnoe.grid(row=10,column=1,padx=4,pady=4)
         
         mailidv=StringVar()
         maile=Entry(top1,width=70,textvariable=mailidv,bg='#97bfbd')
         maile.grid(row=11,column=1,padx=4,pady=4)
        
         salaryv=StringVar()
         salarye=Entry(top1,width=70,textvariable=salaryv,bg='#97bfbd')
         salarye.grid(row=12,column=1,padx=4,pady=4)
         def save():
                   mycursor = mydb.cursor()
                   sql = "INSERT INTO employee(name,age,gender,adhar,father,mother,dob,address,contact,mailid,salary) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

                   a=namev.get()
                   b=agev.get()
                   c=genderv.get()
                   d=adharv.get()
                   e=fatherv.get()
                   f=motherv.get()
                   g=dobv.get()
                   h=addressv.get()
                   i=contactv.get()
                   j=mailidv.get()
                   k=salaryv.get()
                   val = (a,b,c,d,e,f,g,h,i,j,k)
                   mycursor.execute(sql, val)
                   mydb.commit()
         button6=Button(top1,text="SAVE",command=save,fg='#ffffff', bg='#629c8e',width=48,height=4,font=100)
         button6.grid(row=13,column=1)
         button5=Button(top1,text="<<  PREVIOUS WINDOW",command=top1.destroy,fg='#ffffff', bg='#629c8e',width=40,height=4,font=100)
         button5.grid(row=13,column=0)
         
#;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;OLD_EMPLOYEE;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;        
    def old_employee():
         top2=Toplevel()
         top2.title("EMPLOYEE MANAGEMENT SYSTEM----PRESENT EMPLOYEE")
         top2.configure(bg='#03fcca')
         top2.geometry("1370x790")
         def delete():
             
                        
                  top6=Toplevel()
                  top6.title("EMPLOYEE MANAGEMENT SYSTEM-----UPDATE")
                  top6.geometry("1370x790")
                  top6.configure(bg='#03fcca')
                  def deletenow():
                      
                        mycursor = mydb.cursor()
                        sql="DELETE FROM employee WHERE name=%s"
                        val=(deletev.get(),)
                        mycursor.execute(sql, val)
                        mydb.commit()
                      
                  deletelabel1=Label(top6,text="",width = 155,font=500, bg='#629c8e')
                  deletelabel1.grid(row=1,column=0)   
                      
                  deletelabel2=Label(top6,text="ENTER THE EMPLOYEE NAME TO DELETE RECORD",width = 155,font=500)
                  deletelabel2.grid(row=2,column=0)
                  
                  deletelabel3=Label(top6,text="",width = 155,font=500, bg='#629c8e')
                  deletelabel3.grid(row=3,column=0)
                  
                  deletev=StringVar()
                  deleteentry=Entry(top6,width=50,textvariable=deletev)
                  deleteentry.grid(row=4,column=0,padx=8,pady=4)  
                  
                  button12=Button(top6,text="DELETE THE RECORD OF EMPLOYEE",command=deletenow,fg='#ffffff', bg='#629c8e',width=155,height=4,font=100)
                  button12.grid(row=5,column=0)
                  
                  
                  button137=Button(top6,text="<<  PREVIOUS EMPLOYEE",command=top6.destroy,fg='#ffffff', bg='#629c8e',width=155,height=4,font=100)
                  button137.grid(row=6,column=0)
    
         
         def search():
                 top5=Toplevel()
                 top5.title("EMPLOYEE MANAGEMENT SYSTEM-----SEARCH EMPLOYEE")
                 top5.configure(bg='#03fcca')
                 top5.geometry("1370x790")
                 def searchnow():
                     
                     selected=drop.get()
                     mycursor = mydb.cursor()
                     if selected=="search by.....":
                          test=Label(top5,text="HEY YOU FORGET TO PICK THE OPTION")
                          test.grid(row=11,column=0)
               
                     if selected=="name":
                         sql="SELECT * FROM employee WHERE name=%s"
                         test=Label(top5,text="RESULT ON BASIS OF NAME")
                         test.grid(row=11,column=0)
                
                     if selected=="age":
                        sql="SELECT * FROM employee WHERE age=%s"
                        test=Label(top5,text="RESULT ON BASIS OF AGE")
                        test.grid(row=11,column=0)
               
                     if selected=="gender":
                         sql="SELECT * FROM employee WHERE gender=%s"
                         test=Label(top5,text="RESULT ON BASIS OF GENDER")
                         test.grid(row=11,column=0)
                  
                     if selected=="adhar":
                         sql="SELECT * FROM employee WHERE adhar=%s"
                         test=Label(top5,text="RESULT ON BASIS OF ADHAR NUMBER")
                         test.grid(row=11,column=0)
               
                     if selected=="dob":
                          sql="SELECT * FROM employee WHERE dob=%s"
                          test=Label(top5,text="RESULT ON BASIS OF DATE OF BIRTH")
                          test.grid(row=11,column=0)
               
                     if selected=="contact":
                           sql="SELECT * FROM employee WHERE contact=%s"
                           test=Label(top5,text="RESULT ON BASIS OF CONTACT NUMBER")
                           test.grid(row=11,column=0)
               
                     if selected=="salary":
                          sql="SELECT * FROM employee WHERE salary=%s"
                          test=Label(top5,text="RESULT ON BASIS OF SALARY")
                          test.grid(row=11,column=0)
                          
                          
                     searched=searchbox.get()
                     name=(searched, )
                     result=mycursor.execute(sql,name)
                     result=mycursor.fetchall()
                     if not result:
                         result="NO MATCH FOUND"
                     searchlabel=Label(top5,text=result)
                     searchlabel.grid(row=12,column=0,padx=8,pady=4)
                     
                 searchboxlabel1=Label(top5,text="",width = 150,font=500)
                 searchboxlabel1.grid(row=1,column=0)
                 searchboxlabel2=Label(top5,text="ENTER SOMETHING TO SEARCH",width = 150,font=500)
                 searchboxlabel2.grid(row=2,column=0)
                 searchboxlabel3=Label(top5,text="",width = 150,font=500)
                 searchboxlabel3.grid(row=3,column=0)
                 
                 searchbox=Entry(top5,width=200)
                 searchbox.grid(row=4,column=0)
                 
                 searchboxlabel4=Label(top5,text="",width = 150,font=500)
                 searchboxlabel4.grid(row=5,column=0)
                 searchboxlabel5=Label(top5,text="PLEASE SELECT OPTION TO SEARCH",width = 150,font=500)
                 searchboxlabel5.grid(row=6,column=0)
                 searchboxlabel6=Label(top5,text="",width = 150,font=500)
                 searchboxlabel6.grid(row=7,column=0)
                 
                 drop=ttk.Combobox(top5,value=["SEARCH BY.....","name","age","gender","adhar","dob","contact","salary"],width=150)
                 drop.current(0)
                 drop.grid(row=8,column=0)
                 
                 button10=Button(top5,text="SEARCH NOW",command=searchnow,fg='#ffffff', bg='#629c8e',width=150,height=4,font=100)
                 button10.grid(row=9,column=0)
                 
                 button14=Button(top5,text="<<  BACK TO PREVIOUS WINDOW",command=top5.destroy,fg='#ffffff', bg='#629c8e',width=150,height=4,font=100)
                 button14.grid(row=10,column=0)
         label34=Label(top2,text="CLICK HERE TO SEARCH RECORD OF EMPLOYEE",width = 150,font=500)
         label34.grid(row=1,column=0)
         searchcustomer=Button(top2,text="SEARCH EMPLOYEE",command=search,fg='#ffffff', bg='#629c8e',width=195,height=10)
         searchcustomer.grid(row=2,column=0)
         label35=Label(top2,text="CLICK HERE TO DELETE RECORD OF EMPLOYEE",width = 150,font=500)
         label35.grid(row=3,column=0)
         
         deletecustomer=Button(top2,text="DELETE EMPLOYEE",command=delete,fg='#ffffff', bg='#629c8e',width=195,height=10)
         deletecustomer.grid(row=4,column=0)
         label36=Label(top2,text="----------------------------",width = 150,font=500)
         label36.grid(row=5,column=0)
        
         button11=Button(top2,text="<<  PREVIOUS EMPLOYEE",command=top2.destroy,fg='#ffffff', bg='#629c8e',width=195,height=10)
         button11.grid(row=6,column=0)
         
         
#;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;INFORMATION;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    def information():
        top3=Toplevel()
        top3.title("EMPLOYEE MANAGEMENT SYSTEM------INFORMATION")
        top3.configure(bg='#03fcca')
        top3.geometry("1370x790")
        def show():
            top4=Toplevel()
            top4.title("EMPLOYEE MANAGEMENT SYSTEM-------DETAILS")
            top4.geometry("1370x790")
            cursor = mydb.cursor()
            cursor.execute("SELECT * FROM employee")
            result = cursor.fetchall()
            for i,x in enumerate(result):
               n=0
               for y in x:
                    label=Label(top4,text=y)
                    label.grid(row=i,column=n)
                    n=n+1  
        button40=Button(top3,text="HERE   YOU   WILL   RECORD   OF   ALL   THE   EMPLOYEE",fg='#e368d3', bg='#03fcca',width=200,height=10)
        button40.grid(row=2,column=0)
        button9=Button(top3,text="RECORDS OF ALL THE EMPLOYEE ",command=show,fg='#ffffff', bg='#629c8e',width=200,height=10)
        button9.grid(row=3,column=0)
        button8=Button(top3,text="<< PREVIOUS WINDOW",command=top3.destroy,fg='#ffffff', bg='#629c8e',width=200,height=10)
        button8.grid(row=4,column=0)
 #'''''''''''''''''''''''''''''''''''''''''''''''''''''''MAIN WINDOW'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''        
    searchboxlabel40=Label(top,text="WELCOME TO EMPLOYEE MANAGEMENT SYSTEM",width = 155,font=500)
    searchboxlabel40.grid(row=1,column=0)   
    button1=Button(top,text="NEW EMPLOYEE",command=new_employee,fg='#ffffff', bg='#629c8e',width=200,height=10)
    button2=Button(top,text="OLD EMPLOYEE",command=old_employee,fg='#ffffff', bg='#629c8e',width=200,height=10)
    button3=Button(top,text="INFORMATION",command=information,fg='#ffffff', bg='#629c8e',width=200,height=10)
    #button4=Button(top,text="LEAVE")
    button1.grid(row=2,column=0)
    button2.grid(row=3,column=0)
    button3.grid(row=4,column=0)
    #button4.grid(row=1,column=4)
    button4=Button(top,text="<< PREVIOUS WINDOW",command=top.destroy,fg='#ffffff', bg='#629c8e',width=200,height=10)
    button4.grid(row=5,column=0)

#''''''''''''''''''''''''''''''''''''''''''''''''''''LOGIN''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#NAME.........................................................
def wrong():
        top7=Toplevel()
        top7.geometry("1370x790")
        top7.configure(bg='#03fcca')
        naame=Label(top7,text="IT'S SEEMS YOU ENTERD WRONG PASSWORD OR USERNAME",width=200)
        naame.grid(row=0,column=0,padx=5,pady=4)
        button40=Button(top7,text="< <  RETURN TO LOGIN WINDOW",command=top7.destroy,fg='#ffffff', bg='#629c8e',width=150,height=4)
        button40.grid(row=1,column=0,padx=8,pady=4)
def check():
    
    a=namev.get()
    b=passwordv.get()
    
    if a!="employee" and b!="123" :
        
            return wrong()
    if a=="employee" and b=="123" :
        
            return open()
    if a=="admin" and b=="123" :
        
            return open()

name=Label(root,text="Enter your name :",width=50,height=4,fg='#e368d3',font=50)
name.grid(row=1,column=0,padx=8,pady=4)
namev=StringVar()
namee=Entry(root,width=70,textvariable=namev,bg='#97bfbd')
namee.grid(row=2,column=0,padx=8,pady=4)
#PASSWORD.....................................................................
password=Label(root,text="Enter your password :",width = 50,height=4,fg='#e368d3',font=50)
password.grid(row=3,column=0,padx=8,pady=4)
passwordv=StringVar()
passworde=Entry(root,width=70,textvariable=passwordv,bg='#97bfbd')
passworde.grid(row=4,column=0,padx=8,pady=4)
#CHECKING....................................................................

    
submit=Button(root,text='submit',command=check,fg='#ffffff', bg='#629c8e',width=50,height=4,font=60)
submit.grid(row=5,column=0)
image1=ImageTk.PhotoImage(Image.open("emp.PNG"))
label11=Label(root,image=image1)
label11.grid(row=0,column=0)

#END....................................................................................................................................

root.configure(bg='#03fcca')
root.mainloop()
