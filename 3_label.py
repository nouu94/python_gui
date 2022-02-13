# tkinter는 따로 pip로 다운 받을 필요 없음. tkinter 모듈 안에 있는 모든 것을 사용 할게요.
from tkinter import *

root = Tk()
root.title("Nouu GUI")

# label 글자만 보여준다, 이미지만 보여준다.
label1 = Label(root, text="안녕하세요")
label1.pack()

photo = PhotoImage(file="./vImage.png")
label2 = Label(root, image=photo)
label2.pack()

# 함수 내에서 레이블의 이미지 값을 바꾸려면 photo 값을 전역 변수로 놓는다.


def change():
    label1.config(text="또 만나요")

    global photo2
    photo2 = PhotoImage(file="./xImage.png")
    label2.config(image=photo2)


btn = Button(root, text="클릭", command=change)
btn.pack()

root.mainloop()
