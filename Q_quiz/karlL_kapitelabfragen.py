import tkinter as tk
from tkinter import ttk
import pandas as pd
from pathlib import Path
import sqlite3

class Testfenster(tk.Tk):

    def __init__(self):
        super().__init__()
        self.geometry("500x500+100+100")
        self.quizpath = Path.cwd().parent
        self.kataloge = self.quizpath / 'Q_kataloge'
        self.db = self.kataloge / 'fragenkapitel.sqlite'
        self.cbokapitelwahllabel = ttk.Label(self, text = 'Kapitel auswählen')
        self.cbokapitelwahllabel.grid(row=0, column=0)
        self.frageVar = tk.StringVar()
        self.cbokapitelwahl = ttk.Combobox(self, textvariable=self.frageVar)
        self.cbokapitelwahl.grid(row=1, column=0)
        self.cbokapitelwahl.bind('<<ComboboxSelected>>', self.get_fragenummern_selected_kapitel)

        self.cbokapitelfragenlabel = ttk.Label(self, text = 'zum Kapitel gehörige Fragen')
        self.cbokapitelfragenlabel.grid(row=0, column=1)
        self.cbokapitelfragen = ttk.Combobox(self)
        self.cbokapitelfragen.grid(row=1, column=1)
        self.get_complete_dataframe()
        self.get_grouped_kapitelebene2()

    def get_complete_dataframe(self):
        self.conn = sqlite3.connect(self.db)
        self.df = pd.read_sql('Select * from katalog', self.conn)

    def get_grouped_kapitelebene2(self):
        self.cbokapitelwahl['values'] = self.df['KapitelEbene2'].unique().tolist()

    def get_fragenummern_selected_kapitel(self, event):
        self.cbokapitelfragen.set('')
        selectionstring = f'Select FrageNr from katalog where KapitelEbene2 == "{self.frageVar.get()}"'
        self.df = pd.read_sql(selectionstring, self.conn)
        self.cbokapitelfragen['values'] = self.df['FrageNr'].to_list()
        self.cbokapitelfragen.current(0)


test = Testfenster()
test.mainloop()
