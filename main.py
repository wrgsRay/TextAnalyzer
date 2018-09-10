"""
Python 3.6
@Author: wrgsRay
"""
from tkinter import *


def main():

    def submit():
        label_text.set(f'{str(len(message_box.get()))} digits long')

    root = Tk()
    # Set title
    root.title('Analyze this')

    # Set size
    root.geometry('900x600')
    label_text = StringVar()
    # Set label
    top_label = Label(root, textvariable=label_text, bg='gray', font=('Arial', 12), width=15, height=2)
    top_label.pack()

    # Set input box
    message_box = Entry(root, width=100)
    message_box.pack()
    # Set button
    submit_button = Button(root, text='Submit', width=15, height=2, command=submit)
    submit_button.pack()

    # mainloop
    root.mainloop()


if __name__ == '__main__':
    main()
