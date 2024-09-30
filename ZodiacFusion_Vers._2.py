# Funktion zur Berechnung des Alters
def berechne_alter(geburtsjahr, aktuelles_jahr):
    return aktuelles_jahr - geburtsjahr

tag = int(input("Gib deinen Geburtstag ein (Tag): "))
monat = int(input("Gib deinen Geburtsmonat ein (Monat): "))
jahr = int(input("Gib dein Geburtsjahr ein (Jahr): "))
# Aktuelles Jahr kann entweder festgelegt oder auch eingegeben werden
aktuelles_jahr = 2024  # Du kannst das aktuelle Jahr manuell anpassen

alter = berechne_alter(jahr, aktuelles_jahr)
print(f"Du wurdest am {tag}.{monat}.{jahr} geboren.")
print(f"Du bist {alter} Jahre alt.")

#Ich wollte eine einzelne Eingabe haben, die direkt als int verarbeitet wird.
#Es ist alles sehr einfach gehalten, aber als kleine Übungsaufgabe perfekt