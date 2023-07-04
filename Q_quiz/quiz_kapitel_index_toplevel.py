'''
Quizkapitel anzeigen
'''
checkboxes = []

def pfade(was):    
    from pathlib import Path
    quizpath = Path.cwd().parent
    bilder = quizpath / 'Q_pics'
    kataloge = quizpath / 'Q_kataloge'
    savename = 'quiz_fragen_score.json'
    fragenkapitelscore = kataloge / 'fragenkapitelscore.sqlite'
    if was == "fragenkapitelscore":
        pfad = fragenkapitelscore
        #print('pfad',pfad)
    return pfad

def sqlabfrage(abfrage):
    import sqlite3
    #print("33", abfrage)
    datenbank = sqlite3.connect(pfade('fragenkapitelscore'))
    datensatzeiger = datenbank.cursor()
    ausgabe = datensatzeiger.execute(abfrage)
    inhalt = ausgabe.fetchall()
    #print("38", ausgabe)
    return inhalt

def quiz_kapitel_index(mainwindow):
    import sqlite3
    import tkinter as tk
    from tkinter import ttk
    from tkinter import BOTH
    import json
  
    # Variablen // Pfade // Initialisierungen
    from pathlib import Path
    quizpath = Path.cwd().parent
    bilder = quizpath / 'Q_pics'
    kataloge = quizpath / 'Q_kataloge'
    savename = 'quiz_fragen_score.json'
    fragenkapitelscore = kataloge / 'fragenkapitelscore.sqlite'
    
    window = tk.Toplevel(mainwindow)
    window.geometry("1000x750")
    window.title("Kapitel-Index")
    row_counter = 0
    # Frame erstellen, um Checkboxen zu enthalten
    checkbox_frame = tk.Frame(window)
    checkbox_frame.pack(fill=BOTH, expand=1)

    # Canvas erstellen, um das Frame in der vertikalen Richtung zu scrollen
    canvas = tk.Canvas(checkbox_frame)
    canvas.pack(side="left", fill="both", expand=1)
    
    # Scrollbar erstellen und dem Canvas zuweisen
    scrollbar = tk.Scrollbar(checkbox_frame, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="left", fill="y")
    
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    #another frame
    second_frame = tk.Frame(canvas)
    canvas.create_window((0,0),window=second_frame, anchor="nw")
    
    #'Anlegen der Checkboxen
    generate_checkboxes(window, second_frame)
    
# Erstellen Sie ein Dictionary, um die Checkbutton-Widgets und ihre zugehörigen BooleanVar-Instanzen zu speichern
def load_checkboxes_state():            
    abfrage = "SELECT DISTINCT Ebene2Bezeichnung FROM katalog WHERE Kapitelwahl = 1"
    #print("SQLABFRAGE Alle Ebene2Bezeichnung mit Kapitelwahl=1", sqlabfrage(abfrage))
    
    with open("quiz_kapitel_auswahl.json", "r", encoding='utf8') as f:
        state = json.load(f)
        
    for checkbox, var in checkboxes.items():
        checkbox_state = state.get(checkbox["text"], False)
        var.set(checkbox_state)
        # print("load_checkboxes_state OK") #DEBUG
        

        #print("{}: {}".format(checkbox['name'], checkbox_state))
   #     print("{}: {}".format(checkbox['text'], checkbox_state))
# Weisen Sie die Funktion "on_checkbox_click" jedem Checkbutton-Widget zu
# for checkbox in checkboxes.keys():
#     checkbox.config(command=on_checkbox_click)        
    
def generate_checkboxes(window, second_frame):
    import tkinter as tk
    
    #Definieren Sie eine Funktion, die aufgerufen wird, wenn ein Checkbox-Widget geklickt wird
    def on_checkbox_click():
    #print(checkboxes)
        print("OK")
        print("PY_VAR1:",name," ",PY_VAR1.get())
        #for checkbox, var in checkboxes.items():
        checkbox_state = var.get()
        
    # Zustand
    
    #
    # Erstellen Sie 70 Checkbutton-Widgets und fügen Sie sie dem Dictionary hinzu
    # Rückgabe ist eine Liste mit Tupeln
    # SQLABFRAGE Alle Ebene2Bezeichnung [('Allgemeine mathematische Grundkenntnisse',), ('Größen und Einheiten',), 
    abfrage = "SELECT DISTINCT Ebene2Bezeichnung FROM katalog"
    
    for i, item in enumerate(sqlabfrage(abfrage)):
        name = "var" + str(i)
        name = tk.IntVar()
        nm = "cb" + str(i)
        label = nm
        # print("ITEM",item, type(item))
        item = str(item[0])
        nm = tk.Checkbutton(second_frame, text=item, variable=name, name=nm)
        nm.pack(anchor="w")
        print("NAME_Line123:", name," ",name.get())
        # Erstelle Liste
        checkboxes.append((label, name.get(),item ))
    close_button = tk.Button(second_frame, text="Speichern - Schließen", command=save_checkboxes_state) #, command=save_checkboxes_state(window)
    close_button.pack(side="bottom", padx=15, pady=15, anchor="w")
    print(checkboxes) #DEBUG
    
def save_checkboxes_state():
    checkboxstate = []
    test = cb0.get()
    print(test)
    #     state = {}
    #     for checkbox, var in checkboxes.items():
    #         state[checkbox["text]] = var.get()
    #     with open("quiz_kapitel_auswahl.json", "w", encoding='utf8') as f:
    #         json.dump(state, f)
    window.destroy()
    # print("save_checkboxes_state OK") DEBUG           
    
'''chapter_list = [
    '1.1 Allgemeine mathematische Grundkenntnisse und Größen (TA)',
    '1.1.1 Allgemeine mathematische Grundkenntnisse',
    '1.1.2 Größen und Einheiten',
    '1.2 Elektrizitäts-, Elektromagnetismus- und Funktheorie (TB)',
    '1.2.1 Leiter, Halbleiter und Isolator',
    '1.2.2 Strom- und Spannungsquellen',
    '1.2.3 Elektrisches Feld',
    '1.2.4 Magnetisches Feld',
    '1.2.5 Elektromagnetisches Feld',
    '1.2.6 Sinusförmige Signale',
    '1.2.7 Nichtsinusförmige Signale',
    '1.2.8 Modulierte Signale',
    '1.2.9 Leistung und Energie',
    '1.3 Elektrische und elektronische Bauteile (TC)',
    '1.3.1 Widerstand',
    '1.3.2 Kondensator',
    '1.3.3 Spule',
    '1.3.4 Übertrager und Transformatoren',
    '1.3.5 Diode',
    '1.3.6 Transistor',
    '1.3.7 Einfache digitale und analoge Schaltkreise und sonstige Bauelemente',
    '1.4 Elektronische Schaltungen und deren Merkmale (TD)',
    '1.4.1 Reihen- und Parallelschaltung von Widerständen, Spulen und Kondensatoren',
    '1.4.2 Schwingkreise und Filter',
    '1.4.3 Stromversorgung',
    '1.4.4 Verstärker',
    '1.4.5 Modulator / Demodulator',
    '1.4.6 Oszillator',
    '1.4.7 Phasenregelkreise',
    '1.5 Analoge und digitale Modulationsverfahren (TE)',
    '1.5.1 Amplitudenmodulation AM, SSB, CW',
    '1.5.2 Frequenzmodulation',
    '1.5.3 Text-, Daten- und Bildübertragung',
    '1.6 Funk-Empfänger (TF)',
    '1.6.1 Einfach- und Doppelsuperhet-Empfänger',
    '1.6.2 Blockschaltbilder',
    '1.6.3 Betrieb und Funktionsweise einzelner Stufen',
    '1.6.4 Empfängermerkmale',
    '1.6.5 Digitale Signalverarbeitung',
    '1.7 Funksender (TG)',
    '1.7.1 Blockschaltbilder',
    '1.7.2 Betrieb und Funktionsweise einzelner Stufen',
    '1.7.3 Betrieb und Funktionsweise von HF-Leistungsverstärkern',
    '1.7.4 Betrieb und Funktionsweise von HF-Transceivern',
    '1.7.5 Unerwünschte Aussendungen',
    '1.8 Antennen und Übertragungsleitungen (TH)',
    '1.8.1 Antennen',
    '1.8.2 Antennenmerkmale',
    '1.8.3 Übertragungsleitungen',
    '1.8.4 Anpassung, Transformation und Symmetrierung',
    '1.9 Wellenausbreitung und Ionosphäre (TI)',
    '1.9.1 Ionosphäre',
    '1.9.2 Kurzwellenausbreitung',
    '1.9.3 Wellenausbreitung oberhalb 30 MHz',
    '1.10 Messungen und Messinstrumente (TJ)',
    '1.10.1 Strom- und Spannungsmesser',
    '1.10.2 Dipmeter',
    '1.10.3 Oszilloskop',
    '1.10.4 Stehwellenmessgerät',
    '1.10.5 Frequenzzähler',
    '1.10.6 Absorptionsfrequenzmesser',
    '1.10.7 Sonstige Messgeräte und Messmittel',
    '1.10.8 Durchführung von Messungen',
    '1.11 Störemissionen, -festigkeit, Schutzanforderungen, Ursachen, Abhilfe (TK)',
    '1.11.1 Störungen elektronischer Geräte',
    '1.11.2 Ursachen für Störungen und störende Beeinflussungen',
    '1.11.3 Maßnahmen gegen Störungen und störende Beeinflussungen',
    '1.12 Elektromagnetische Verträglichkeit, Anwendung, Personen- und Sachschutz (TL)',
    '1.12.1 Störfestigkeit',
    '1.12.2 Schutz von Personen',
    '1.12.3 Sicherheit',
    ]
'''
        

    
    





    
    

    
