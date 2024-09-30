import datetime

# Statt einer festgelegten Jahreszahl 
# wird nun das aktuelle Datum verwendet, 
# um sicherzustellen, dass das Alter 
# dynamisch und korrekt berechnet wird.

# Funktion zur Berechnung des Alters
def berechne_alter(tag, monat, jahr):
    heute = datetime.date.today()
    geburtsdatum = datetime.date(jahr, monat, tag)
    alter = heute.year - geburtsdatum.year
    # Wenn der Geburtstag noch nicht in diesem Jahr war, 
    # wird das Alter um 1 veringert
    if heute.month < geburtsdatum.month or (heute.month == geburtsdatum.month and heute.day < geburtsdatum.day):
        alter -= 1
    return alter


# Eingabe des Geburtstags vom Benutzer mit Validierung
tag = ""
while not tag.isdigit() or not 1 <= int(tag) <= 31:
    tag = input("Gib deinen Geburtstag ein (Tag): ")
    if not tag.isdigit():
        print("Ungültiger Tag. Bitte gib eine Zahl ein.")
    elif not 1 <= int(tag) <= 31:
        print("Ungültiger Tag. Bitte gib eine Zahl zwischen 1 und 31 ein.")

tag = int(tag)

monat = ""
while not monat.isdigit() or not 1 <= int(monat) <= 12:
    monat = input("Gib deinen Geburtsmonat ein (Monat): ")
    if not monat.isdigit():
        print("Ungültiger Monat. Bitte gib eine Zahl ein.")
    elif not 1 <= int(monat) <= 12:
        print("Ungültiger Monat. Bitte gib eine Zahl zwischen 1 und 12 ein.")

monat = int(monat)

jahr = ""
while not jahr.isdigit():
    jahr = input("Gib dein Geburtsjahr ein (Jahr): ")
    if not jahr.isdigit():
        print("Ungültige Eingabe. Bitte gib eine Zahl ein.")

jahr = int(jahr)



# Einfacher Output: Geburtstag und Alter anzeigen
alter = berechne_alter(tag, monat, jahr)
print(f"Du wurdest am {tag}.{monat}.{jahr} geboren.")
print(f"Du bist {alter} Jahre alt.")

