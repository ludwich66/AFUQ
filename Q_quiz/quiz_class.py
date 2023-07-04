# Teil von AFU-Test
# Dateiname: quiz_class.py
# 2023-03-18_12-00
# Ausgelagerte Funktionen zum AFU Quiz
# IMPORTE
import csv
import json
import tkinter as tki
from tkinter import filedialog
from tkinter import messagebox
from pathlib import Path
import PIL.Image
from PIL import ImageTk


# Liest die Fragen aus der Datei
def read_questions_from_csv_file(filename):
    '''
    Einlesen der Quizfragen aus einer CSV Datei
    Prüfen ob die Datei vorhanden ist sonst Anzeige eines Datei-Öffnungsdialogs
    '''
    quiz_questions = []
    try:
        with open(filename, 'r', encoding='utf8') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            for row in reader:
                quiz_questions.append(row)

    except FileNotFoundError:
        messagebox.showerror("Fehler", f"Die angegebene Datei {filename} konnte nicht gefunden werden.")
        exit()
    
    return quiz_questions

##########
# Liest die Fragen aus der Datei
import json

def read_questions_from_json_file(filename):
    '''
    Einlesen der Quizfragen aus einer JSON-Datei
    Prüfen ob die Datei vorhanden ist sonst Anzeige eines Datei-Öffnungsdialogs
    LIST of DICT
    '''
    quiz_questions = []
    try:
        with open(filename, 'r', encoding='utf8') as jsonfile:
            quiz_questions = json.load(jsonfile)
    except FileNotFoundError:
        messagebox.showerror("Fehler", f"Die angegebene Datei {filename} konnte nicht gefunden werden.")
        exit()
    # Ersetze die "null" Werte durch Leere Strings    
    for d in quiz_questions:
        for k, v in d.items():
            if v == "null":
                d[k] = ""

    return quiz_questions



#####################################################
'''
Die Funktion öffnet die Datei 'quiz_score.json' und versucht, sie als JSON-Objekt zu laden.
Falls die Datei nicht gefunden wird, wird ein leeres Dictionary erstellt. Anschließend wird das
Dictionary um die neue Antwort erweitert oder aktualisiert und die Datei wird mit dem aktualisierten
Dictionary überschrieben. Zur Verwendung der Funktion rufen Sie einfach score auf und übergeben die
Fragennummer als ersten Parameter und True (für eine richtige Antwort) oder False (für eine falsche
Antwort) als zweiten Parameter. Beispiel:

score('FR001', True)  # Richtige Antwort zur Frage FR001 hinzufügen
score('FR002', False)  # Falsche Antwort zur Frage FR002 hinzufügen
'''
import json
from datetime import datetime

def score(FrageNr, RichtigOderFalsch):
    # Datumsstempel bilden
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    
    # json-Datei öffnen oder erstellen
    try:
        with open('quiz_score.json', 'r') as file:
            score_dict = json.load(file)
    except FileNotFoundError:
        score_dict = {}
    
    # Richtige oder falsche Antwort hinzufügen
    if FrageNr in score_dict:
        if RichtigOderFalsch:
            score_dict[FrageNr][0] = [timestamp]
            if score_dict[FrageNr][1]:
                score_dict[FrageNr][1] = [score_dict[FrageNr][1][-1]]
        else:
            score_dict[FrageNr][1] = [timestamp]
            if score_dict[FrageNr][0]:
                score_dict[FrageNr][0] = [score_dict[FrageNr][0][-1]]
    else:
        if RichtigOderFalsch:
            score_dict[FrageNr] = [[timestamp], []]
        else:
            score_dict[FrageNr] = [[], [timestamp]]
    
    # json-Datei aktualisieren
    with open('quiz_score.json', 'w') as file:
        json.dump(score_dict, file)



#TEST
#score("TF305", True)
        
        
#####################################################
def csv_to_dict(dateiname):
    fragen_dict = {}
    with open(dateiname, 'r') as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter=';')
        for row in csvreader:
            frage_nr = row['FrageNr']
            fragen_dict[frage_nr] = ['', '']  # Initialisiere Datum-Zeit Stempel mit leeren Strings
    return fragen_dict

#####################################################
def speichern_dict(dict_obj, dateiname):
    with open(dateiname, 'w') as f:
        json.dump(dict_obj, f)
        
#####################################################
def laden_dict(dateiname):
    with open(dateiname, 'r') as f:
        dict_obj = json.load(f)
    return dict_obj

#####################################################
#####################################################

# Testprogramm Basisdaten DICT aus CSV anlegen

quizpath = Path.cwd().parent
bilder = quizpath / 'Q_pics'
kataloge = quizpath / 'Q_kataloge'
filename = kataloge / '2023-02-15_1503_afu_tech_edit.csv'           # Vollständiger Katalog
savename = 'quiz_fragen_score.json'


#fragen_dict = csv_to_json(filename, savename)
# print(fragen_dict) # DEBUG


###
class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.question_index = 0
        self.score_ok = 0
        self.score_bad = 0
    
    def get_current_question(self):
        return self.questions[self.question_index]
    
    def get_current_score(self):
        return self.score_ok, self.score_bad
    
    def check_answer(self, answer):
        question = self.get_current_question()
        if question.is_correct_answer(answer):
            self.score_ok += 1
            return True
        else:
            self.score_bad += 1
            return False
    
    def next_question(self):
        self.question_index += 1
    
    def is_last_question(self):
        return self.question_index == len(self.questions) - 1
########################################
import csv
import json

def convert_csv_to_json(csv_file, json_file):
    '''Aufruf
    convert_csv_to_json('../Q_kataloge/quiz_questions.csv', '../Q_kataloge/quiz_questions.json')
    '''
    # Öffne die CSV-Datei im Lesemodus
    with open(csv_file, 'r', encoding='utf-8') as file:
        # Lese die CSV-Daten und speichere sie in einem Dictionary
        reader = csv.DictReader(file, delimiter=';')
        data = [row for row in reader]

    # Öffne die JSON-Datei im Schreibmodus
    with open(json_file, 'w', encoding='utf-8') as file:
        # Schreibe die Daten als JSON in die Datei
        json.dump(data, file, ensure_ascii=False, indent=4)
        print("convert_csv_to_json OK")

#convert_csv_to_json('../Q_kataloge/2023-02-15_1503_afu_tech_edit.csv', '../Q_kataloge/2023-02-15_1503_afu_tech_edit.json')
#convert_csv_to_json('../Q_kataloge/Nur_Bild_2023-02-15_1502_afu_tech_edit.csv', '../Q_kataloge/Nur_Bild_2023-02-15_1502_afu_tech_edit.json')

######################
'''
Muster
'''
def quiz_allgemeine_hinweise(mainwindow, maxformat):
    import tkinter as tk
    from tkinter import scrolledtext
    # Erstellen des Fensters
    window = tk.Toplevel(mainwindow)
    print("Bildschirmformat :", maxformat) # DEBUG
    window.geometry("1000x750")
    window.title("Allgemeine Informationen und Hinweise")
    # Text
    AHtext = 'Woll'
    #
    # Erstellen der Grid-Manager-Zellen
    window.columnconfigure(0, weight=1)
    window.rowconfigure(0, weight=1)
    window.rowconfigure(1, weight=0)
    #
    # Erstellen der Textbox mit vertikalem Scrollbalken
    textbox = scrolledtext.ScrolledText(window, wrap=tk.WORD, ) #font=("Arial", 12))
    textbox.insert(tk.END, AHtext)
    textbox.grid(row=0, column=0, sticky="NSEW")
    #
    # Erstellen des Schliessen-Buttons unterhalb des Textes
    close_button = tk.Button(window, text="Schliessen", command=window.destroy)
    close_button.grid(row=1, column=0, pady=10)
    #
    # Starten der Haupt-Event-Schleife
    window.mainloop()

def bild_scalieren(image):
    ''' Bilder die größer als 300 Pixel Breite sind, werden scalliert und mit dem LANCZOS Algo geglättet
        test für .place'''
    if image.height > 180:
        scale_factor = 140 / image.height
        #Image.resize(size, resample=None, box=None, reducing_gap=None)
        wi =  int(image.width * scale_factor)
        hi =  int(image.height * scale_factor)
        print("wi ",wi)
        print("hi ",hi)
        image = image.resize((wi, hi), resample=PIL.Image.LANCZOS)
        #image = Image.resize((int(image.width * scale_factor), int(image.height * scale_factor)), resample=LANCZOS)
    return image