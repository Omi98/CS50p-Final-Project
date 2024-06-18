# imports
from tkinter import *
from tkinter import messagebox
import tkinter as tk


# globals
global cal_gui, entry1, entry2
global num1, num2, answer
global selected_option, option
num1 = 0
num2 = 0
answer = 0
option = None


def main():
    global cal_gui
    cal_gui = calculatorGUI()
    root = cal_gui.createWindow()  # create window

    root.mainloop()

# functions
def proceedClick():
    global cal_gui
    cal_gui.proceedFrame()

def save_option():
    global cal_gui, selected_option
    global option
    
    option = selected_option.get()

def submit():
    global cal_gui, entry1, entry2
    global option
    global num1, num2, answer

    try:
        num1 = int(entry1.get())
        num2 = int(entry2.get())
    except ValueError:
        cal_gui.handle_vError()
    
    if option == 'a':
        answer = num1 + num2
        cal_gui.display_answer()
    elif option == 's':
        answer = num1 - num2
        cal_gui.display_answer()
    elif option == 'm':
        answer = num1 * num2
        cal_gui.display_answer()
    else:  # option == 'd'
        if num2 != 0:
            answer = num1 // num2
            cal_gui.display_answer()
        else:
            # 0 division error
            cal_gui.handle_0Error()    


# calculator gui class
class calculatorGUI:
    def __init__(self):
        pass

    def createWindow(self):
        self.myWindow = Tk()
        self.myWindow.title("My Calculator")
        self.myWindow.geometry("400x600")
        self.welcomeFrame()  # call func. to create frame
        return self.myWindow
    
    def welcomeFrame(self):
        self.wFrame = LabelFrame(self.myWindow, padx=15, pady=150, relief="flat")
        self.wFrame.pack(anchor=CENTER)
        self.welcomeLabel()  # call func. to create label
        self.proceedButton()  # call func. to create proceed button
        self.exitButton()  # call func. to create exit button

    def welcomeLabel(self):
        self.myLabel = Label(self.wFrame, text="Welcome to Calculator", font=("Arial", 20))
        self.myLabel.grid(row=0, column=0, sticky="we", pady=15)

    def proceedButton(self):
        self.pButton = Button(self.wFrame, text="Proceed", width=10, command=proceedClick)
        self.pButton.grid(row=1, column=0, pady=5)

    def exitButton(self):
        self.eButton = Button(self.wFrame, text="Exit", width=10, command=self.myWindow.quit)
        self.eButton.grid(row=2, column=0, pady=5)

    def proceedFrame(self):
        self.wFrame.destroy()
        self.pFrame = LabelFrame(self.myWindow, padx=25, pady=100, relief="flat")
        self.pFrame.pack(anchor=W)
        self.createLabels()  # create labels
        self.createFields()  # create entry fields
        self.createOptions()  # create radio buttons for options
        self.submitButton()  # create submit button

    def createLabels(self):
        label1 = Label(self.pFrame, text="Enter first number")
        label1.grid(row=0, column=0, sticky="W")

        label2 = Label(self.pFrame, text="Enter second number")
        label2.grid(row=1, column=0, sticky="W")

    def createFields(self):
        global entry1, entry2

        entry1 = Entry(self.pFrame)
        entry1.grid(row=0, column=1, sticky="E", padx=15)

        entry2 = Entry(self.pFrame)
        entry2.grid(row=1, column=1, sticky="E", padx=15)

    def createOptions(self):
        global selected_option
        selected_option = tk.StringVar()
        selected_option.set(None)

        # text
        label3 = Label(self.pFrame, text="Choose one operation")
        label3.grid(row=2, column=0, sticky="W", pady=(20, 0))
        
        # create buttons
        r1 = Radiobutton(self.pFrame, text="Add", variable=selected_option, value='a', command=save_option)
        r2 = Radiobutton(self.pFrame, text="Subtract", variable=selected_option, value='s', command=save_option)
        r3 = Radiobutton(self.pFrame, text="Multiply", variable=selected_option, value='m', command=save_option)
        r4 = Radiobutton(self.pFrame, text="Divide", variable=selected_option, value='d', command=save_option)

        # display buttons on grid
        r1.grid(row=3, column=0, sticky="W")
        r2.grid(row=4, column=0, sticky="W")
        r3.grid(row=5, column=0, sticky="W")
        r4.grid(row=6, column=0, sticky="W")

    def submitButton(self):
        myButton = Button(self.pFrame, text="Submit", command=submit)
        myButton.grid(row=7, column=1, sticky="W", padx=15, pady=10)

    def display_answer(self):
        global answer
        self.myWindow.quit()
        messagebox.showinfo("Answer", f"The answer is {answer}")

    def handle_vError(self):
        self.myWindow.quit()
        messagebox.showerror("Value Error", "Make sure you are entering 2 integers!")

    def handle_0Error(self):
        self.myWindow.quit()
        messagebox.showerror("Zero Division Error", "Number cannot be divided by zero!")


if __name__ == "__main__":
    main()