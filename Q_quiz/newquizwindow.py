import tkinter as tk
from tkinter import ttk
from pathlib import Path

class Quiz(tk.Tk):

    def __init__(self):
        super().__init__()
        self.quizpath = Path.cwd()
        self.bilder = self.quizpath / 'Q_pics'
        self.title("Quiz")
        self.bildschirmbreite = str(self.winfo_screenwidth())
        self.bildschirmhoehe = str(self.winfo_screenheight())
        self.geometry(f'{self.bildschirmbreite}x{self.bildschirmhoehe}')
        self.config(background='grey')
        [self.rowconfigure(i, weight=1) for i in range(5)]
        [self.columnconfigure(i, weight=1) for i in range(3)]


    def main(self):
        self.erzeuge_frageLabel()
        self.erzeuge_bildfrage1Labels()
        self.erzeuge_radioButtons()
        self.erzeuge_Buttons()


    def erzeuge_frageLabel(self):
        self.frageLabel = ttk.Label(self, text='frageLabel', background='white')
        self.frageLabel.grid(row=0, column=0, columnspan=2, sticky='news', padx=20, pady=20)

    def erzeuge_bildfrage1Labels(self):
        self.bildfrageLabel_1 = ttk.Label(self, background='white', text= 'bildfrageLabel_1')
        self.bildfrageLabel_1.grid(row=1, column=0, sticky='news', padx=20)
        self.bildfrageLabel_2 = ttk.Label(self, background='white', text='bildfrageLabel_2')
        self.bildfrageLabel_2.grid(row=1, column=1, sticky='news', padx=20)

    def erzeuge_radioButtons(self):
        # frames für die radiobuttons anlegen
        self.optA = tk.Radiobutton(self,  background='white', text='AntwortA', value="a")
        self.optA.grid(row=2, column=0, sticky="nw", padx=20, pady=20)
        self.optB = tk.Radiobutton(self,  background='white', text='AntwortB', value="a")
        self.optB.grid(row=2, column=1, sticky="nw", padx=20, pady=20)
        self.optC = tk.Radiobutton(self,  background='white', text='AntwortC', value="a")
        self.optC.grid(row=3, column=0, sticky="nw", padx=20, pady=20)
        self.optD = tk.Radiobutton(self,  background='white', text='AntwortD', value="a")
        self.optD.grid(row=3, column=1, sticky="nw", padx=20, pady=20)
        self.optD.grid_propagate(False)

    def erzeuge_Buttons(self):
        self.check_antwort = ttk.Button(self, text="Lore ipsum einziehen")
        self.check_antwort.grid(row=4, column=1, sticky='news')
        self.check_antwort.config(command=self.zeigeloreipsum)

    def zeigeloreipsum(self):
        self.frageLabel.config(text=self.getlore(), justify='left')
        self.bildfrageLabel_1.config(text= self.getlore())
        self.bildfrageLabel_2.config(text= self.getlore())
        self.optA.config(text=self.getlore())
        self.optB.config(text=self.getlore())
        self.optC.config(text=self.getlore())
        self.optD.config(text=self.getlore())

    def getlore(self):

        return '''Lorem ipsum dolor sit amet, consetetur sadipscing elitr, 
                sed diam nonumy eirmod tempor invidunt ut labore et dolore magna 
                aliquyam erat, sed diam voluptua. At vero eos et accusam et justo 
                duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata 
                sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, 
                consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt 
                ut labore et dolore magna aliquyam erat, sed diam voluptua. 
                At vero eos et accusam et justo duo dolores et ea rebum. 
                Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum 
                dolor sit amet.'''

q = Quiz()
q.main()
q.mainloop()