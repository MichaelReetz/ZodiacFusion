# Funktion zur Berechnung des Alters
def berechne_alter(geburtsjahr, aktuelles_jahr):
    return aktuelles_jahr - geburtsjahr

# Eingabe des vollständigen Geburtstags 
geburtsdatum = input("Gib dein Geburtsdatum ein (TT.MM.JJJJ): ")

# Aufteilen des Datums in Tag, Monat und Jahr
tag, monat, jahr = map(int, geburtsdatum.split('.'))

# Aktuelles Jahr kann entweder festgelegt oder auch eingegeben werden
aktuelles_jahr = 2024  # Du kannst das aktuelle Jahr manuell anpassen

# Einfacher Output: Geburtstag und Alter anzeigen
alter = berechne_alter(jahr, aktuelles_jahr)
print(f"Du wurdest am {tag}.{monat}.{jahr} geboren.")
print(f"Du bist {alter} Jahre alt.")

#Das war meine erste Idee, etwas in Python zu schreiben.
#Aber mir kamen direkt weitere Ideen und so wurde es zu einem Projekt.