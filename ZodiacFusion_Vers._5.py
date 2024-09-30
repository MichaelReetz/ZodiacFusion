import datetime

# In dieser Version wollte ich das er auch den Wochentag vom nächsten Geburtstag ausgibt
def berechne_alter(tag, monat, jahr):
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
    # Zunächst den nächsten Geburtstag im aktuellen Jahr annehmen
    naechster_geburtstag = datetime.date(heute.year, monat, tag)
    
    # Wenn der Geburtstag in diesem Jahr schon vorbei ist, auf nächstes Jahr verschieben
    if heute > naechster_geburtstag:
        naechster_geburtstag = datetime.date(heute.year + 1, monat, tag)
    
    # Wochentag des nächsten Geburtstags
    wochentag_naechster_geburtstag = naechster_geburtstag.weekday()
    
    return (alter, 
            wochentag_der_geburt[wochentag], 
            naechster_geburtstag, 
            wochentag_der_geburt[wochentag_naechster_geburtstag])

# Einfacher Ablauf mit Eingabe für den Geburtstag
tag = int(input("Gib deinen Geburtstag ein (Tag): "))
monat = int(input("Gib deinen Geburtsmonat ein (Monat): "))
jahr = int(input("Gib dein Geburtsjahr ein (Jahr): "))

# Alter, Wochentag der Geburt und nächster Geburtstag berechnen
alter, wochentag, naechster_geburtstag, wochentag_naechster_geburtstag = berechne_alter(tag, monat, jahr)

# Ausgabe der Informationen
print(f"Du wurdest am {tag}.{monat}.{jahr} geboren, das war ein ---{wochentag}---.")
print(f"Du bist ---{alter}--- Jahre alt.")
print(f"Dein nächster Geburtstag ist am {naechster_geburtstag.strftime('%d.%m.%Y')} und das ist ein ---{wochentag_naechster_geburtstag}---.")
