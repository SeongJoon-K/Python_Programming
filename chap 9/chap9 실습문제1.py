from tkinter import *

window = Tk()


def displayRect():  # 사각형그리는 함수 선언
    canvas.create_rectangle(10, 10, 190, 90, tags="rect")
# 10,10 좌표와 190, 90좌표에 맞춰 사각형을 그리는 함수이다


def displayOval():  # 타원출력하는 함수 선언
    canvas.create_arc(10, 10, 190, 90, fill="red", tags="oval")
# 10,10의 점, 190,90점의 대각선을 맞추고 빨간색이 채워진 타원을 그린다.


def displayArc():  # 함수를 선언
    canvas.create_arc(10, 10, 190, 90, start=0, extent=90,
                      width=8, fill="red", tag="arc")
# 10,10 190,90을 기준으로 하고, 0부터 90도 까지 그리고, 두께는 8, 색은 빨간색인 호를 그린다


def displayPolygon():  # 함수를 선언
    canvas.create_polygon(10, 10, 190, 90, 30, 50, tags="polygon")
# 10,10 190,90을 기준으로 하고 a = 10,10 b = 190,90 c = 30,50 세 점으로 하는 삼각형을 출력한다.


def displayLine():  # 선분을 출력하는 함수 선언
    # 10,10 과 190,90을 잇는 선분을 생성 색깔은 빨간색으로 함
    canvas.create_line(10, 10, 190, 90, fill="red", tags="line")
    canvas.create_line(10, 90, 190, 10, width=9, arrow="last",  # 10,90 과 190,10 을 잇는 선분을 그리고, 두께는 9로함
                       activefill="blue", tags="line")  # 그리고 선의 끝지점의 화살표를 지정하고,마우스 지정시 파란색을 설정한다.


def displayString():  # 문자열 출력함수
    canvas.create_text(60, 40, text="Hi, I am string",  # 60,40에 텍스트를 출력하고, font, 사이즈, 굵기, 밑줄을 설정한다.
                       font="Times 10 bold underline", tags="string")


def clearCanvas():  # 컨버스를 지우는함수를 선언
    # 아래의 tags들을 지운다.
    canvas.delete("rect", "oval", "arc", "polygon", "line", "string")


window = Tk()  # 위젯을 출력할 윈도우 창을 선언함
window.title("Canvas 그리기")  # 창의 제목 설정

# 윈도우 창에 캔버스 배치
# canvas는 너비200, 높이 100으로 배경색은 흰색으로 함
canvas = Canvas(window, width=200, height=100, bg="white")
canvas.pack()  # 배치관리자 설정
# 프레임에 버튼을 배치한다
frame = Frame(window)  # 윈도우 안에 프레임을 설정한다.
frame.pack()  # 배치관리자 설정

# 사각형을 만드는 버튼을 설정 누르면 사각형을 그려줌
btRectangle = Button(frame, text="Rectangle", command=displayRect)
btOval = Button(frame, text="Oval", command=displayOval)  # 누르면 타원을 그려주는 버튼생성
btArc = Button(frame, text="Arc", command=displayArc)  # 누르면 호를 그려주는 버튼을 생성
# 누르면 다각형(삼각형)을 그리는 버튼을 생성
btPolygon = Button(frame, text="Polygon", command=displayPolygon)
btLine = Button(frame, text="Line", command=displayLine)  # 누르면 선분을 그려주는 버튼을 생성
# 누르면 텍스트를 출력해주는 버튼을 생성함
btString = Button(frame, text="String", command=displayString)
btClear = Button(frame, text="Clear", command=clearCanvas)  # 컨버스를 지우는 버튼생성

btRectangle.grid(row=1, column=1)  # 사각형버튼은 1,1행렬에
btOval.grid(row=1, column=2)  # 타원버튼 1,2행렬에
btArc.grid(row=1, column=3)  # 호의 버튼은 1,3행렬
btPolygon.grid(row=1, column=4)  # 다각형 버튼 1,4행렬
btLine.grid(row=1, column=5)  # 선 긋는 버튼은 1,5 행렬
btString.grid(row=1, column=6)  # 문자열출력 버튼 1,6 행렬
btClear.grid(row=1, column=7)  # 초기화 버튼은 1,7버튼
window.mainloop()  # 프로그램이 실행되도록 메인루프 실행
