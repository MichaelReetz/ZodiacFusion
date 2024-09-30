# Funktion zur Berechnung des Alters
def berechne_alter(geburtsjahr, aktuelles_jahr):
    return aktuelles_jahr - geburtsjahr

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

# Aktuelles Jahr kann entweder festgelegt oder auch eingegeben werden
aktuelles_jahr = 2024  # Du kannst das aktuelle Jahr manuell anpassen

# Einfacher Output: Geburtstag und Alter anzeigen
alter = berechne_alter(jahr, aktuelles_jahr)
print(f"Du wurdest am {tag}.{monat}.{jahr} geboren.")
print(f"Du bist {alter} Jahre alt.")

# Es ist wichtig, dass das Programm erkennt, dass ein Datum im 
# richtigen Format eingegeben werden muss, und bei einer falschen Eingabe, 
# eine entsprechende Rückmeldung an den Benutzer erfolgt.