'''
Allgemeine Hinweise anzeigen
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
    AHtext = ' \n \
    Dieser Fragen- und Antwortenkatalog veranschaulicht Prüfungsinhalte und -anforderungen im Prüfungsteil „Technische \n \
    Kenntnisse“, die bei Prüfungen zum Erwerb von Amateurfunkzeugnissen der Klasse A gefordert werden. \n \
    \n \
    Ab dem 1. Juni 2007 werden die Prüfungen im Prüfungsteil „Technische Kenntnisse“ der Klasse A nur noch auf der \n \
    Grundlage dieses Fragenkatalogs durchgeführt. Zur Vorbereitung auf bis zum 31. Mai 2007 stattfindende Prüfungen im \n \
    Prüfungsteil „Technische Kenntnisse“ der Klasse A kann entweder dieser Fragenkatalog oder der Technikteil des bis- \n \
    herigen Fragenkatalogs „Prüfungsfragen für den Erwerb der Amateurfunkzeugnisse der Klassen 1 und 2“ verwendet \n \
    werden. Neue Prüfungsinhalte dieses Fragenkatalogs werden erst ab dem 1. Juni 2007 bei Prüfungen angewendet. \n \
    Für die Fragen TG523, TG524 und TK204 gilt dies vorbehaltlich der vorherigen Veröffentlichung entsprechender \n \
    Richtwerte gemäß § 16 Abs. 4 Satz 2 der AFuV. Die Prüfungen nach dem bisherigen Katalog für die Klassen 1 und 2 \n \
    im Prüfungsteil „Technische Kenntnisse“ der Klasse A enden zum 31. Mai 2007. \n \
    \n \
    Einzelheiten zu Prüfungsinhalten und –anforderungen und zu Zusatzprüfungen sind in Vfg Nr. 4/2007 enthalten, die im  \n \
    Amtsblatt der Bundesnetzagentur Nr. 2 vom 24. Januar 2007, S. 103 veröffentlicht ist. Im Prüfungsteil „Technische Kenntnis- \n \
    se“ der Klasse A richten sich die Prüfungsinhalte und -anforderungen im Wesentlichen nach den technikbezo- \n \
    genen Inhalten und Anforderungen der Anlage 6 der CEPT1-Empfehlung T/R 61-02. Eine deutsche Übersetzung der \n \
    CEPT-Empfehlung T/R 61-02 ist als Anlage 2 zu Vfg. Nr. 11/2005 im Amtsblatt der Regulierungsbehörde Nr. 7 vom 20. \n \
    April 2005, S. 548 veröffentlicht. \n \
    \n \
    Für den Erwerb eines Amateurfunkzeugnisses müssen die Prüfungsteile „Technische Kenntnisse“, „Betriebliche Kennt- \n \
    nisse“ und „Kenntnisse von Vorschriften“ erfolgreich abgelegt werden. Die Inhalte und Anforderungen der Prüfungsteile \n \
    für die Klassen A und E unterscheiden sich ab dem 1. Februar 2007 nur noch beim Prüfungsteil „Technische Kenntnis- \n \
    se“. Der Aufstieg von Klasse E nach Klasse A ist mit einer Zusatzprüfung möglich, die nur aus dem Prüfungsteil „Tech- \n \
    nische Kenntnisse“ der Klasse A besteht. \n \
    \n \
    Die Inhalte und Anforderungen der Prüfungsteile sind in den folgenden drei Fragen- und Antwortenkatalogen veran- \n \
    schaulicht, die mindestens 3 Monate vor ihrer Anwendung neu herausgegeben werden: \n \
    • Prüfungsfragen in den Prüfungsteilen „Betriebliche Kenntnisse“ und „Kenntnisse von Vorschriften“ bei Prüfungen \n \
      zum Erwerb von Amateurfunkzeugnissen der Klassen A und E, \n \
    • Prüfungsfragen im Prüfungsteil „Technische Kenntnisse“ bei Prüfungen zum Erwerb von Amateurfunkzeugnissen \n \
      der Klasse A, \n \
    • Prüfungsfragen im Prüfungsteil „Technische Kenntnisse“ bei Prüfungen zum Erwerb von Amateurfunkzeugnissen \n \
      der Klasse E. \n \
    Bei den Prüfungen müssen nicht ausschließlich Fragen und Antworten aus diesen Katalogen verwendet werden. Es \n \
    können auch andere Fragen und Antworten verwendet werden, die sich inhaltlich an den Fragen des betreffenden \n \
    Katalogs orientieren. Die Fragenkataloge können zwar als Hilfsmittel zur Vorbereitung auf die Amateurfunkprüfung \n \
    dienen, sie sind jedoch keine Lehrbücher und können die Vielseitigkeit der handelsüblichen Fachliteratur nicht erset- \n \
    zen. \n \
    Die richtige Antwort bei jeder Frage ist in den Katalogen immer die Antwort A. Die Antworten B, C und D sind falsche \n \
    oder teilweise falsche Antworten. In den Prüfungsbögen werden die Antworten in zufälliger Reihenfolge angeordnet. \n \
    Bei der Prüfung ist im Antwortbogen die als richtig angesehene Antwort anzukreuzen.\n \
    Für die Einzelheiten zur Durchführung von Amateurfunkprüfungen gilt die Vfg Nr. 81/2005 geändert durch die Vfg \n \
    Nr. 3/2007. Letztere ist im Amtsblatt der Bundesnetzagentur Nr. 2 vom 24. Januar 2007, S. 103 veröffentlicht. \n \
    \n \
    Bei der Prüfung wird im Prüfungsteil „Technische Kenntnisse“ eine Formelsammlung für die jeweilige Klasse zur Verfü- \n \
    gung gestellt. Die Formelsammlung entspricht der als Anhang im Technik-Fragenkatalog für die jeweilige Klasse ent- \n \
    halten Formelsammlung und kann auch erforderliche Korrekturen und Ergänzungen enthalten. Andere Formelsamm-  \n \
    lungen dürfen bei der Prüfung nicht benutzt werden. Weiterhin sind bei der Prüfung im Teil „Technische Kenntnisse“ als  \n \
    Hilfsmittel eigene nicht programmierbare Taschenrechner ohne Textspeicher zulässig. \n \
    \n \
    Die genannten Verfügungen sowie weitere Regelungen, Informationen und Antragsformblätter zum Thema Amateur-  \n \
    funk sind unter http://www.bundesnetzagentur.de/enid/Amateurfunk zu finden. \n \
    \n \
    Die in diesem Katalog enthaltenen Fragen wurden unter Mitwirkung von Amateurfunkvereinigungen und einzelnen  \n \
    Funkamateuren erstellt. Wir danken allen, die zu der Erstellung dieses Katalogs beigetragen haben. \n \
     \n \
    Bundesnetzagentur, Referat 225 \
    '
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