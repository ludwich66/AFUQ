# ABFRAGE: zeiger.execute(SQL-Anweisung)
# CREATE: CREATE TABLE datenbank (vorname VARCHAR(20), nachname VARCHAR(30), geburtstag DATE)")
# legt die Daten nicht an wenn bereits vorhynde: CREATE TABLE IF NOT EXISTS datenbank (vorname VARCHAR(20), nachname VARCHAR(30), geburtstag DATE)")
# AUSFÜHREN: datenbank.commit()
# SCHLIESSEN: datenbank.close()
# ORDER BY 
# DESK absteigend
# ALLE DATEN HOLEN: datensatzeiger.execute("SELECT * FROM personen")
#    inhalt = datensatzeiger.fetchall()
#
# INSERT INTO tabellennamen
# Datentypen in SQLite: INTEGER, REAL, TEXT, BLOB und NULL
# Python Importe
import csv
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
import textwrap

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
import os.path
quizpath = Path.cwd().parent
bilder = quizpath / 'Q_pics'
kataloge = quizpath / 'Q_kataloge'
savename = 'quiz_fragen_score.json'
fragenkapitelscore = kataloge / 'fragenkapitelscore.sqlite'
#Rubrik
#FrageNr

# Datum schreiben
def write_current_time_to_db():
    # Erstelle eine Verbindung zur Datenbank
    conn = sqlite3.connect(fragenkapitelscore)
    c = conn.cursor()

    # Erstelle den Zeitstempel im gewünschten Format
    current_time = datetime.now().strftime('%Y.%m.%d_%H:%M')

    # Schreibe den Zeitstempel in die Datenbank
    c.execute(f"UPDATE katalog SET Antwort_OK = '{current_time}' WHERE FrageNr = 'TA102'")

    # Speichere die Änderungen und schließe die Verbindung
    conn.commit()
    conn.close()
    
# datum einlesen und in     
from datetime import datetime

def convert_date_string(date_strings):
    date_objs = []
    date_format = '%Y.%m.%d_%H:%M'
    for date_string in date_strings:
        date_obj = datetime.strptime(date_string[0], date_format)
        date_objs.append(date_obj)
    return date_objs


import sqlite3
datenbank = sqlite3.connect(fragenkapitelscore)
datensatzeiger = datenbank.cursor()

# Ausgabe alle selektierten Fragen, eingeschränkt auf Kapitelauswahl
ausgabe = datensatzeiger.execute("SELECT FrageNr FROM katalog WHERE Kapitelwahl = 1")
#ausgabe = datensatzeiger.execute("SELECT * FROM katalog WHERE FrageNr = 'TA' AND Kapitelwahl = 1")
inhalt = ausgabe.fetchall()
print(inhalt)

# Ausgabe alle selektierten Fragen, eingeschränkt auf Kapitelauswahl
# UPDATE personen SET vorname='Johann Christoph Friedrich' WHERE nachname='Schiller'
##datensatzeiger.execute("UPDATE katalog SET Antwort_OK = '' WHERE FrageNr = 'TA102'")
#ausgabe = datensatzeiger.execute("SELECT * FROM katalog WHERE FrageNr = 'TA' AND Kapitelwahl = 1")
#datensatzeiger.commit()
#print(inhalt)
write_current_time_to_db()

print("Inhalt")

ausgabe = datensatzeiger.execute("SELECT Antwort_OK FROM katalog WHERE FrageNr = 'TA102'")
inhalt = ausgabe.fetchall()
print(inhalt)
inhalt2 = convert_date_string(inhalt)
print(inhalt2)

#SELECT DISTINCT Ebene1Bezeichnung, Ebene2Bezeichnung FROM <table_name>;
print("\nINHALT:")
ausgabe = datensatzeiger.execute("SELECT DISTINCT Ebene1Bezeichnung, Ebene2Bezeichnung FROM katalog")
#ausgabe = datensatzeiger.execute("SELECT * FROM katalog WHERE FrageNr = 'TA' AND Kapitelwahl = 1")
inhalt = ausgabe.fetchall()
for z, i in enumerate(inhalt):
    print(inhalt[z])


from datetime import datetime



