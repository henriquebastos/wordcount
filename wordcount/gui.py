import tkinter as tk
from tkinter.filedialog import askopenfile
from tkinter.scrolledtext import ScrolledText

from wordcount.cmd import top_words, count_words, read_words

root = tk.Tk()


class SmartScrolledText(ScrolledText):
    @property
    def content(self):
        return self.get(1.0, tk.END)

    @content.setter
    def content(self, value):
        self.delete(1.0, tk.END)
        self.insert(tk.INSERT, value)


class Application(tk.Frame):
    COUNT = 'c'
    TOP = 't'

    MODES = {
        COUNT: count_words,
        TOP: top_words,
    }

    def __init__(self, master=None):
        super().__init__(master)

        self.words = []
        self.mode = tk.StringVar()
        self.mode.set(self.COUNT)

        self.textarea = None

        self.create_widgets()

    def read_words(self):
        self.words = read_words(askopenfile())
        self.show_words()

    def show_words(self):
        command = self.MODES[self.mode.get()]
        self.textarea.content = command(self.words)

    def create_widgets(self):
        self.pack()

        tk.Radiobutton(master=root, text='Count', variable=self.mode, value=self.COUNT,
                       command=self.show_words).pack(side="top")
        tk.Radiobutton(master=root, text='Top', variable=self.mode, value=self.TOP,
                       command=self.show_words).pack(side="top")

        tk.Button(master=root, text='Open file', command=self.read_words).pack()

        self.textarea = SmartScrolledText(master=root, wrap=tk.WORD, width=50, height=20)
        self.textarea.pack(padx=10, pady=10, fill=tk.BOTH, expand=True, side="bottom")


def gui():
    app = Application(master=root)
    app.mainloop()
