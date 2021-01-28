


import tkinter
window = tkinter.Tk()

frame = tkinter.Frame(window)
frame.pack()
myLabel = tkinter.Label(frame, text="Enter something:")
myLabel.pack()
myText = tkinter.Entry(frame)
myText.pack()

def signUp():
    import database
    database.insertMessage(myText.get())
    
    
myButton = tkinter.Button(frame, text="Sign Up",
                          command=signUp )
myButton.pack()
tkinter.mainloop()
