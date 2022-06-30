from tkinter import *
from tkinter.font import Font
root=Tk()
root.geometry('400x400')
root.title('Máy Tính Cá Nhân')
fts=Font(family='Helvetica',size=15)
drnum=8
py=5
mh=Label(root,bg='white',fg='black',width=350,height=2,font=('arial',19))
mh.pack()
mh2=Label(root,bg='white',fg='black',width=350,height=2,font=('arial',19))
mh2.pack()
fr=Frame(root)
fr.pack()
expression=''
def express(temp):
    global expression
    expression=expression+str(temp)
    mh.config(text=expression)

def calculate():
    global res
    global expression
    if(expression[-2]=='/' and expression[-1]=='0'):
        res='loi chia cho 0'
    else:
        res=eval(expression)
    file_object = open('TH1.txt', mode='a+')
    file_object.write(expression+' = '+str(res)+'\n')
    mh2.config(text=res)
    expression=''
def clear():
    global expression
    mh.config(text='')
    mh2.config(text='')
    expression=''
    print(expression)


bt7=Button(fr,text='7',font=fts,width=drnum,pady=py,command=lambda:express('7'))
bt7.grid(row=1,column=1)
bt8=Button(fr,text='8',font=fts,width=drnum,pady=py,command=lambda:express('8'))
bt8.grid(row=1,column=2)
bt9=Button(fr,text='9',font=fts,width=drnum,pady=py,command=lambda:express('9'))
bt9.grid(row=1,column=3)
btCong=Button(fr,text='+',font=fts,width=drnum,pady=py,command=lambda:express('+'))
btCong.grid(row=1,column=4)

bt4=Button(fr,text='4',font=fts,width=drnum,pady=py,command=lambda:express('4'))
bt4.grid(row=2,column=1)
bt5=Button(fr,text='5',font=fts,width=drnum,pady=py,command=lambda:express('5'))
bt5.grid(row=2,column=2)
bt6=Button(fr,text='6',font=fts,width=drnum,pady=py,command=lambda:express('6'))
bt6.grid(row=2,column=3)
btTru=Button(fr,text='-',font=fts,width=drnum,pady=py,command=lambda:express('-'))
btTru.grid(row=2,column=4)

bt1=Button(fr,text='1',font=fts,width=drnum,pady=py,command=lambda:express('1'))
bt1.grid(row=3,column=1)
bt2=Button(fr,text='2',font=fts,width=drnum,pady=py,command=lambda:express('2'))
bt2.grid(row=3,column=2)
bt3=Button(fr,text='3',font=fts,width=drnum,pady=py,command=lambda:express('3'))
bt3.grid(row=3,column=3)
btNhan=Button(fr,text='x',font=fts,width=drnum,pady=py,command=lambda:express('*'))
btNhan.grid(row=3,column=4)

bt0=Button(fr,text='0',font=fts,width=drnum,pady=py,command=lambda:express('0'))
bt0.grid(row=4,column=2)
btChia=Button(fr,text='/',font=fts,width=drnum,pady=py,command=lambda:express('/'))
btChia.grid(row=4,column=4)
btChia=Button(fr,text='.',font=fts,width=drnum,pady=py,command=lambda:express('.'))
btChia.grid(row=4,column=3)

btAC=Button(fr,text='AC',font=fts,width=drnum,pady=py,command=clear)
btAC.grid(row=5,column=3)
btBang=Button(fr,text='=',background='Blue',foreground='white',font=fts,width=drnum,pady=py,command=calculate)
btBang.grid(row=5,column=4)
root.mainloop()