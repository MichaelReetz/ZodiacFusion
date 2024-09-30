import datetime

# Das ursprüngliche Programm zur Berechnung von Alter, 
# westlichem und chinesischem Sternzeichen sowie des nächsten 
# Geburtstags und des Wochentags der Geburt war prozedural aufgebaut. 

# Mein Ziel oder Hauptlogik bestand aus einzelnen Funktionen wie berechne_alter, 
# berechne_westliches_sternzeichen und berechne_chinesisches_sternzeichen, 
# die aufgerufen wurden, um die entsprechenden Informationen von 
# der Benutzereingaben zu berechnen. 

class Person:
    def __init__(self, tag, monat, jahr):
        self.tag = tag
        self.monat = monat
        self.jahr = jahr
        self.heute = datetime.date.today()
        self.geburtsdatum = datetime.date(jahr, monat, tag)

    def berechne_alter(self):
        """Berechnet das Alter basierend auf dem Geburtsdatum."""
        alter = self.heute.year - self.geburtsdatum.year
        if (self.heute.month < self.geburtsdatum.month or 
            (self.heute.month == self.geburtsdatum.month and self.heute.day < self.geburtsdatum.day)):
            alter -= 1
        return alter

    def berechne_wochentag(self):
        """Berechnet den Wochentag der Geburt."""
        wochentag = self.geburtsdatum.weekday()
        wochentag_der_geburt = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]
        return wochentag_der_geburt[wochentag]

    def berechne_naechster_geburtstag(self):
        """Berechnet das Datum and den Wochentag des nächsten Geburtstags."""
        naechster_geburtstag = datetime.date(self.heute.year, self.monat, self.tag)
        if self.heute > naechster_geburtstag:
            naechster_geburtstag = datetime.date(self.heute.year + 1, self.monat, self.tag)
        
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
        tiere = ["Ratte", "Büffel", "Tiger", "Hase", "Drache", "Schlange", "Pferd", "Ziege", "Affe", "Hahn", "Hand", "Schwein"]
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
        
        print(f"Du wurdest am {self.tag}.{self.monat}.{self.jahr} geboren, das war ein ---{wochentag_geburt}---.")
        print(f"Du bist ---{alter}--- Jahre alt.")
        print(f"Dein nächster Geburtstag ist am {naechster_geburtstag.strftime('%d.%m.%Y')} and das ist ein ---{wochentag_naechster_geburtstag}---.")
        print(f"Dein westliches Sternzeichen ist ---{westliches_sternzeichen}---.")
        print(f"Dein chinesisches Sternzeichen ist ---{chinesisches_sternzeichen}---.")

# Eingabe des Geburtstags
tag = int(input("Gib deinen Geburtstag ein (Tag): "))
monat = int(input("Gib deinen Geburtsmonat ein (Monat): "))
jahr = int(input("Gib dein Geburtsjahr ein (Jahr): "))

# Erstellung des Objekts der Klasse Person
person = Person(tag, monat, jahr)

# Ausgabe der berechneten Informationen
person.ausgabe_informationen()
