import sqlite3

def sqlabfrage(abfrage):
    datenbank = sqlite3.connect('/Users/juergenfrey/Downloads/Quiz_Sammlung/2023-04-05_A_FUQ_uiz/Q_kataloge/fragenkapitelscore.sqlite')
    datensatzeiger = datenbank.cursor()
    ausgabe = datensatzeiger.execute(abfrage)
    inhalt = ausgabe.fetchall()
    return inhalt

def load_checkboxes_state():
    '''Liefert eine liste mit tupeln aller Fregen  '''
    abfrage = 'SELECT "index", Kapitelwahl FROM katalog'    #'SELECT * FROM katalog WHERE Kapitelwahl = 1'
    print("SQLABFRAGE_[(index, Kapitelwahl), ...]", sqlabfrage(abfrage))

def make_checkboxes():
    for i, item in enumerate(chapter_list):
        var = tk.BooleanVar()
        name = "cb" + str(i)
        checkbox = tk.Checkbutton(second_frame, text=item, variable=var, name=name) #"Checkbutton {}".format(i)
        checkbox.pack(anchor="w")
        checkboxes[checkbox] = var
        
        
load_checkboxes_state()