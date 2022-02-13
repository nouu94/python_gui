# tkinter는 따로 pip로 다운 받을 필요 없음. tkinter 모듈 안에 있는 모든 것을 사용 할게요.
from tkinter import *

root = Tk()
root.title("Nouu GUI")
root.geometry("640x480")  # 가로 * 세로
# 가로 * 세로 + x좌표 + y좌표, 창 크기도 조절할 수 있고 나타나는 위치도 조절 가능합니다.
# root.geometry("640x480+300+100")

root.resizable(False, False)  # x(너비), y(높이) 값 변경 불가 (창 크기 변경 불가)

root.mainloop()
