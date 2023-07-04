import tkinter
root = tkinter.Tk()
root.geometry("600x640")

welcomenote = tkinter.Label(root, text="Your long textYour long textYour long textYour long textYour long textYour long text", font="helvetica 14", wraplength=300, justify="center")
welcomenote.bind('<Configure>', lambda e: welcomenote.config(wraplength=welcomenote.winfo_width()))
welcomenote.pack()

root.mainloop()