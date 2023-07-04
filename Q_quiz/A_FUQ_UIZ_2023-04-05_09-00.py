'''
# AFU Quiz
# Einlesen des Fragenkatalogs aus CSV Datei
#
# Pfade:
#       Quiz
#       Quiz/Q_quiz    (Python-Programm Code)
#       Quiz/Q_pics    (Bilder im JPG Format)
#       Quiz/Q_katalog (FragenKataloge A, N, E)
#
# LastDoing: Fenstergröße auf MAC angepasst
#            Wrapping geändert FUNKTION get_wraped_text(text, breite):
#            Skizze der Grideinteilung 5 LabelFrames, 2 x 300 B, 6 x 150 H
#            Pfade neu, Pathlib Bibliothek
#            klappt, jetzt schön machen!
# 11-03-2023 Einfaches Scoring eingebaut, Labelframe unter Auswertebutton
#            
# GRIDMODELL
#
  Col 0    Col 1
R╔═Nr.═══════════════╗
0║ Frage             ║
 ╟───────────────────╢
1║ FrageBild 1 + 2   ║
 ╠═A═══════╦═B═══════╣
2║ Antw_A  ║ Antw_B  ║
 ╟─────────╫─────────╢
3║AntwA_Pic║AntwB_Pic║
 ╠═C═══════╬═D═══════╣
4║ Antw_C  ║ Antw_D  ║
 ╟─────────╫─────────╢
5║AntwC_Pic║AntwD_Pic║
 ╚═════════╩═════════╝
 
AUSWERTUNG
todo
> Tool zu bilden des Dictionaries das speicherbar und ladbar sein muss um das lernen fortzusetzen zu können
  Dictionary mit {Fragennummer:[Antwort_bad_Datum-HHMMSS,Antwort_OK_Datum-HHMMSS]}
> Richtig Beantwortete Fragen werden definierbare Zeit nicht mehr gefragt
> Filterung der Fragen auf bestimmte Lerngebiete -> Kapitelübersicht
'''
# Python Importe
import csv
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
import textwrap
import os.path
from random import shuffle
import PIL.Image
from PIL import ImageTk
from pathlib import Path
import pyautogui

# Eigene Importe
from quiz_class import *
from quiz_allgemeine_hinweise_toplevel import quiz_allgemeine_hinweise
from quiz_kapitel_index_toplevel import quiz_kapitel_index
from quiz_formelsammlung_toplevel import ScrolledCanvas
from quiz_score_datei_erzeugen import csv_to_json
from quiz_print_debug_questions import debug_show_question
from scrollimage import ScrollableImage

# Variablen // Pfade // Initialisierungen
quizpath = Path.cwd().parent
bilder =   quizpath / 'Q_pics'
kataloge = quizpath / 'Q_kataloge'
#filename = kataloge / 'Nur_Bild_2023-02-15_1502_afu_tech_edit.json'  # Kleine Auswahl 
filename = kataloge / '2023-03-31_10-20_afu_tech_edit.json'           # Vollständiger Katalog
savename = 'quiz_fragen_score.json'
Versionsstempel = '2023-04-05 09:00\nV0.1'
# Globale Variable zur Überwachung des Scores
question_index = 0  # Fragenzähler
score_ok = 0        # Zähler richtig gelöste Fragen
score_bad = 0       # Zähler falsch gelöste Fragen
row_count = 0       # Zeilenzähler Grid
i = 0

# DEF #########################################

        
def mainwindow_show(mainwindow): # Aufruf aus def-kopfzeile_anzeigen//def-start
    mainwindow.deiconify()       # Ausgeblendetes leerees Fenster def-programmstart anzeigen withdraw()
    
def kopfzeile_anzeigen(mainwindow):
    
    def start():
        mainwindow_show(mainwindow)
        # Fragenkatalogauswahl
        quiz_questions= read_questions_from_json_file(filename)
        
        # Mische die Fragen
        shuffle(quiz_questions)
        # Zeige die erste zufällige Frage an
        show_question(question_index, quiz_questions, mainwindow)
        
    def exit():
        mainwindow.destroy() #.quit()
        
    def score_datei_resetten():
        messagebox.askokcancel('Sicherheitsabfrage', 'Wollen sie Ihre Lernerfolgedatei unwiderruflich zurücksetzen?') 
        savename = "quiz_score.json"
        dateiname = filename
        csv_to_json(dateiname, savename)     
        
    def zeige_allgemeine_hinweise_an():
        maxformat = bildschirm_groesse_auslesen()
        quiz_allgemeine_hinweise(mainwindow, maxformat)
        
    def zeige_formelsammlung_seite_1_an():
        bild = bilder / 'Formelsammlung_1-1.jpg'
        ScrolledCanvas(image_filename=bild)
       
    def zeige_formelsammlung_seite_2_an():
        bild = bilder / 'Formelsammlung_1-2.jpg'
        ScrolledCanvas(image_filename=bild)
        
    def zeige_formelsammlung_seite_3_an():
        bild = bilder / 'Formelsammlung_1-3.jpg'
        ScrolledCanvas(image_filename=bild)
        
    def zeige_formelsammlung_seite_4_an():
        bild = bilder / 'Formelsammlung_1-4.jpg'
        ScrolledCanvas(image_filename=bild)
       
    def zeige_formelsammlung_seite_5_an():
        bild = bilder / 'Formelsammlung_1-5.jpg'
        ScrolledCanvas(image_filename=bild)
        
    def zeige_formelsammlung_seite_6_an():
        bild = bilder / 'Formelsammlung_1-6.jpg'
        ScrolledCanvas(image_filename=bild)
        
    def zeige_kapitel_index_an():
        quiz_kapitel_index(mainwindow)
        
    ##GRAFIK UND ###########################################   
    # Erstellen Sie die Menüleiste und das Datei-Menü
    # |AFU-Quiz||Datei||Kapitel||Info|
    # |AFU-Quiz|
    kopfzeile = Menu(mainwindow)
    mainwindow.config(menu=kopfzeile)
    #
    programmname = Menu(kopfzeile, tearoff=0)
    kopfzeile.add_cascade(label="A_FUQ_uiz", menu=programmname)
    ## |AFU-Quiz-Zeilen
    programmname.add_command(label="Starte A_FUQ_uiz", command=start)
    programmname.add_command(label="Beende A_FUQ_uiz", command=exit)
    #
    # |Datei|
    dateimenu =  Menu(kopfzeile, tearoff=0)
    kopfzeile.add_cascade(label="Datei", menu=dateimenu)
    ## |Datei-Zeilen
    dateimenu.add_command(label="Öffnen todo", command="")
    dateimenu.add_command(label="Speichern todo", command="")
    dateimenu.add_separator()
    dateimenu.add_command(label="Reset Statistik-Datei", command=score_datei_resetten) #Statistik_Reset
    #
    # |Kapitel|
    kapitelmenu =  Menu(kopfzeile, tearoff=0)
    kopfzeile.add_cascade(label="Kapitel", menu=kapitelmenu)
    ## Kapitel-Zeilen
    kapitelmenu.add_command(label="Kapitel-Index", command=zeige_kapitel_index_an)
    #
    # |Info|
    infomenu = Menu(kopfzeile, tearoff=0)
    kopfzeile.add_cascade(label="Info", menu=infomenu)
    ## |Info-Zeilen
    infomenu.add_command(label="Allgemeine Hinweise", command=zeige_allgemeine_hinweise_an)
    infomenu.add_separator()
    infomenu.add_command(label="Formelsammlung Seite 1 ", command=zeige_formelsammlung_seite_1_an)
    infomenu.add_command(label="Formelsammlung Seite 2 ", command=zeige_formelsammlung_seite_2_an)
    infomenu.add_command(label="Formelsammlung Seite 3 ", command=zeige_formelsammlung_seite_3_an)
    infomenu.add_command(label="Formelsammlung Seite 4 ", command=zeige_formelsammlung_seite_4_an)
    infomenu.add_command(label="Formelsammlung Seite 5 ", command=zeige_formelsammlung_seite_5_an)
    infomenu.add_command(label="Formelsammlung Seite 6 ", command=zeige_formelsammlung_seite_6_an)
    infomenu.add_separator()
    infomenu.add_command(label="A_FUQ_uiz Version: " + Versionsstempel, command="")
    
# Zeigt die Frage an
def show_question(question_index, quiz_questions,  mainwindow):
    ''' quiz_questions_json = List of Dicts
    quiz_questions "null" wurde beim Import durch Leerstrings ersetzt '''
    global row_count
    row_count = 0
    #
    print("DEBUG ersetzung ", quiz_questions)       
    #quiz_questions_json = List of Dicts
    question = quiz_questions[question_index]
    #print("question_json: ", question_json)
    #FrageNr = question_json[FrageNr]
    FrageNr, Frage,  \
    Frage_Bild1, Frage_Bild1_scale,  \
    Frage_Bild2, Frage_Bild2_scale, \
    AntwortA, AntwortA_Bild, AntwortA_Bild_scale, \
    AntwortB, AntwortB_Bild, AntwortB_Bild_scale, \
    AntwortC, AntwortC_Bild, AntwortC_Bild_scale, \
    AntwortD, AntwortD_Bild, AntwortD_Bild_scal = question.values()
    print("QUESTION-JSON",question)
    #
    # debug_show_question(question) # DEBUG Ausgabe der Fragen
    #
    # shuffle_anwser() Mischt die vier Antworten/Bilder und liefert als 5ten Wert die korrekte Antwort/Bild komination
    gescrambelt = shuffle_anwser(question)
    # print(type( gescrambelt)) # DEBUG
    # print("GS:", gescrambelt) # DEBUG
    AntwortA = gescrambelt[0][0]
    AntwortA_Bild = gescrambelt[0][1]
    AntwortB = gescrambelt[1][0]
    AntwortB_Bild = gescrambelt[1][1]
    AntwortC = gescrambelt[2][0]
    AntwortC_Bild = gescrambelt[2][1]
    AntwortD = gescrambelt[3][0]
    AntwortD_Bild = gescrambelt[3][1]
    Antwort_OK = gescrambelt[4][0]
    Antwort_OK_Bild = gescrambelt[4][1]
    #DEBUG
    print("####SCRABLE####")
    print(AntwortA)
    print(AntwortA_Bild)
    print(AntwortB)
    print(AntwortB_Bild)
    print(AntwortC)
    print(AntwortC_Bild)
    print(AntwortD)
    print(AntwortD_Bild)
    print(Antwort_OK)
    print(Antwort_OK_Bild)
    print("####SCRABLE####")
    #
    # Entferne die vorherigen Fragen und Antwortmöglichkeiten
#    for widget in mainwindow.winfo_children():
#        print("window kinder ", mainwindow.winfo_children())
#        widget.destroy()
        
    kopfzeile_anzeigen(mainwindow) # Logikfehler? kopfzeile veschwindet nach dem "widget destroy"
    
    ## Erst mal alles in ein Canvas stecken
    canvas = tk.Canvas(mainwindow)
    canvas.grid(row=0, column=0, sticky="nsew")
    #
    mainwindow.grid_rowconfigure(0, weight=1)
    mainwindow.grid_columnconfigure(0, weight=1)
    mainwindow.grid_columnconfigure(1, weight=0) # ist der Scroller
    ## Fügen Sie eine Scrollbar hinzu und verknüpfen Sie sie mit dem Canvas-Widget
    scrollbar = ttk.Scrollbar(mainwindow, orient=tk.VERTICAL, command=canvas.yview)
    scrollbar.grid(row=0, column=1, sticky="ns")
    canvas.configure(yscrollcommand=scrollbar.set)
    #canvas.configure(width=600, height=700)
    # Erstellen Sie ein Frame-Widget innerhalb des Canvas-Widgets und fügen Sie alle Elemente hinzu
    inner_frame = tk.Frame(canvas)
    inner_frame.configure(width=1000, height=800)
    canvas.create_window((0, 0), window=inner_frame, anchor='nw')
    # Hier wird das Event gebunden
#    inner_frame.bind('<Configure>', on_configure)
    ## GRAFIK UND ###########################################   
    # Grundfenster 
    # LabelFrame Fragebereich
    LFFrage = LabelFrame(inner_frame, text="Frage", width=1000, height=260) # background='white',
    LFFrage.grid_propagate(False)
    LFFrage.grid(column=0, columnspan=2, row=0, sticky="wens")
    
    #
    # LabelFrame Antwort A links-oben
    LFAntwortA = LabelFrame(inner_frame, text="Option A", width=500, height=210) # background='red'
    LFAntwortA.grid_propagate(False)
    LFAntwortA.grid(column=0, columnspan=1, row=1, sticky="wens")
    #
    # LabelFrame Antwort A links-oben
    LFAntwortB = LabelFrame(inner_frame, text="Option B", width=500, height=210) # background='green',
    LFAntwortB.grid_propagate(False)
    LFAntwortB.grid(column=1, columnspan=1, row=1, sticky="wens")
    #
    # LabelFrame Antwort A links-oben
    LFAntwortC = LabelFrame(inner_frame, text="Option C", width=500, height=210) # background='blue'
    LFAntwortC.grid_propagate(False)
    LFAntwortC.grid(column=0, columnspan=1, row=2, sticky="wens")
    #
    # LabelFrame Antwort A links-oben
    LFAntwortD = LabelFrame(inner_frame, text="Option D", width=500, height=210) # background='red'
    LFAntwortD.grid_propagate(False)
    LFAntwortD.grid(column=1, columnspan=1, row=2, sticky="nsew")
    #
    # FragenText in Abschnitte unterteilen DEF  get_wraped_text(Frage, Anzahlzeichen) Rückgabe Text mit NewLine
    LFFrage.configure(text=FrageNr)
    ##wrapped_frage = get_wraped_text(Frage, 75)
    frage = tk.Label(LFFrage, text=Frage, justify=LEFT, font=("Arial", 16), wraplength=980)
    frage.bind('<Configure>', lambda e: frage.config(wraplength=frage.winfo_width()))
    frage.grid(row=0, column=0, columnspan=2, pady=10, padx=10, sticky='w')
    #
    row_count += 1
    #
    # Bild1 zur Frage
    if Frage_Bild1 != "":
        image = PIL.Image.open(bilder / Frage_Bild1)
        image = bild_scalieren(image)
        photo = ImageTk.PhotoImage(image)
        photolblF1 = tk.Label(LFFrage, image=photo)
        photolblF1.grid(row=1 + row_count, column=0, columnspan=1, pady=5, padx=5, sticky='wn')
        photolblF1.image = photo
        #
        # Bild2 zur Frage
        if Frage_Bild2 != "":
            image = PIL.Image.open(bilder / Frage_Bild2)
            image = bild_scalieren(image)
            photo = ImageTk.PhotoImage(image)
            photolblF2 = tk.Label(LFFrage, image=photo)
            photolblF2.grid(row=1 + row_count, column=1, columnspan=1, pady=5, padx=5, sticky='wn')
            photolblF2.image = photo    
        row_count += 1
        #
    # Zeige die Antwortmöglichkeiten
    option_value = tk.StringVar()  # Variable der Optionsfelder
    option_value.set(None)         # Alle Optionsfelder auf unausgewählt setzen 
    #
    # AntwortA
    AntwAges = ""
    optionA = ""
    optionA = tk.Radiobutton(LFAntwortA, text=AntwortA, variable=option_value, value="Option A", justify=LEFT, anchor="nw", wraplength=460)
    optionA.bind('<Configure>', lambda e: optionA.config(wraplength=optionA.winfo_width()))
    optionA.grid(row=0 + i + row_count, column=0, sticky="WE")
    if AntwortA_Bild != "":
        image = PIL.Image.open(bilder / AntwortA_Bild)
        image = bild_scalieren(image)
        photo = ImageTk.PhotoImage(image)
        photolblA = tk.Label(LFAntwortA, image=photo)
        photolblA.grid(row=1 + i + row_count, column=0, padx=20, pady=10)
        photolblA.image = photo
    #    
    # AntwortB
    AntwBges = ""
    optionB = ""
    optionB = tk.Radiobutton(LFAntwortB, text=AntwortB, variable=option_value, value="Option B", justify=LEFT, anchor="nw", wraplength=460)
    optionB.bind('<Configure>', lambda e: optionB.config(wraplength=optionB.winfo_width()))
    optionB.grid(row=0 + i + row_count, column=0, sticky="WE")
    if AntwortB_Bild != "":
        image = PIL.Image.open(bilder / AntwortB_Bild)
        image = bild_scalieren(image)
        photo = ImageTk.PhotoImage(image)
        photolblB = tk.Label(LFAntwortB, image=photo)
        photolblB.grid(row=1 + i + row_count, column=0, padx=20, pady=10)
        photolblB.image = photo
    #   
    # AntwortC
    AntwCges = ""
    optionC = ""
    optionC = tk.Radiobutton(LFAntwortC, text=AntwortC, variable=option_value, value="Option C", justify=LEFT, anchor="nw", wraplength=460)
    optionC.bind('<Configure>', lambda e: optionC.config(wraplength=optionC.winfo_width()))
    optionC.grid(row=0 + i + row_count, column=0, sticky="WE")
    if AntwortC_Bild != "":
        image = PIL.Image.open(bilder / AntwortC_Bild)
        image = bild_scalieren(image)
        photo = ImageTk.PhotoImage(image)
        photolblC = tk.Label(LFAntwortC, image=photo)
        photolblC.grid(row=1 + i + row_count, column=0, padx=20, pady=10)
        photolblC.image = photo
    #   
    # AntwortD
    AntwDges = ""
    optionD = ""
    optionD = tk.Radiobutton(LFAntwortD, text=AntwortD, variable=option_value, value="Option D", justify=LEFT, anchor="nw", wraplength=460)
    optionD.bind('<Configure>', lambda e: optionD.config(wraplength=optionD.winfo_width()))
    optionD.grid(row=0 + i + row_count, column=0, sticky="WE")
    if AntwortD_Bild != "" :   
        image = PIL.Image.open(bilder / AntwortD_Bild)
        image = bild_scalieren(image)
        photo = ImageTk.PhotoImage(image)
        photolblD = tk.Label(LFAntwortD, image=photo)
        photolblD.grid(row=1 + i + row_count, column=0, padx=20, pady=10)
        photolblD.image = photo
    #    
    # Zeige den Auswerten-Button im Hauptfenster unter den FrameLabels
    AuswertenButton = tk.Button(inner_frame, text="Auswerten", command=lambda: check_answer(FrageNr, question_index, quiz_questions, option_value.get(), gescrambelt, mainwindow))
    AuswertenButton.grid(row=3 + i + row_count, column=0, columnspan=2, pady=10, padx=10, sticky="WE")
    #
    # LabelFrame Anzahl Fragen
    LFScore = LabelFrame(inner_frame, text="Ergebnis", width=500, height=30)
    LFScore.grid(column=0, columnspan=1, row=4 + i + row_count, sticky="wnse")
    #
    LFScoreTxt = str(f"{question_index} von {len(quiz_questions)} Fragen bearbeitet    Falsch: {score_bad}   Richtig: {score_ok}   ")
    Score = tk.Label(LFScore, text=LFScoreTxt, justify=LEFT, font=("Arial"), fg="green")
    Score.grid(row=0, column=0, columnspan=2, pady=10, padx=10, sticky='w')
    
    # Aktualisieren Sie das Canvas-Widget, um die Größe des inneren Frame-Widgets anzupassen
    inner_frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox('all'))

def shuffle_anwser(question):
    ''' Die vier Antwort/Antwort-Bild kombinationen werden zufällig angeordnet,
    die Richtige Antwort wir als letzte Kombi in die Liste geschrieben.
    ReturnListe:[[Frage_?,Bild_?][Frage_?,Bild_?][Frage_?,Bild_?][Frage_?,Bild_?][Antwort_OK,Bild_OK]] '''
    ####JSON-DICT
    '''{'FrageNr': 'TE216', 'Frage': 'Wie wird die Empfindlichkeit eines FM-Modulators angegeben?', 'Frage_Bild1': '',
        'Frage_Bild1_scale': '', 'Frage_Bild2': '', 'Frage_Bild2_scale': '',
        'AntwortA': 'In kHz/V', 'AntwortA_Bild': '', 'AntwortA_Bild_scale': '',
        'AntwortB': 'Als Modulationsindex', 'AntwortB_Bild': '', 'AntwortB_Bild_scale': '',
        'AntwortC': 'Als Hub', 'AntwortC_Bild': '', 'AntwortC_Bild_scale': '',
        'AntwortD': 'In Rad/s', 'AntwortD_Bild': '', 'AntwortD_Bild_scale': ''}'''
    #
    print("shuffle_anwser_INPUT_quesstion", question)
    AntwortOptionsListe = []
    Antwort_OK = [question.get('AntwortA'), question.get('AntwortA_Bild')]
    #     
    AntwortOptionsListe =       [[question.get('AntwortA'), question.get('AntwortA_Bild')],
                                [question.get('AntwortB'), question.get('AntwortB_Bild')],
                                [question.get('AntwortC'), question.get('AntwortC_Bild')],
                                [question.get('AntwortD'), question.get('AntwortD_Bild')],]
    shuffle(AntwortOptionsListe)
    AntwortOptionsListe.append(Antwort_OK)
    print("ANTWORT-OPTIONS-LISTE: ", AntwortOptionsListe)
    return AntwortOptionsListe 
    
def check_answer(FrageNr, question_index, quiz_questions, selected_answer, gescrambelt, mainwindow):
    ''' Prüfen ob die Antwort OK ist -> RICHTIG
    Hinweis auf die richtige Antwort (Option A-D) wenn falsch gewählt wurde
    TO DO Anzeige der Fragenanzahl, gelöste Fragen etc TO DO '''
    global score_ok
    global score_bad
    #RICHTIG
    richtig = ""
    #
    options = ["Option A", "Option B", "Option C", "Option D"]
    for i in range(4):
        if gescrambelt[4] == gescrambelt[i]:
            richtig = options[i]
            break
    #
    # Check if the selected answer is correct or not
    question = quiz_questions[question_index]
    #
    # Überprüft, ob keine Antwort ausgewählt wurde
    print(f"selected_answer: {selected_answer} selected_answer_type: {type(selected_answer)}") # DEBUG
    #
    if selected_answer == 'None':
        messagebox.showerror("BÄHHH", "Bitte wählen Sie eine Antwort aus.")
        return
    #
    # Überprüft, ob die ausgewählte Antwort richtig ist
    if selected_answer == richtig:
        if selected_answer == richtig:
            messagebox.showinfo('Evaluation_', 'Richtig')  # Wenn die Antwort richtig ist, wird eine "Richtig"-Meldung angezeigt
            score_ok += 1                                  # und der Score wird um 1 erhöht
            score(FrageNr, True)                           # Ergebnisse (Zeitstempel) werden in der json-Datei zu Frage gespeichert
    # Überprüft, ob die ausgewählte Antwort falsch ist       
    else:
        if selected_answer != richtig:                     # FALSCH!
            messagebox.showerror("Evaluation", f"Falsch!\nRichtig ist:\n\n{richtig}")  # Wenn die Antwort falsch ist, wird eine "Falsch"-Meldung angezeigt
            score_bad += 1
            score(FrageNr, False)
    #       
    question_index = question_index + 1
    show_question(question_index, quiz_questions, mainwindow)
    #
    # Überprüft, ob es die letzte Frage ist
    if question_index == len(quiz_questions) - 1:
        messagebox.showinfo("Ergebnis", f"Geschafft!\nRichtige Antworten: {score_ok} von {len(quiz_questions)}")
        exit()
    else:
        # shuffle(quiz_questions)
        show_question(question_index, quiz_questions, mainwindow)
        

def bild_scalieren(image):
    ''' Bilder die größer als 300 Pixel Breite sind, werden scalliert und mit dem LANCZOS Algo geglättet '''
    if image.height > 180:
        scale_factor = 150 / image.height
        #Image.resize(size, resample=None, box=None, reducing_gap=None)
        wi =  int(image.width * scale_factor)
        hi =  int(image.height * scale_factor)
        print("wi ",wi)
        print("hi ",hi)
        image = image.resize((wi, hi), resample=PIL.Image.LANCZOS)
        #image = Image.resize((int(image.width * scale_factor), int(image.height * scale_factor)), resample=LANCZOS)
    return image

def get_wraped_text(text, anz_zeichen):
    ''' Fragen-text wird nach x Zeichen umgebrochen (einfügen von newline).
    Der Text wird an Leerzeichen Umgebrochen ohne Worte zu killen.'''
    return textwrap.fill(text, width=anz_zeichen)

def on_configure(event):
    # Aktionen ausführen, wenn das Fenster verändert wurde
    print("Window resized to", event.width, "x", event.height)        
        
def bildschirm_groesse_auslesen():
    width, height = pyautogui.size()
    #width, height = pyautogui.size(monitor=2)
    dimension = "{}x{}".format(width, height)
    return dimension
        
def programmstart():
    mainwindow = tk.Tk()
    print("Bildschirmgröße", bildschirm_groesse_auslesen())
    
    mainwindow.geometry("1050x800") #"600x640" , bildschirm_groesse_auslesen()
    #mainwindow.columnconfigure(0, minsize=630, weight=1, uniform="group1")
    #mainwindow.columnconfigure(0, minsize=300, weight=1, uniform="group1")
    #mainwindow.columnconfigure(1, minsize=300, weight=1, uniform="group1")
    mainwindow.title('Amateurfunkprüfungsfragen Klasse: A')
    #
    # Betriebssystem und bildschirm_grösse_auslesen() als Info zu Layout Fenster individuelles
    import sys
    if sys.platform.startswith('win'):
        print('Betriebssystem:    Windows')
    elif sys.platform.startswith('darwin'):
        print('Betriebssystem:    Mac OS X')
        mainwindow.withdraw() # Mainwindow ausblenden bis |AFU-Quiz|Starte AFU-Quiz
    elif sys.platform.startswith('linux'):
        print('Betriebssystem:    Linux')
    else:
        print('Unknown operating system')
      
    #mainwindow.iconbitmap("myico.ico")
    kopfzeile_anzeigen(mainwindow) # Python |AFU-Quiz||Datei||Kapitel||Über|
    #
    mainwindow.mainloop()
    
programmstart()




    