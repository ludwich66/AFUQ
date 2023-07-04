import tkinter as tk
import PIL.Image
from PIL import ImageTk
from pathlib import Path
from quiz_class import *

# Variablen // Pfade // Initialisierungen
quizpath = Path.cwd().parent
bilder =   quizpath / 'Q_pics'
kataloge = quizpath / 'Q_kataloge'
#filename = kataloge / 'Nur_Bild_2023-02-15_1502_afu_tech_edit.json'  # Kleine Auswahl 
filename = kataloge / '2023-03-31_10-20_afu_tech_edit.json'           # Vollständiger Katalog
savename = 'quiz_fragen_score.json'
Versionsstempel = '2023-04-03 09:00\nV0.1'
# Hauptfenster
mainwindow = tk.Tk()
mainwindow.geometry("960x700")
# 1024x768 4:3
# 1280x920 4:3
# 1920 x 1440x1080
mainwindow.title('Amateurfunkprüfungsfragen Klasse: A')

# Fragebereich
##Frage_frame = tk.Frame(mainwindow, width=1000, height=240, bd=2, relief="groove")
##Frage_frame.place(x=10, y=10)

LFFrage = tk.LabelFrame(mainwindow, text="Frage", width=945, height=190)
LFFrage.place(x=5, y=5)

# Antwortbereiche
#Antwort_frame_LO = tk.Frame(mainwindow, width=490, height=240, bd=2, relief="groove")
#Antwort_frame_LO.place(x=10, y=260)

LFAntwortA = tk.LabelFrame(mainwindow, text="Option A", width=470, height=190)
LFAntwortA.place(x=5, y=200)

#Antwort_frame_RO = tk.Frame(mainwindow, width=490, height=240, bd=2, relief="groove")
#Antwort_frame_RO.place(x=524, y=260)

LFAntwortB = tk.LabelFrame(mainwindow, text="Option B", width=470, height=190)
LFAntwortB.place(x=480, y=200)

#Antwort_frame_LU = tk.Frame(mainwindow, width=490, height=240, bd=2, relief="groove")
#Antwort_frame_LU.place(x=10, y=510)

LFAntwortC = tk.LabelFrame(mainwindow, text="Option C", width=470, height=190)
LFAntwortC.place(x=5, y=400)

#Antwort_frame_RU = tk.Frame(mainwindow, width=490, height=240, bd=2, relief="groove")
#Antwort_frame_RU.place(x=524, y=510)

LFAntwortD = tk.LabelFrame(mainwindow, text="Option D", width=470, height=190)
LFAntwortD.place(x=480, y=400)

# Auswerten-Button
AuswertenButton = tk.Button(mainwindow, text="Auswerten", command=lambda: check_answer(FrageNr, question_index, quiz_questions, option_value.get(), gescrambelt, mainwindow))
AuswertenButton.place(x=5, y=605, width=945, height=40)

########################
# Frage Label
Frage = 'Lorem ipsum dolor sit amet, consectetur adipisici elit, sed eiusmod tempor incidunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquid ex ea commodi consequat. Quis aute iure reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint obcaecat cupiditat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
frage = tk.Label(mainwindow, text=Frage, justify=tk.LEFT, font=("Arial", 12), wraplength=930)
frage.place(x=25, y=25)

# Option A Label
TOptionA = 'ALorem ipsum dolor sit amet, consectetur adipisici elit, sed eiusmod tempor incidunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquid ex ea commodi consequat. Quis aute iure reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur'
OptionA = tk.Radiobutton(mainwindow, text=TOptionA, justify=tk.LEFT, font=("Arial", 12), wraplength=440)
OptionA.place(x=10, y=220, anchor='nw')
#
AntwortA_Bild = 'tc525_a.jpg'
if AntwortA_Bild != "":
        image = PIL.Image.open(bilder / AntwortA_Bild)
        image = bild_scalieren(image)
        photo = ImageTk.PhotoImage(image)
        photolblA = tk.Label(mainwindow, image=photo)
        photolblA.place(x=34, y=240, anchor='nw')
        photolblA.image = photo

# Option B Label
TOptionB = 'BLorem ipsum dolor sit amet, consectetur adipisici elit, sed eiusmod tempor incidunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquid ex ea commodi consequat. Quis aute iure reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint obcaecat cupiditat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
OptionB = tk.Radiobutton(mainwindow, text=TOptionB, justify=tk.LEFT, font=("Arial", 12), wraplength=440)
OptionB.place(x=485, y=220, anchor='nw')

# Option C Label
TOptionC = 'CLorem ipsum dolor sit amet, consectetur adipisici elit, sed eiusmod tempor incidunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquid ex ea commodi consequat. '
OptionC = tk.Radiobutton(mainwindow, text=TOptionC, justify=tk.LEFT, font=("Arial", 12),  wraplength=440)
OptionC.place(x=10, y=420, anchor='nw')

# Option D Label
TOptionD = 'DLorem ipsum dolor sit amet, consectetur adipisici elit, sed eiusmod tempor incidunt ut labore et dolore magna aliqua. '
OptionD = tk.Radiobutton(mainwindow, text=TOptionD, justify=tk.LEFT, font=("Arial", 12), wraplength=440)
OptionD.place(x=485, y=420, anchor='nw')

mainwindow.mainloop()  #

