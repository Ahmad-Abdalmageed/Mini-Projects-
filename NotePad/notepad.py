import tkinter as tk
from tkinter import filedialog as tkFile
from tkinter import messagebox as mb

# This is a Notepad Application using Python Tkinter
# It should include the following :
# 1- A NotePad to write the text
# 2- Save Button to save the file anywhere the user defines
# 3- Open button to a file from anywhere the user chooses


class NotePad(tk.Frame):
    _master = tk.Tk()
    _text = tk.Text(_master)
    _menubar = tk.Menu(_master)
    _fileMenu = tk.Menu(_menubar, tearoff=0)
    _editMenu = tk.Menu(_menubar, tearoff=0)
    _helpMenu = tk.Menu(_menubar, tearoff=0)

    _File = None
    _scrollBar = tk.Scrollbar(_text)

    def MenuCommands(self):
        self._text.grid(row=0)
        self._master.config(menu=self._menubar)
        # File Menu
        self._fileMenu.add_command(label="New", command=self.__NewFile)
        self._fileMenu.add_command(label="Open", command=self.__OpenFile)
        self._fileMenu.add_command(label="Save", command=self.__SaveFile)
        self._fileMenu.add_separator()
        self._fileMenu.add_command(label="Exit", command=self.__Exit)
        self._menubar.add_cascade(label="File", menu=self._fileMenu)
        # Edit Menu
        self._editMenu.add_command(label="Copy", command=self.__copy)
        self._editMenu.add_command(label="Paste", command=self.__paste)
        self._editMenu.add_command(label="Cut", command=self.__cut)
        self._menubar.add_cascade(label="Edit", menu=self._editMenu)
        # Help Menu
        self._helpMenu.add_command(label="About", command=self.__info)
        self._menubar.add_cascade(label="Help", menu=self._helpMenu)

    def run(self):
        self._master.mainloop()

    # File Menu Commands
    def __NewFile(self):
        self._File = None
        self._master.title("Untitled - Notepad")
        self._text.delete(1.0, tk.END)

    def __OpenFile(self):
        self._File = tkFile.askopenfilename(defaultextension=".txt", filetypes=["All Files", ("Text Documents", "*.txt")
                                                                                ])
        if self._File == "":
            self._File = None
        else:
            self.master.title(tkFile.os.path.basename(self._File) + " - Notepad")
            self._text.delete(1.0, tk.END)
            file = open(self._File, "r")
            self._text.insert(1.0, file.read())

            file.close()

    def __SaveFile(self):
        if self._File is None:
            self._File = tkFile.asksaveasfilename(title="Save File", initialdir="/",
                                                  filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")],
                                                  defaultextension=".txt",
                                                  initialfile="Untitled.txt")
            if self._File == "":
                self._File = None
            else:
                file = open(self._File, "w")
                file.write(self._text.get(1.0, tk.END))

                self._master.title(tkFile.os.path.basename(self._File) + " - NotePad")

    def __cut(self):
        self._text.event_generate("<<Cut>>")

    def __paste(self):
        self._text.event_generate("<<Paste>>")

    def __copy(self):
        self._text.event_generate("<<Copy>>")

    def __Exit(self):
        self._master.destroy()

    def __info(self):
        mb.showinfo("About", "Notepad Version 0.01 By Ahmad AbdelMageed")

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self._master.title("Untitled - Notepad")
        self._master.grid_rowconfigure(0, weight=1)
        self._master.grid_columnconfigure(0, weight=1)
        self.MenuCommands()


notepad = NotePad()
notepad.run()









