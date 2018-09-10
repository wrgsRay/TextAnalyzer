"""
Python 3.6
@Author: wrgsRay
"""
from tkinter import *


class Analyzer(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        # Set title and size
        master.title('Analyze this')
        master.geometry('900x600')

        # Set label
        self.label_text = StringVar()
        self.top_label = Label(master, textvariable=self.label_text, bg='gray', font=('Arial', 12),
                               width=15, height=2)
        self.top_label.pack()

        # Set input box
        self.message_box = Entry(master, width=100)
        self.message_box.focus()
        self.message_box.pack()

        # Set Submit button
        self.submit_button = Button(master, text='Submit', width=15, height=2, command=self.submit)
        self.submit_button.pack()

        # Set Reset button
        self.reset_button = Button(master, text='Reset', width=15, height=2, command=self.reset)
        self.reset_button.pack()

    def submit(self):
        self.label_text.set('{} digits long'.format(str(len(self.message_box.get()))))

    def reset(self):
        self.label_text.set('')
        self.message_box.delete(0, 'end')


def main():
    root = Tk()
    # mainloop
    Analyzer(root).pack(expand=True, fill='both')
    root.mainloop()


if __name__ == '__main__':
    main()
