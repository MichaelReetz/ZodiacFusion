import datetime

# Funktion zur Berechnung des Alters, des Wochentages und des Sternzeichens
def berechne_alter_und_sternzeichen(tag, monat, jahr):
    heute = datetime.date.today()
    geburtsdatum = datetime.date(jahr, monat, tag)
    
    # Alter berechnen
    alter = heute.year - geburtsdatum.year
    if heute.month < geburtsdatum.month or (heute.month == geburtsdatum.month and heute.day < geburtsdatum.day):
        alter -= 1
    
    # Wochentag der Geburt
    wochentag = geburtsdatum.weekday()
    wochentag_der_geburt = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]
    
    # Nächster Geburtstag berechnen
    naechster_geburtstag = datetime.date(heute.year, monat, tag)
    if heute > naechster_geburtstag:
        naechster_geburtstag = datetime.date(heute.year + 1, monat, tag)
    
    wochentag_naechster_geburtstag = naechster_geburtstag.weekday()
    
    # Sternzeichen berechnen
    sternzeichen = berechne_sternzeichen(tag, monat)
    
    return (alter, 
            wochentag_der_geburt[wochentag], 
            naechster_geburtstag, 
            wochentag_der_geburt[wochentag_naechster_geburtstag],
            sternzeichen)

# Funktion zur Berechnung des Sternzeichens basierend auf dem Geburtsdatum
def berechne_sternzeichen(tag, monat):
    if (monat == 3 and tag >= 21) or (monat == 4 and tag <= 20):
        return "Widder"
    elif (monat == 4 and tag >= 21) or (monat == 5 and tag <= 20):
        return "Stier"
    elif (monat == 5 and tag >= 21) or (monat == 6 and tag <= 21):
        return "Zwillinge"
    elif (monat == 6 and tag >= 22) or (monat == 7 and tag <= 22):
        return "Krebs"
    elif (monat == 7 and tag >= 23) or (monat == 8 and tag <= 23):
        return "Löwe"
    elif (monat == 8 and tag >= 24) or (monat == 9 and tag <= 23):
        return "Jungfrau"
    elif (monat == 9 and tag >= 24) or (monat == 10 and tag <= 23):
        return "Waage"
    elif (monat == 10 and tag >= 24) or (monat == 11 and tag <= 22):
        return "Skorpion"
    elif (monat == 11 and tag >= 23) or (monat == 12 and tag <= 21):
        return "Schütze"
    elif (monat == 12 and tag >= 22) or (monat == 1 and tag <= 20):
        return "Steinbock"
    elif (monat == 1 and tag >= 21) or (monat == 2 and tag <= 19):
        return "Wassermann"
    elif (monat == 2 and tag >= 20) or (monat == 3 and tag <= 20):
        return "Fische"

# Einfacher Ablauf mit Eingabe für den Geburtstag
tag = int(input("Gib deinen Geburtstag ein (Tag): "))
monat = int(input("Gib deinen Geburtsmonat ein (Monat): "))
jahr = int(input("Gib dein Geburtsjahr ein (Jahr): "))

# Alter, Wochentag der Geburt, nächster Geburtstag und Sternzeichen berechnen
alter, wochentag, naechster_geburtstag, wochentag_naechster_geburtstag, sternzeichen = berechne_alter_und_sternzeichen(tag, monat, jahr)

# Ausgabe der Informationen
print(f"Du wurdest am {tag}.{monat}.{jahr} geboren, das war ein ---{wochentag}---.")
print(f"Du bist ---{alter}--- Jahre alt.")
print(f"Dein nächster Geburtstag ist am {naechster_geburtstag.strftime('%d.%m.%Y')} und das ist ein ---{wochentag_naechster_geburtstag}---.")
print(f"Dein Sternzeichen ist ---{sternzeichen}---.")
