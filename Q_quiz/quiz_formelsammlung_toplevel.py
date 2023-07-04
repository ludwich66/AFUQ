''' Toplevel'''
import tkinter as tk
from tkinter import ttk
import PIL.Image

''' Toplevel'''
import tkinter as tk
from tkinter import ttk
import PIL.Image

class ScrolledCanvas(tk.Toplevel):
    def __init__(self, parent=None, image_filename=None): 
        tk.Toplevel.__init__(self, parent)
        self.master.title("Formelsammlung")

        canv = tk.Canvas(self, relief=tk.SUNKEN)
        canv.config(width=1000, height=700)
        canv.config(highlightthickness=0)
        canv.grid(row=0, column=0, sticky='nwes')

        sbarV = tk.Scrollbar(self, orient=tk.VERTICAL)
        sbarH = tk.Scrollbar(self, orient=tk.HORIZONTAL)

        sbarV.config(command=canv.yview)
        sbarH.config(command=canv.xview)

        canv.config(yscrollcommand=sbarV.set)
        canv.config(xscrollcommand=sbarH.set)

        sbarV.grid(row=0, column=1, sticky='ns')
        sbarH.grid(row=1, column=0, sticky='ew')

        self.im=PIL.Image.open(image_filename)
        width,height=self.im.size
        canv.config(scrollregion=(0,0,width,height))
        self.im2=PIL.ImageTk.PhotoImage(self.im)
        self.imgtag=canv.create_image(0,0,anchor="nw",image=self.im2)

        # Add mousewheel functionality to the scrollbars
        def scroll(event):
            if event.delta > 0:
                canv.yview_scroll(-1, "units")
                sbarV.set(canv.yview()[0], canv.yview()[1])
            elif event.delta < 0:
                canv.yview_scroll(1, "units")
                sbarV.set(canv.yview()[0], canv.yview()[1])
        sbarV.bind_all("<MouseWheel>", scroll)

        def hscroll(event):
            if event.delta > 0:
                canv.xview_scroll(-1, "units")
                sbarH.set(canv.xview()[0], canv.xview()[1])
            elif event.delta < 0:
                canv.xview_scroll(1, "units")
                sbarH.set(canv.xview()[0], canv.xview()[1])
        sbarH.bind_all("<MouseWheel>", hscroll)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

#ScrolledCanvas().mainloop()
# 
# class ScrolledCanvas(tk.Toplevel):
#     def __init__(self, parent=None, image_filename=None): 
#         tk.Toplevel.__init__(self, parent)
#         self.master.title("Formelsammlung")
# 
#         canv = tk.Canvas(self, relief=tk.SUNKEN)
#         canv.config(width=1000, height=700)
#         canv.config(highlightthickness=0)
#         canv.grid(row=0, column=0, sticky='nwes')
# 
#         sbarV = tk.Scrollbar(self, orient=tk.VERTICAL)
#         sbarH = tk.Scrollbar(self, orient=tk.HORIZONTAL)
# 
#         sbarV.config(command=canv.yview)
#         sbarH.config(command=canv.xview)
# 
#         canv.config(yscrollcommand=sbarV.set)
#         canv.config(xscrollcommand=sbarH.set)
# 
#         sbarV.grid(row=0, column=1, sticky='ns')
#         sbarH.grid(row=1, column=0, sticky='ew')
# 
#         self.im=PIL.Image.open(image_filename)
#         width,height=self.im.size
#         canv.config(scrollregion=(0,0,width,height))
#         self.im2=PIL.ImageTk.PhotoImage(self.im)
#         self.imgtag=canv.create_image(0,0,anchor="nw",image=self.im2)
# 
#         self.grid_rowconfigure(0, weight=1)
#         self.grid_columnconfigure(0, weight=1)

#ScrolledCanvas().mainloop()