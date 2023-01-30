from tkinter import *
from tkinter import messagebox
import tkinter.messagebox
import random
import time
import datetime
import pymysql

dbc=pymysql.connect(host='localhost',user='root',passwd='',db='shyam')

c=dbc.cursor()

c.execute('select * from employee')

data=c.fetchall()

win = Tk()
win.title('EMPLOYEE PAYROLL')
win.geometry('1650x850+0+0')
win.config(bg='green')

#Frames
top = Frame(win,width=1350,height=50,bd=16,relief='sunken')
top.pack(side=TOP)

left = Frame(win,width=700,height=650,bd=16,relief='sunken')
left.pack(side=LEFT)

right = Frame(win,width=600,height=650,bd=16,relief='sunken')
right.pack(side=RIGHT)

topic = Label(top,text='Payroll Management ',font=('Calibri',50,'bold'),fg='red',bg='yellow',bd=10)
topic.grid(row=0,column=0)

left1 = Frame(left,width=700,height=100,bd=8,relief='sunken')
left1.pack(side=TOP)

left2 = Frame(left,width=325,height=400,bd=8,relief='sunken')
left2.pack(side=LEFT)

left3 = Frame(left,width=325,height=400,bd=8,relief='sunken')
left3.pack(side=RIGHT)

right1 = Frame(right,width=800,height=200,bd=42,relief='sunken')
right1.pack(side=TOP)

right2 = Frame(right,width=325,height=400,bd=16,relief='sunken')
right2.pack(side=LEFT)

right3 = Frame(right,width=325,height=400,bd=16,relief='sunken')
right3.pack(side=RIGHT)

def createwindow():
     window = Toplevel(win)
     window.title('Pay Slip')
     window.geometry('400x900')
     global close

     payslip = Text(window,width=590,height=690)
     payslip.place(x=0,y=0)
     payslip.insert(END,'\t\tPay Slip\n\n')
     payslip.insert(END,'Employee Name\t\t'+Employee_Name.get()+'\n\n')
     payslip.insert(END,'Address\t\t'+Address.get()+'\n\n')
     payslip.insert(END,'Post code\t\t'+Post_Code.get()+'\n\n')
     payslip.insert(END,'Gender\t\t'+Gender.get()+'\n\n')
     payslip.insert(END,'Refrence\t\t'+Reference.get()+'\n\n')
     payslip.insert(END,'Employer Name\t\t'+Employeer_Name.get()+'\n\n')
     payslip.insert(END,'Annual income\t\t'+City_Weighting.get()+'\n\n')
     payslip.insert(END,'Basic Salary\t\t'+Basic_Salary.get()+'\n\n')
     payslip.insert(END,'Over Time\t\t'+Over_Time.get()+'\n\n')
     payslip.insert(END,'Gross Pay\t\t'+Gross_Pay.get()+'\n\n')
     payslip.insert(END,'Net Pay\t\t'+Net_Pay.get()+'\n\n')
     payslip.insert(END,'Tax\t\t'+Tax.get()+'\n\n')
     payslip.insert(END,'Pension\t\t'+Pension.get()+'\n\n')
     payslip.insert(END,'Student Loan\t\t'+Student_Loan.get()+'\n\n')
     payslip.insert(END,'NI Payment\t\t'+NI_Payment.get()+'\n\n')
     payslip.insert(END,'Deductions\t\t'+Deductions.get()+'\n\n')
     payslip.insert(END,'Pay Date\t\t'+Pay_Date.get()+'\n\n')
     payslip.insert(END,'tax Period\t\t'+Tax_Period.get()+'\n\n')
     payslip.insert(END,'NI Number\t\t'+NI_Number.get()+'\n\n')
     payslip.insert(END,'NI Code\t\t'+NI_Code.get()+'\n\n')
     payslip.insert(END,'Tax Payable\t\t'+Tax_Payable.get()+'\n\n')
     payslip.insert(END,'Pensionable Pay\t\t'+Pensionable_Pay.get()+'\n\n')
     payslip.insert(END,'Other\t\t'+Other_Payment_Due.get()+'\n\n')
     def submit():
          a1=Employee_Name.get()
          a2=Address.get()
          a3=Post_Code.get()
          a4=Gender.get()
          a5=Reference.get()
          a6=Employeer_Name.get()
          a7=City_Weighting.get()
          a8=Basic_Salary.get()
          a9=Over_Time.get()
          a10=Gross_Pay.get()
          a11=Net_Pay.get()
          a12=Tax.get()
          a13=Pension.get()
          a14=Student_Loan.get()
          a15=NI_Payment.get()
          a16=Deductions.get()
          a17=Pay_Date.get()
          a18=Tax_Period.get()
          a19=NI_Number.get()
          a20=NI_Code.get()
          a21=Tax_Payable.get()
          a22=Pensionable_Pay.get()
          a23=Other_Payment_Due.get()
          
          sql = "INSERT INTO employee(EmployeName,Address,PostCode,Gender,Reference,EmployeerName,HR,BasicSalary,OverTime,GrossPay,NetPay,Tax,Pension,StudentLoan,NIPayment,Deductions,PayDate,TaxPeriod,NINumber,NICode,TaxPayable,PensionablePay,OtherPaymentDue)VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
          val = (a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23)
          c.execute(sql,val)
          dbc.commit()  
          
          dbc.rollback()
          dbc.close()
     butn = Button(window,text='Submit',command=submit)
     butn.place(x=350,y=0)
     for i in data:
       print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
       print(i)

#Variables
Employee_Name=StringVar()
Address=StringVar()
Post_Code=StringVar()
Gender=StringVar()
Reference=StringVar()
Employeer_Name=StringVar()
City_Weighting=StringVar()
Basic_Salary=StringVar()
Over_Time=StringVar()
Gross_Pay=StringVar()
Net_Pay=StringVar()
Tax=StringVar()
Pension=StringVar()
Student_Loan=StringVar()
NI_Payment=StringVar()
Deductions=StringVar()
Pay_Date=StringVar()
Tax_Period=StringVar()
NI_Number=StringVar()
NI_Code=StringVar()
Tax_Payable=StringVar()
Pensionable_Pay=StringVar()
Other_Payment_Due=StringVar()

#Functions
def close():
     win.destroy()

def reset():
     Employee_Name.set('')
     Address.set('')
     Post_Code.set('')
     Gender.set('')
     Reference.set('')
     Employeer_Name.set('')
     City_Weighting.set('')
     Basic_Salary.set('')
     Over_Time.set('')
     Gross_Pay.set('')
     Net_Pay.set('')
     Tax.set('')
     Pension.set('')
     Student_Loan.set('')
     NI_Payment.set('')
     Deductions.set('')
     Pay_Date.set('')
     Tax_Period.set('')
     NI_Number.set('')
     NI_Code.set('')
     Tax_Payable.set('')
     Pensionable_Pay.set('')
     Other_Payment_Due.set('')
def reference():
     Pay_Date.set(time.strftime('%d/%m/%Y'))

     ref = random.randint(10000,60000)
     ref1 = ('PR'+str(ref))
     Reference.set(ref1)

     ninum = random.randint(10000,60000)
     ninum1 = ('NI'+str(ninum))
     NI_Number.set(ninum1)

     nico = random.randint(10000,60000)
     nico1 = ('NICODE'+str(nico))
     NI_Code.set(nico1)

     d = datetime.datetime.now()
     Tax_Period.set(d.month)

def month():
     bs = float(Basic_Salary.get())
     tra = float(City_Weighting.get())
     ot = float(Over_Time.get())
     
     gp = 'Rs',str(ot+bs+tra)
     Gross_Pay.set(gp)

     t = ((bs+ot+tra) * 0.1)
     t1 = 'Rs',str('%.2f'%t)
     Tax.set(t1)

     pe = ((bs+ot+tra) * 0.02)
     pe1 = 'Rs',str('%.2f'%pe)
     Pension.set(pe1)

     loan = ((bs+ot+tra) * 0.012)
     loan1 = 'Rs',str(loan)
     Student_Loan.set(loan1)

     nip = ((bs+ot+tra) * 0.011)
     nip1 = 'Rs',str('%.2f'%nip)
     NI_Payment.set(nip1)

     dec = (t+pe+loan+nip)
     dec1 = 'Rs',str('%.2f'%dec)
     Deductions.set(dec1)

     netp = (bs+tra+ot)-dec
     netp1 = 'Rs',str(netp)
     Net_Pay.set(netp1)

     Tax_Payable.set(t1)
     Pensionable_Pay.set(pe1)
     Other_Payment_Due.set(' 0.00')
#Label and Entry left part
eme_name = Label(left1,text='Employee Name',font=('Calibri',12,'bold'),fg='red',bg='yellow',bd=10)
eme_name.grid(row=0,column=0)

eme1 = Entry(left1,bd=20,font=('Calibri',12,'bold'),width=54,justify='left',textvariable=Employee_Name)
eme1.grid(row=0,column=1)

add = Label(left1,text='Address',font=('Calibri',12,'bold'),fg='red',bg='yellow',bd=10)
add.grid(row=1,column=0)

add1 = Entry(left1,bd=20,font=('Calibri',12,'bold'),width=54,justify='left',textvariable=Address)
add1.grid(row=1,column=1)

ref = Label(left1,text='Reference',font=('Calibri',12,'bold'),fg='red',bg='yellow',bd=10)
ref.grid(row=2,column=0)

ref1 = Entry(left1,bd=20,font=('Calibri',12,'bold'),width=54,justify='left',textvariable=Reference)
ref1.grid(row=2,column=1)

emp = Label(left1,text='Employeer Name',font=('Calibri',12,'bold'),fg='red',bg='yellow',bd=10)
emp.grid(row=3,column=0)

emp1 = Entry(left1,bd=20,font=('Calibri',12,'bold'),width=54,justify='left',textvariable=Employeer_Name)
emp1.grid(row=3,column=1)


city= Label(left2,text='HR',font=('Calibri',12,'bold'),fg='red',bg='yellow',bd=10)
city.grid(row=0,column=0)

city1 = Entry(left2,bd=10,font=('Calibri',12,'bold'),width=18,justify='left',textvariable=City_Weighting)
city1.grid(row=0,column=1)

basic= Label(left2,text='Basic Salary',font=('Calibri',12,'bold'),fg='red',bg='yellow',bd=10)
basic.grid(row=1,column=0)

basic1 = Entry(left2,bd=10,font=('Calibri',12,'bold'),width=18,justify='left',textvariable=Basic_Salary)
basic1.grid(row=1,column=1)

over= Label(left2,text='Over Time',font=('Calibri',12,'bold'),fg='red',bg='yellow',bd=10)
over.grid(row=2,column=0)

over1 = Entry(left2,bd=10,font=('Calibri',12,'bold'),width=18,justify='left',textvariable=Over_Time)
over1.grid(row=2,column=1)

gross= Label(left2,text='Gross Pay',font=('Calibri',12,'bold'),fg='red',bg='yellow',bd=10)
gross.grid(row=3,column=0)

gross1 = Entry(left2,bd=10,font=('Calibri',12,'bold'),width=18,justify='left',textvariable=Gross_Pay)
gross1.grid(row=3,column=1)

net= Label(left2,text='Net Pay',font=('Calibri',12,'bold'),fg='red',bg='yellow',bd=10)
net.grid(row=4,column=0)

net1 = Entry(left2,bd=10,font=('Calibri',12,'bold'),width=18,justify='left',textvariable=Net_Pay)
net1.grid(row=4,column=1)

tax= Label(left3,text='Tax',font=('Calibri',12,'bold'),fg='red',bg='yellow',bd=10)
tax.grid(row=0,column=0)

tax1 = Entry(left3,bd=10,font=('Calibri',12,'bold'),width=18,justify='left',textvariable=Tax)
tax1.grid(row=0,column=1)

pen= Label(left3,text='Pension',font=('Calibri',12,'bold'),fg='red',bg='yellow',bd=10)
pen.grid(row=1,column=0)

pen1 = Entry(left3,bd=10,font=('Calibri',12,'bold'),width=18,justify='left',textvariable=Pension)
pen1.grid(row=1,column=1)

stud= Label(left3,text='Student Loan ',font=('Calibri',12,'bold'),fg='red',bg='yellow',bd=10)
stud.grid(row=2,column=0)

stud1 = Entry(left3,bd=10,font=('Calibri',12,'bold'),width=18,justify='left',textvariable=Student_Loan)
stud1.grid(row=2,column=1)

ni= Label(left3,text='NI Payment',font=('Calibri',12,'bold'),fg='red',bg='yellow',bd=10)
ni.grid(row=3,column=0)

ni1 = Entry(left3,bd=10,font=('Calibri',12,'bold'),width=18,justify='left',textvariable=NI_Payment)
ni1.grid(row=3,column=1)

ded= Label(left3,text='Deductions',font=('Calibri',12,'bold'),fg='red',bg='yellow',bd=10)
ded.grid(row=4,column=0)

ded1 = Entry(left3,bd=10,font=('Calibri',12,'bold'),width=18,justify='left',textvariable=Deductions)
ded1.grid(row=4,column=1)




#Entry and Label right part
post = Label(right1,text='Post Code',font=('Calibri',12,'bold'),fg='red',bg='yellow',bd=10)
post.grid(row=0,column=0)

post1 = Entry(right1,bd=10,font=('Calibri',12,'bold'),width=48,justify='left',textvariable=Post_Code)
post1.grid(row=0,column=1)

gen = Label(right1,text='Gender',font=('Calibri',12,'bold'),fg='red',bg='yellow',bd=10)
gen.grid(row=1,column=0)

gen1 = Entry(right1,bd=10,font=('Calibri',12,'bold'),width=48,justify='left',textvariable=Gender)
gen1.grid(row=1,column=1)

date = Label(right2,text='Pay Date',font=('Calibri',12,'bold'),fg='red',bg='yellow',bd=10)
date.grid(row=0,column=0)

date1 = Entry(right2,bd=10,font=('Calibri',12,'bold'),width=18,justify='left',textvariable=Pay_Date)
date1.grid(row=0,column=1)

taxp = Label(right2,text='Tax Period',font=('Calibri',12,'bold'),fg='red',bg='yellow',bd=10)
taxp.grid(row=1,column=0)

taxp1 = Entry(right2,bd=10,font=('Calibri',12,'bold'),width=18,justify='left',textvariable=Tax_Period)
taxp1.grid(row=1,column=1)

nin = Label(right2,text='NI Number',font=('Calibri',12,'bold'),fg='red',bg='yellow',bd=10)
nin.grid(row=2,column=0)

nin1 = Entry(right2,bd=10,font=('Calibri',12,'bold'),width=18,justify='left',textvariable=NI_Number)
nin1.grid(row=2,column=1)

nic = Label(right2,text='NI Code',font=('Calibri',12,'bold'),fg='red',bg='yellow',bd=10)
nic.grid(row=3,column=0)

nic1 = Entry(right2,bd=10,font=('Calibri',12,'bold'),width=18,justify='left',textvariable=NI_Code)
nic1.grid(row=3,column=1)

taxpa = Label(right2,text='Tax Payable',font=('Calibri',12,'bold'),fg='red',bg='yellow',bd=10)
taxpa.grid(row=4,column=0)

taxpa1 = Entry(right2,bd=10,font=('Calibri',12,'bold'),width=18,justify='left',textvariable=Tax_Payable)
taxpa1.grid(row=4,column=1)

pp = Label(right2,text='Pensionable Pay',font=('Calibri',12,'bold'),fg='red',bg='yellow',bd=10)
pp.grid(row=5,column=0)

pp1 = Entry(right2,bd=10,font=('Calibri',12,'bold'),width=18,justify='left',textvariable=Pensionable_Pay)
pp1.grid(row=5,column=1)

o = Label(right2,text='Other Payment Due',font=('Calibri',12,'bold'),fg='red',bg='yellow',bd=10)
o.grid(row=6,column=0)

o1 = Entry(right2,bd=10,font=('Calibri',12,'bold'),width=18,justify='left',textvariable=Other_Payment_Due)
o1.grid(row=6,column=1)

#Buttons
wbtn=Button(right3,padx=8,command=month,text='Calculate',bd=8,width=14,font=('Calibri',16,'bold'),fg='red',bg='yellow')
wbtn.grid(row=0,column=1)

pbtn=Button(right3,padx=8,text='Pay Reference',bd=8,width=14,font=('Calibri',16,'bold'),fg='red',bg='yellow',command=reference)
pbtn.grid(row=1,column=1)

pcbtn=Button(right3,padx=8,text='Pay Slip',bd=8,width=14,font=('Calibri',16,'bold'),fg='red',bg='yellow',command=createwindow)
pcbtn.grid(row=2,column=1)

rbtn=Button(right3,padx=8,text='Reset',bd=8,width=14,font=('Calibri',16,'bold'),fg='red',bg='yellow',command=reset)
rbtn.grid(row=3,column=1)

ebtn=Button(right3,padx=8,text='Exit',bd=8,width=14,font=('Calibri',16,'bold'),fg='red',bg='yellow',command=close)
ebtn.grid(row=4,column=1)







win.mainloop()



    
