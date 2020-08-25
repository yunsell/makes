from tkinter import *
from time import *

root = Tk()
root.title("python 용어 연습")
n = 0

def centerWindow():
    w = 340 # 넓이
    h = 110 # 높이

    sw = root.winfo_screenwidth() # 화면 넓이
    sh = root.winfo_screenheight() # 화면 높이

    x = (sw - 400)/2
    y = (sh - 400)/2
    root.geometry('%dx%d+%d+%d' % (w, h, x, y)) # 넓이, 높이, x좌표, y좌표
centerWindow()

ex = Label(root, text="한글", font=20)
ex.grid(row=0, column=0)

kor = Entry(root, width=30)
kor.grid(row=0, column=1)

ex = Label(root, text="영어", font=20)
ex.grid(row=1, column=0)

eng = Entry(root, width=30)
eng.grid(row=1, column=1)
enb = Button(root, text="Exit", command = quit, font=20)
enb.grid(row=1, column=2)

ex = Label(root, text="▶", font=20)
ex.grid(row = 2, column=0)

typ = Entry(root, width=30)
typ.grid(row=2, column=1)

ent = Button(root, text="Enter", font=15)
ent.grid(row=2, column=2)

t = Label(root, text="기록", font=20)
t.grid(row=3, column=0)


data = [["매개변수","parameter"],
        ["변수", "variable"],
        ["객체", "object"],
        ["문자열", "string"],
        ["정수", "integer"],
        ["함수", "function"],
        ["메소드", "method"],
        ["-------끝-------","-------end-------"]]
start = time() # 기록 시작

kor.insert(0, data[n][0]) # 한글출력
eng.insert(0, data[n][1]) # 영어출력
typ.focus_set()           # 빈칸

def make_game(self) :
    global n # 전역변수 n 가져오기
    if n < len(data)-1 :
        if  data[n][1] == typ.get(): # 일치하면
            kor.delete(0, END) #입력창들 지우기
            eng.delete(0, END)
            typ.delete(0, END)
            n = n + 1
            kor.insert(0, data[n][0])
            eng.insert(0, data[n][1])

        else:
            data[n][1] != typ.get()
            typ.delete(0, END)
            typ.insert(0, "다시 시도!")

    if n == 7:
            typ.delete(0, END)
            typ.insert(0, "수고하셨습니다! 기록은 아래에서 :)")
            return

    if n < len(data)-1 :
        end = time()
        et = end - start
        et = format(et, " .2f")
        t.configure(text = " ")
        t.configure(text = et + "초")


root.bind('<Return>', make_game) # 엔터키 활성화

root.mainloop()

