# quiz_score_datei_erzeugen.py
#####################################################
from pathlib import Path
import csv
import json
def csv_to_json(dateiname, savename):
    '''
    Erstellen einer Datei um die Fragenergebnisse zu speichern
    1: Öffnet die CSV-Datei mit den Quizfragen
    2: Bildet ein JSON-DICT
    die Fragennummer als KEY
    ein DICT mit 2 Werten als VALUE
    {'FrageNr':['Timestamp_Frage_OK','Timestamp_Frage_bad']}
    {'1':['20220312-123456', '20220312-134500']}
    '''
    fragen_dict = {}
    with open(dateiname, 'r') as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter=';')
        for row in csvreader:
            frage_nr = row['FrageNr']
            fragen_dict[frage_nr] = ['', '']        # Initialisiere Datum-Zeit Stempel mit leeren Strings
    with open(savename, 'w') as file:
        json.dump(fragen_dict, file)
        print(f' Durch "quiz_score_datei_erzeugen.py csv_to_json" als {savename} gespeichert')
    return fragen_dict


quizpath = Path.cwd().parent
quiz = quizpath / 'Q_quiz'
bilder = quizpath / 'Q_pics'
kataloge = quizpath / 'Q_kataloge'
filename = kataloge / '2023-02-15_1503_afu_tech_edit.csv'           # Vollständiger Katalog
savename = quizpath / quiz /'quiz_score.json'
# csv_to_json(filename, savename) # DEBUG Test