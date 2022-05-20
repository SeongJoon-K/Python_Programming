from tkinter import *

window = Tk()


def change_img():
    path = inputBox.get()
    img = PhotoImage(file=path)

    imageLabel.configure(image=img)
    imageLabel.image = img


photo = PhotoImage(
    file="/Users/seongjoon/Desktop/인공지능프기실/chap9/back.gif")
imageLabel = Label(window, image=photo)
imageLabel.pack()

inputBox = Entry(window)
inputBox.pack()

button = Button(window, text='Submit', command=change_img)
button.pack()

window.mainloop()
