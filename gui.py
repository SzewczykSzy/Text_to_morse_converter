import tkinter
from tkinter import *
from tkinter import messagebox
from convert_morse import text_to_morse, morse_to_text
import pyperclip


class Interface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Morse")
        self.window.config(bg='white', padx=10, pady=10)

        self.main_label = Label(
            text="Morse Converter", bg='white', fg='Green', font=("Comic Sans MS", 30, "bold"))
        self.main_label.grid(row=0, column=0, sticky="NEWS", columnspan=2)

        morse_image = PhotoImage(file="morse.png")
        self.canvas = Canvas(
            width=430, height=115, bg="white", highlightthickness=0)
        self.morse_img = self.canvas.create_image(218, 60, image=morse_image)
        self.canvas.grid(row=1, column=0, pady=10, columnspan=2)

        self.mode = StringVar(value='text')
        self.text = Radiobutton(
            self.window, text='Convert text', variable=self.mode, value='text', bg='white')
        self.text.grid(row=2, column=0, sticky="E", pady=10)
        self.morse = Radiobutton(
            self.window, text='Convert morse code', variable=self.mode, value='morse', bg='white')
        self.morse.grid(row=2, column=1, sticky="W")

        self.entry_label = Label(text="Enter text/code:", bg='white')
        self.entry_label.grid(row=3, column=0, sticky="W")

        self.text = StringVar()
        self.text_code = Entry(
            self.window, textvariable=self.text, highlightthickness=2, width=55)
        self.text_code.grid(row=3, column=0, columnspan=2, sticky="E")

        self.convert = Button(text="Convert", command=self.convert)
        self.convert.grid(row=4, column=0, pady=10)

        self.copy_output = Button(
            text="Copy Output", command=lambda: pyperclip.copy(self.result_canvas.itemconfig(self.result, 'text')[4]))
        self.copy_output.grid(row=4, column=1)

        self.result_canvas = tkinter.Canvas(
            width=430, height=250, bg="white")
        self.result = self.result_canvas.create_text(
            215, 125, text="---Result here---", width=400, font=("Arial", 20, "italic"))
        self.result_canvas.grid(row=5, column=0, columnspan=2, pady=10)

        self.window.mainloop()

    def convert(self):
        if self.mode.get() == 'text':
            converted_text = text_to_morse(self.text.get())
            self.result_canvas.itemconfig(
                self.result, text=f"{converted_text}")
        elif self.mode.get() == 'morse':
            try:
                converted_text = morse_to_text(self.text.get())
            except:
                messagebox.showerror(
                    title="Error", message="Entered text has non morse code elements.\nPlease, enter valid code")
            else:
                self.result_canvas.itemconfig(
                    self.result, text=f"{converted_text}")


app = Interface()
