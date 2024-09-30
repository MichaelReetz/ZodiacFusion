import datetime

'''Das Programm validiert jetzt jede Eingabe (Tag, Monat, Jahr) einzeln und gibt im Falle
eines Fehlers eine genaue spezifische Rückmeldung, sodass der Benutzer nur den fehlerhaften 
Teil erneut eingeben muss. Zusätzlich wird jetzt das Datum als Ganzes geprüft
(z.B. um ungültige Daten wie den 30. Februar zu verhindern).'''

class Person:
    def __init__(self, tag, monat, jahr):
        self.tag = tag
        self.monat = monat
        self.jahr = jahr
        self.geburtsdatum = datetime.date(jahr, monat, tag)
        self.heute = datetime.date.today()
    
    def berechne_alter(self):
        """Berechnet das Alter basierend auf dem Geburtsdatum."""
        alter = self.heute.year - self.geburtsdatum.year
        if (self.heute.month, self.heute.day) < (self.geburtsdatum.month, self.geburtsdatum.day):
            alter -= 1
        return alter
    
    def berechne_wochentag(self):
        """Berechnet den Wochentag der Geburt."""
        wochentag = self.geburtsdatum.weekday()
        wochentag_der_geburt = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]
        return wochentag_der_geburt[wochentag]
    
    def berechne_naechster_geburtstag(self):
        """Berechnet das Datum und den Wochentag des nächsten Geburtstags."""
        try:
            naechster_geburtstag = self.geburtsdatum.replace(year=self.heute.year)
        except ValueError:
            # Für den 29. Februar in Nicht-Schaltjahren
            naechster_geburtstag = self.geburtsdatum.replace(year=self.heute.year, day=28)
        
        if self.heute > naechster_geburtstag:
            try:
                naechster_geburtstag = naechster_geburtstag.replace(year=self.heute.year + 1)
            except ValueError:
                naechster_geburtstag = naechster_geburtstag.replace(year=self.heute.year + 1, day=28)
        
        wochentag_naechster_geburtstag = naechster_geburtstag.weekday()
        wochentag_der_geburt = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]
        
        return naechster_geburtstag, wochentag_der_geburt[wochentag_naechster_geburtstag]
    
    def berechne_westliches_sternzeichen(self):
        """Berechnet das westliche Sternzeichen basierend auf dem Geburtsdatum."""
        if (self.monat == 3 and self.tag >= 21) or (self.monat == 4 and self.tag <= 20):
            return "Widder"
        elif (self.monat == 4 and self.tag >= 21) or (self.monat == 5 and self.tag <= 20):
            return "Stier"
        elif (self.monat == 5 and self.tag >= 21) or (self.monat == 6 and self.tag <= 21):
            return "Zwillinge"
        elif (self.monat == 6 and self.tag >= 22) or (self.monat == 7 and self.tag <= 22):
            return "Krebs"
        elif (self.monat == 7 and self.tag >= 23) or (self.monat == 8 and self.tag <= 23):
            return "Löwe"
        elif (self.monat == 8 and self.tag >= 24) or (self.monat == 9 and self.tag <= 23):
            return "Jungfrau"
        elif (self.monat == 9 and self.tag >= 24) or (self.monat == 10 and self.tag <= 23):
            return "Waage"
        elif (self.monat == 10 and self.tag >= 24) or (self.monat == 11 and self.tag <= 22):
            return "Skorpion"
        elif (self.monat == 11 and self.tag >= 23) or (self.monat == 12 and self.tag <= 21):
            return "Schütze"
        elif (self.monat == 12 and self.tag >= 22) or (self.monat == 1 and self.tag <= 20):
            return "Steinbock"
        elif (self.monat == 1 and self.tag >= 21) or (self.monat == 2 and self.tag <= 19):
            return "Wassermann"
        elif (self.monat == 2 and self.tag >= 20) or (self.monat == 3 and self.tag <= 20):
            return "Fische"
    
    def berechne_chinesisches_sternzeichen(self):
        """Berechnet das chinesische Sternzeichen basierend auf dem Geburtsjahr."""
        tiere = ["Ratte", "Büffel", "Tiger", "Hase", "Drache", "Schlange", "Pferd", "Ziege", "Affe", "Hahn", "Hund", "Schwein"]
        startjahr = 1924  # Zyklus beginnt im Jahr 1924 mit der Ratte
        index = (self.jahr - startjahr) % 12
        return tiere[index]
    
    def ausgabe_informationen(self):
        """Gibt alle berechneten Informationen aus."""
        alter = self.berechne_alter()
        wochentag_geburt = self.berechne_wochentag()
        naechster_geburtstag, wochentag_naechster_geburtstag = self.berechne_naechster_geburtstag()
        westliches_sternzeichen = self.berechne_westliches_sternzeichen()
        chinesisches_sternzeichen = self.berechne_chinesisches_sternzeichen()
        
        print(f"Du wurdest am {self.tag}.{self.monat}.{self.jahr} geboren, das war ein {wochentag_geburt}.")
        print(f"Du bist {alter} Jahre alt.")
        print(f"Dein nächster Geburtstag ist am {naechster_geburtstag.strftime('%d.%m.%Y')} und das ist ein {wochentag_naechster_geburtstag}.")
        print(f"Dein westliches Sternzeichen ist {westliches_sternzeichen}.")
        print(f"Dein chinesisches Sternzeichen ist {chinesisches_sternzeichen}.")


import datetime

def eingabe_birthday():
    # Tag eingeben und verifizieren ob es richtig ist
    while True:
        try:
            tag = int(input("Gib deinen Geburtstag ein (Tag): "))
            if not (1 <= tag <= 31):
                print(f"Ungültiger Tag: {tag}. Bitte gib einen Tag zwischen 1 und 31 ein.")
            else:
                break  # Tag ist gültig
        except ValueError:
            print("Ungültige Eingabe. Bitte gib eine Zahl für den Tag ein.")

    # Monat eingeben und verifizieren ob es richtig ist
    while True:
        try:
            monat = int(input("Gib deinen Geburtsmonat ein (Monat): "))
            if not (1 <= monat <= 12):
                print(f"Ungültiger Monat: {monat}. Bitte gib einen Monat zwischen 1 und 12 ein.")
            else:
                break  # Monat ist gültig
        except ValueError:
            print("Ungültige Eingabe. Bitte gib eine Zahl für den Monat ein.")

    # Jahr eingeben und verifizieren ob es richtig ist
    while True:
        try:
            jahr = int(input("Gib dein Geburtsjahr ein (Jahr): "))
            if jahr < 0:
                print(f"Ungültiges Jahr: {jahr}. Bitte gib ein gültiges Jahr ein.")
            else:
                break  # Jahr ist gültig
        except ValueError:
            print("Ungültige Eingabe. Bitte gib eine Zahl für das Jahr ein.")
    
    # Überprüfen, ob das eingegebene Datum gültig ist
    while True:
        try:
            geburtsdatum = datetime.date(jahr, monat, tag)  # Prüfen, ob das Datum existiert
            return tag, monat, jahr  # Gültiges Datum, also Rückgabe der Werte
        except ValueError:
            print(f"Das Datum {tag}.{monat}.{jahr} ist ungültig. Bitte gib einen gültigen Tag und Monat ein.")
            # Tag und Monat müssen erneut eingegeben werden, aber das Jahr bleibt gleich
            tag = int(input("Gib deinen Geburtstag erneut ein (Tag): "))
            monat = int(input("Gib deinen Geburtsmonat erneut ein (Monat): "))

if __name__ == "__main__":
    # Die Eingabe des Geburtstags mit Fehlerbehandlung
    tag, monat, jahr = eingabe_birthday()
    
    # Die Erstellung des Objekts der Klasse Person
    person = Person(tag, monat, jahr)
    
    # Die Ausgabe der berechneten Informationen
    person.ausgabe_informationen()


