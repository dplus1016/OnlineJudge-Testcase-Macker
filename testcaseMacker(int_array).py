'''
[정수 배열-예시] 
<in 파일>
5
3 5 100 7 85

<out 파일>
200
'''
import tkinter
from math import*
import tkinter.ttk
import random as rn
import exCode

window=tkinter.Tk()
window.title("Online Judge Testcase Generator v.1 by 득쌤")
window.geometry("640x400")
window.resizable(False, True)

def delete1(event):
    entry1.delete(0,10)
def delete2(event):
    entry2.delete(0,10)
def delete3(event):
    entry3.delete(0,10)
def delete4(event):
    entry4.delete(0,10)
def delete5(event):
    entry5.delete(3,20)
def inputDG():
    a=int(entry1.get())
    b=int(entry2.get())
    c=int(entry3.get())
    d=int(entry4.get())
    P=str(entry5.get())
    for i in range(1,51):
        file=open(P+str(i)+'.in','w')
        file.write('')
        n=str(rn.randint(a,b))
        file.write(n+'\n')
        for i in range(int(n)):
            t=str(rn.randint(c, d))
            file.write(t+' ')
    file.close()
    button1.config(text="입력 데이터 생성 완료")

def outputDG():
    P=str(entry5.get())
    for i in range(1,51):
        file_i=open(P+str(i)+'.in','r')    
        file_o=open(P+str(i)+'.out','w')
        n=int(file_i.readline())
        s=file_i.readline()
        ans=str(exCode.F(n,s))    
        file_o.write(ans)
        file_i.close()
        file_o.close()
    button2.config(text="출력 데이터 생성 완료")
        
label0=tkinter.Label(window, text="아래의 빈칸에 입력 데이터의 수(n값), 데이터 값(ai)의 범위와 파일의 경로를 기입하시오.")
label1=tkinter.Label(window, text="(예) 1~10000000,  d:/python/testcase/") 
entry1=tkinter.Entry(window)
entry1.insert(0,"(n의 최소값)")
entry1.bind("<Button-1>",delete1)
label2=tkinter.Label(window, text="~")
entry2=tkinter.Entry(window)
entry2.insert(0,"(n의 최대값)")
entry2.bind("<Button-1>",delete2)

label0.pack(side="top", fill="x", ipady=10)
label1.pack(side="top", fill="x")
entry1.place(x=280, y=70, width=90, height=25)
label2.place(x=370, y=70, width=20, height=25)
entry2.place(x=390, y=70, width=90, height=25)

entry3=tkinter.Entry(window)
entry3.insert(0,"(ai의 최소값)")
entry3.bind("<Button-1>",delete3)
label3=tkinter.Label(window, text="~")
entry4=tkinter.Entry(window)
entry4.insert(0,"(ai의 최대값)")
entry4.bind("<Button-1>",delete4)
entry5=tkinter.Entry(window)
entry5.insert(0,"d:/python/testcase/")
entry5.bind("<Button-1>",delete5)

entry3.place(x=280, y=100, width=90, height=25)
label3.place(x=370, y=100, width=20, height=25)
entry4.place(x=390, y=100, width=90, height=25)
entry5.place(x=280, y=130, width=200, height=25)

label4=tkinter.Label(window, text="▶입력 데이터 수의 범위")
label5=tkinter.Label(window, text="▶입력 데이터 값의 범위")
label6=tkinter.Label(window, text="▶입력 데이터 파일 경로")

label4.place(x=140, y=70)
label5.place(x=140, y=100)
label6.place(x=140, y=130)

button1=tkinter.Button(window, text="입력 데이터 생성", overrelief="solid", command=inputDG)
button1.place(x=140, y=160, width=340, height=25)

button2=tkinter.Button(window, text="출력 데이터 생성", overrelief="solid", command=outputDG)
button2.place(x=140, y=190, width=340, height=25)

label7=tkinter.Label(window, text="[주의사항]")
label7.place(x=80, y=230)

label8=tkinter.Label(window, text="1. 경로 폴더 안에 in, out 파일(파일명 1.in, 2.in, ... ,50.in)이 각각 50개가 있어야 함")
label8.place(x=80, y=250)

label9=tkinter.Label(window, text="2. 본 프로그램과 같은 폴더에 함수형태(함수명:F)로 수정된 예시코드(파일명: exCode)가 있어야 함")
label9.place(x=80, y=270)


window.mainloop()
