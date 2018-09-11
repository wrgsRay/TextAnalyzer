"""
Python 3.6
@Author: wrgsRay
"""
from tkinter import *
from tkinter import scrolledtext
import pyperclip


class Analyzer(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        # Set title and size
        master.title('Analyze this')
        master.geometry('700x300')
        # Set padding
        self.paddingx = 50
        self.paddingy = 10

        # Set label
        self.label_text = StringVar()
        self.label_text.set('Please input text')
        self.top_label = Label(master, textvariable=self.label_text, bg='gray', font=('Arial', 12),
                               width=15, height=2)
        self.top_label.grid(row=0, column=0, columnspan=3, padx=self.paddingx, pady=self.paddingy)

        # Set input box
        self.message_box = Entry(master, width=70)
        self.message_box.focus()
        self.message_box.grid(row=1, column=0, columnspan=3, padx=self.paddingx, pady=self.paddingy)

        # Set Submit button
        self.submit_button = Button(master, text='Get Length', width=15, height=2, command=self.submit)
        self.submit_button.grid(row=2, column=0)

        # Set Copy button
        self.copy_button = Button(master, text='Copy to Clipboard', width=15, height=2, command=self.copy)
        self.copy_button.grid(row=3, column=0)

        # Set Trim button
        self.trim_button = Button(master, text='Trim to 250', width=15, height=2, command=self.trim)
        self.trim_button.grid(row=2, column=2)

        # Set Reset button
        self.reset_button = Button(master, text='Reset', width=15, height=2, command=self.reset)
        self.reset_button.grid(row=3, column=2)

    def submit(self):
        self.label_text.set('{} digits long'.format(str(len(self.message_box.get()))))

    def reset(self):
        self.label_text.set('Please input text')
        self.message_box.delete(1.0, 'end')

    def copy(self):
        pyperclip.copy(self.message_box.get())

    def trim(self):
        self.message_box.delete(250, END)


def main():
    root = Tk()
    # mainloop
    Analyzer(root)
    root.mainloop()


if __name__ == '__main__':
    main()
