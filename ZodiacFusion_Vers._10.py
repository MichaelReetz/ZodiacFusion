'''Mehrsprachige Unterstützung: Der Code fragt nach der bevorzugten Sprache
des Nutzers und zeigt die Texte in Deutsch, Englisch, Spanisch oder 
Französisch an'''

import datetime

class Person:
    def __init__(self, tag, monat, jahr, sprache):
        self.tag = tag
        self.monat = monat
        self.jahr = jahr
        self.sprache = sprache
        self.geburtsdatum = datetime.date(jahr, monat, tag)
        self.heute = datetime.date.today()

    def berechne_alter(self):
        alter = self.heute.year - self.geburtsdatum.year
        if (self.heute.month, self.heute.day) < (self.geburtsdatum.month, self.geburtsdatum.day):
            alter -= 1
        return alter

    def berechne_wochentag(self):
        wochentag = self.geburtsdatum.weekday()
        wochentag_der_geburt_de = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]
        wochentag_der_geburt_en = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        wochentag_der_geburt_fr = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
        wochentag_der_geburt_es = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

        if self.sprache == 'D':
            return wochentag_der_geburt_de[wochentag]
        elif self.sprache == 'E':
            return wochentag_der_geburt_en[wochentag]
        elif self.sprache == 'F':
            return wochentag_der_geburt_fr[wochentag]
        elif self.sprache == 'S':
            return wochentag_der_geburt_es[wochentag]

    def berechne_naechster_geburtstag(self):
        try:
            naechster_geburtstag = self.geburtsdatum.replace(year=self.heute.year)
        except ValueError:
            naechster_geburtstag = self.geburtsdatum.replace(year=self.heute.year, day=28)
        
        if self.heute > naechster_geburtstag:
            try:
                naechster_geburtstag = naechster_geburtstag.replace(year=self.heute.year + 1)
            except ValueError:
                naechster_geburtstag = naechster_geburtstag.replace(year=self.heute.year + 1, day=28)
        
        wochentag_naechster_geburtstag = naechster_geburtstag.weekday()
        wochentag_der_geburt_de = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]
        wochentag_der_geburt_en = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        wochentag_der_geburt_fr = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
        wochentag_der_geburt_es = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

        if self.sprache == 'D':
            return (naechster_geburtstag, wochentag_der_geburt_de[wochentag_naechster_geburtstag])
        elif self.sprache == 'E':
            return (naechster_geburtstag, wochentag_der_geburt_en[wochentag_naechster_geburtstag])
        elif self.sprache == 'F':
            return (naechster_geburtstag, wochentag_der_geburt_fr[wochentag_naechster_geburtstag])
        elif self.sprache == 'S':
            return (naechster_geburtstag, wochentag_der_geburt_es[wochentag_naechster_geburtstag])

    def berechne_westliches_sternzeichen(self):
        if (self.monat == 3 and self.tag >= 21) or (self.monat == 4 and self.tag <= 19):
            return "Widder" if self.sprache == 'D' else "Aries" if self.sprache == 'E' else "Aries" if self.sprache == 'S' else "Bélier"
        elif (self.monat == 4 and self.tag >= 20) or (self.monat == 5 and self.tag <= 20):
            return "Stier" if self.sprache == 'D' else "Taurus" if self.sprache == 'E' else "Tauro" if self.sprache == 'S' else "Taureau"
        elif (self.monat == 5 and self.tag >= 21) or (self.monat == 6 and self.tag <= 20):
            return "Zwillinge" if self.sprache == 'D' else "Gemini" if self.sprache == 'E' else "Géminis" if self.sprache == 'S' else "Gémeaux"
        elif (self.monat == 6 and self.tag >= 21) or (self.monat == 7 and self.tag <= 22):
            return "Krebs" if self.sprache == 'D' else "Cancer" if self.sprache == 'E' else "Cáncer" if self.sprache == 'S' else "Cancer"
        elif (self.monat == 7 and self.tag >= 23) or (self.monat == 8 and self.tag <= 22):
            return "Löwe" if self.sprache == 'D' else "Leo" if self.sprache == 'E' else "Leo" if self.sprache == 'S' else "Lion"
        elif (self.monat == 8 and self.tag >= 23) or (self.monat == 9 and self.tag <= 22):
            return "Jungfrau" if self.sprache == 'D' else "Virgo" if self.sprache == 'E' else "Virgo" if self.sprache == 'S' else "Vierge"
        elif (self.monat == 9 and self.tag >= 23) or (self.monat == 10 and self.tag <= 22):
            return "Waage" if self.sprache == 'D' else "Libra" if self.sprache == 'E' else "Libra" if self.sprache == 'S' else "Balance"
        elif (self.monat == 10 and self.tag >= 23) or (self.monat == 11 and self.tag <= 21):
            return "Skorpion" if self.sprache == 'D' else "Scorpio" if self.sprache == 'E' else "Escorpio" if self.sprache == 'S' else "Scorpion"
        elif (self.monat == 11 and self.tag >= 22) or (self.monat == 12 and self.tag <= 21):
            return "Schütze" if self.sprache == 'D' else "Sagittarius" if self.sprache == 'E' else "Sagitario" if self.sprache == 'S' else "Sagittaire"
        elif (self.monat == 12 and self.tag >= 22) or (self.monat == 1 and self.tag <= 19):
            return "Steinbock" if self.sprache == 'D' else "Capricorn" if self.sprache == 'E' else "Capricornio" if self.sprache == 'S' else "Capricorne"
        elif (self.monat == 1 and self.tag >= 20) or (self.monat == 2 and self.tag <= 18):
            return "Wassermann" if self.sprache == 'D' else "Aquarius" if self.sprache == 'E' else "Acuario" if self.sprache == 'S' else "Verseau"
        elif (self.monat == 2 and self.tag >= 19) or (self.monat == 3 and self.tag <= 20):
            return "Fische" if self.sprache == 'D' else "Pisces" if self.sprache == 'E' else "Piscis" if self.sprache == 'S' else "Poisson"

    def berechne_chinesisches_sternzeichen(self):
        tiere = [
            "Ratte", "Ochse", "Tiger", "Hase", "Drache", "Schlange", "Pferd", "Ziege", "Affe", "Hahn", "Hund", "Schwein"
        ]
        tiere_en = [
            "Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig"
        ]
        tiere_es = [
            "Rata", "Buey", "Tigre", "Liebre", "Dragón", "Serpiente", "Caballo", "Cabra", "Mono", "Gallo", "Perro", "Cerdo"
        ]
        tiere_fr = [
            "Rat", "Bœuf", "Tigre", "Lapin", "Dragon", "Serpent", "Cheval", "Chèvre", "Singe", "Coq", "Chien", "Cochon"
        ]
        return tiere[self.jahr % 12] if self.sprache == 'D' else tiere_en[self.jahr % 12] if self.sprache == 'E' else tiere_es[self.jahr % 12] if self.sprache == 'S' else tiere_fr[self.jahr % 12]

    def ausgabe_informationen(self):
        alter = self.berechne_alter()
        wochentag = self.berechne_wochentag()
        naechster_geburtstag, wochentag_naechster = self.berechne_naechster_geburtstag()
        westliches_sternzeichen = self.berechne_westliches_sternzeichen()
        chinesisches_sternzeichen = self.berechne_chinesisches_sternzeichen()

        # Ausgabe in der gewählten Sprache
        if self.sprache == 'D':
            print(f"Du bist {alter} Jahre alt.")
            print(f"Du wurdest an einem {wochentag} geboren.")
            print(f"Dein nächster Geburtstag ist am {naechster_geburtstag.day}.{naechster_geburtstag.month}.{naechster_geburtstag.year} ({wochentag_naechster}).")
            print(f"Dein westliches Sternzeichen ist {westliches_sternzeichen}.")
            print(f"Dein chinesisches Sternzeichen ist {chinesisches_sternzeichen}.")
        elif self.sprache == 'E':
            print(f"You are {alter} years old.")
            print(f"You were born on a {wochentag}.")
            print(f"Your next birthday is on {naechster_geburtstag.day}/{naechster_geburtstag.month}/{naechster_geburtstag.year} ({wochentag_naechster}).")
            print(f"Your western zodiac sign is {westliches_sternzeichen}.")
            print(f"Your Chinese zodiac sign is {chinesisches_sternzeichen}.")
        elif self.sprache == 'S':
            print(f"Tienes {alter} años.")
            print(f"Naciste en un {wochentag}.")
            print(f"Tu próximo cumpleaños es el {naechster_geburtstag.day}/{naechster_geburtstag.month}/{naechster_geburtstag.year} ({wochentag_naechster}).")
            print(f"Tu signo zodiacal occidental es {westliches_sternzeichen}.")
            print(f"Tu signo zodiacal chino es {chinesisches_sternzeichen}.")
        elif self.sprache == 'F':
            print(f"Vous avez {alter} ans.")
            print(f"Vous êtes né un {wochentag}.")
            print(f"Votre prochain anniversaire est le {naechster_geburtstag.day}/{naechster_geburtstag.month}/{naechster_geburtstag.year} ({wochentag_naechster}).")
            print(f"Votre signe du zodiaque occidental est {westliches_sternzeichen}.")
            print(f"Votre signe du zodiaque chinois est {chinesisches_sternzeichen}.")

def eingabe_birthday():
    sprache = input("Wählen Sie eine Sprache (D für Deutsch, E für Englisch, S für Spanisch, F für Französisch): ").strip().upper()
    while sprache not in ['D', 'E', 'S', 'F']:
        print("Ungültige Eingabe. Bitte wählen Sie D, E, S oder F.")
        sprache = input("Wählen Sie eine Sprache (D für Deutsch, E für Englisch, S für Spanisch, F für Französisch): ").strip().upper()

    tag_frage = {
        'D': "Gib deinen Geburtstag (Tag) ein: ",
        'E': "Enter your birthday (day): ",
        'S': "Ingresa tu cumpleaños (día): ",
        'F': "Entrez votre anniversaire (jour): "
    }[sprache]
    
    monat_frage = {
        'D': "Gib deinen Geburtsmonat (Monat) ein: ",
        'E': "Enter your birth month (month): ",
        'S': "Ingresa tu mes de nacimiento (mes): ",
        'F': "Entrez votre mois de naissance (mois): "
    }[sprache]
    
    jahr_frage = {
        'D': "Gib dein Geburtsjahr (Jahr) ein: ",
        'E': "Enter your birth year (year): ",
        'S': "Ingresa tu año de nacimiento (año): ",
        'F': "Entrez votre année de naissance (année): "
    }[sprache]

    fehler_tag = {
        'D': "Ungültiger Tag. Bitte gib einen Tag zwischen 1 und 31 ein.",
        'E': "Invalid day. Please enter a day between 1 and 31.",
        'S': "Día inválido. Por favor, ingrese un día entre 1 y 31.",
        'F': "Jour invalide. Veuillez entrer un jour entre 1 et 31."
    }[sprache]

    fehler_monat = {
        'D': "Ungültiger Monat. Bitte gib einen Monat zwischen 1 und 12 ein.",
        'E': "Invalid month. Please enter a month between 1 and 12.",
        'S': "Mes inválido. Por favor, ingrese un mes entre 1 y 12.",
        'F': "Mois invalide. Veuillez entrer un mois entre 1 et 12."
    }[sprache]

    fehler_jahr = {
        'D': "Ungültiges Jahr. Bitte gib ein Jahr ein, das nicht in der Zukunft liegt.",
        'E': "Invalid year. Please enter a year that is not in the future.",
        'S': "Año inválido. Por favor, ingrese un año que no esté en el futuro.",
        'F': "Année invalide. Veuillez entrer une année qui n'est pas dans le futur."
    }[sprache]

    while True:
        try:
            tag = int(input(tag_frage))
            if not (1 <= tag <= 31):
                print(fehler_tag)
                continue
            break
        except ValueError:
            print(fehler_tag)

    while True:
        try:
            monat = int(input(monat_frage))
            if not (1 <= monat <= 12):
                print(fehler_monat)
                continue
            break
        except ValueError:
            print(fehler_monat)

    while True:
        try:
            jahr = int(input(jahr_frage))
            if jahr > datetime.date.today().year:
                print(fehler_jahr)
                continue
            break
        except ValueError:
            print(fehler_jahr)

    while True:
        try:
            geburtsdatum = datetime.date(jahr, monat, tag)
            return tag, monat, jahr, sprache
        except ValueError:
            print(datum_fehler)

# Beispiel für die Verwendung der Klasse
tag, monat, jahr, sprache = eingabe_birthday()
person = Person(tag, monat, jahr, sprache)
person.ausgabe_informationen()

weitere_anfrage = input("Möchtest du eine weitere Anfrage durchführen? (ja/nein): ").strip().lower()
if weitere_anfrage != 'ja':
    print("Programm beendet.")
    
