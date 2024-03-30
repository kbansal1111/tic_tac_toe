import tkinter as tk
from tkinter import messagebox

class App:
    def __init__(self, window):
        self.window = window
        self.listMain = []
        self.turn = tk.StringVar(window)
        self.head = tk.Label(window, text='Player O', font=('Times New Roman', 25))
        self.head.pack()
        self.frame1 = tk.Frame(window, height=20, width=20)
        self.frame1.pack()
        self.btn1 = tk.Button(self.frame1, height=3, width=7, font=('Times New Roman', 25), command=lambda: self.change(1))
        self.btn2 = tk.Button(self.frame1, height=3, width=7, font=('Times New Roman', 25), command=lambda: self.change(2))
        self.btn3 = tk.Button(self.frame1, height=3, width=7, font=('Times New Roman', 25), command=lambda: self.change(3))
        self.btn4 = tk.Button(self.frame1, height=3, width=7, font=('Times New Roman', 25), command=lambda: self.change(4))
        self.btn5 = tk.Button(self.frame1, height=3, width=7, font=('Times New Roman', 25), command=lambda: self.change(5))
        self.btn6 = tk.Button(self.frame1, height=3, width=7, font=('Times New Roman', 25), command=lambda: self.change(6))
        self.btn7 = tk.Button(self.frame1, height=3, width=7, font=('Times New Roman', 25), command=lambda: self.change(7))
        self.btn8 = tk.Button(self.frame1, height=3, width=7, font=('Times New Roman', 25), command=lambda: self.change(8))
        self.btn9 = tk.Button(self.frame1, height=3, width=7, font=('Times New Roman', 25), command=lambda: self.change(9))
        self.btn1.grid(row=0,column=0, padx=2, pady=2)
        self.btn2.grid(row=0,column=1, padx=2, pady=2)
        self.btn3.grid(row=0,column=2, padx=2, pady=2)
        self.btn4.grid(row=1,column=0, padx=2, pady=2)
        self.btn5.grid(row=1,column=1, padx=2, pady=2)
        self.btn6.grid(row=1,column=2, padx=2, pady=2)
        self.btn7.grid(row=2,column=0, padx=2, pady=2)
        self.btn8.grid(row=2,column=1, padx=2, pady=2)
        self.btn9.grid(row=2,column=2, padx=2, pady=2)

    def change(self, num):
        if num == 1 and self.btn1.cget('text') == '':
            self.turn.set('X') if self.turn.get() == 'O' else self.turn.set('O')
            self.btn1.config(text=self.turn.get())
        elif num == 2 and self.btn2.cget('text') == '':
            self.turn.set('X') if self.turn.get() == 'O' else self.turn.set('O')
            self.btn2.config(text=self.turn.get())
        elif num == 3 and self.btn3.cget('text') == '':
            self.turn.set('X') if self.turn.get() == 'O' else self.turn.set('O')
            self.btn3.config(text=self.turn.get())
        elif num == 4 and self.btn4.cget('text') == '':
            self.turn.set('X') if self.turn.get() == 'O' else self.turn.set('O')
            self.btn4.config(text=self.turn.get())
        elif num == 5 and self.btn5.cget('text') == '':
            self.turn.set('X') if self.turn.get() == 'O' else self.turn.set('O')
            self.btn5.config(text=self.turn.get())
        elif num == 6 and self.btn6.cget('text') == '':
            self.turn.set('X') if self.turn.get() == 'O' else self.turn.set('O')
            self.btn6.config(text=self.turn.get())
        elif num == 7 and self.btn7.cget('text') == '':
            self.turn.set('X') if self.turn.get() == 'O' else self.turn.set('O')
            self.btn7.config(text=self.turn.get())
        elif num == 8 and self.btn8.cget('text') == '':
            self.turn.set('X') if self.turn.get() == 'O' else self.turn.set('O')
            self.btn8.config(text=self.turn.get())
        elif num == 9 and self.btn9.cget('text') == '':
            self.turn.set('X') if self.turn.get() == 'O' else self.turn.set('O')
            self.btn9.config(text=self.turn.get())
        
        self.listMain.append([num, self.turn.get()])
        self.head.config(text = 'Player X' if self.turn.get() == 'O' else 'Player O')
        self.combo()

    def combo(self):        
        list = [[1,2,3], [4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9], [1,5,9], [3,5,7]]
        listX = []
        listO = []
        for i in self.listMain:
            if i[1] == 'X':
                listX.append(i[0])
            else:
                listO.append(i[0])
        for i in list:
            countX = 0
            countO = 0
            for j in i:
                if j in listX:
                    countX += 1
                elif j in listO:
                    countO += 1
            print(countO, countX)
            if countX == 3 or countO == 3:
                messagebox.showinfo('Hurray!','Player O Win' if self.head.cget('text') == 'Player X' else 'Player X Win')
                self.window.destroy()
                RunProgram()
                break
        if {1, 2, 3, 4, 5, 6, 7, 8, 9} == set(listX+listO):
            messagebox.showinfo('Aah!',"  It's a Tie  ")
            self.window.destroy()
            RunProgram()
        print()

def RunProgram():
    root = tk.Tk()
    root.geometry('500x500+'+str((root.winfo_screenwidth()-500)//2)+'+'+str((root.winfo_screenheight()-500)//2))
    App(root)
    root.mainloop()

RunProgram()
