from tkinter import *

window = Tk()
window.title("My Calculator")
display = Entry(window, width=33, bg="yellow")
display.grid(row=0, column=0, columnspan=5)

button_list = [
    '7', '8', '9', '/', 'C',
    '4', '5', '6', '*', ' ',
    '1', '2', '3', '-', ' ',
    '0', '.', '=', '+', 'C',
]

row_index = 1  # 2행부터 시작
col_index = 0  # 1열부터 시작
for button_text in button_list:  # button_text는 button_list에 있는 원소들을 이고, 이를 반복문을 통해 돌리겠다
    Button(window, text=button_text, width=5).grid(  # text는 button_text이고 너비는 5로 선언한다.
        row=row_index, column=col_index)  # 그리고 격자를 설정하고 각행과 열은 row_index, col_index로 선언함
    col_index += 1  # col_index는 반복문이 돌아갈 때마다 1씩 증가함
    if col_index > 4:  # 하지만 col_index가 4보다 클때, 그러니까 1열의 버튼 5개가 다 채워졌을 때
        row_index += 1  # 행이 추가되고
        col_index = 0  # 다시 col은 0으로 만든다.

window.mainloop()
