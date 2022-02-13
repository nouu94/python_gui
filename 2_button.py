# tkinter는 따로 pip로 다운 받을 필요 없음. tkinter 모듈 안에 있는 모든 것을 사용 할게요.
from tkinter import *

root = Tk()
root.title("Nouu GUI")

# root.geometry("640x480")  # 가로 * 세로
# root.resizable(False, False)

btn1 = Button(root, text="버튼1")
btn1.pack()

btn2 = Button(root, padx=5, pady=10, text="버튼2")  # 동적 크기
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text="버튼3")
btn3.pack()

btn4 = Button(root, width=10, height=3, text="버튼4")  # 고정크기
btn4.pack()

btn5 = Button(root, fg="red", bg="yellow", text="버튼5")
btn5.pack()

photo = PhotoImage(file="./vImage.png")
btn6 = Button(root, image=photo)
btn6.pack()


def btncmd():
    print("버튼이 클릭되었습니다.")


# 버튼 동작
btn7 = Button(root, text="동작하는 버튼", command=btncmd)
btn7.pack()

root.mainloop()
