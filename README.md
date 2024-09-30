# ZodiacFusion
README: ZodiacFusion
________________________________________
Projektname: ZodiacFusion
Beschreibung:
ZodiacFusion ist ein Programm, das auf Basis des Geburtsdatums eines Benutzers detaillierte Informationen über dessen westliches und chinesisches Sternzeichen sowie weitere relevante Daten berechnet. Das Programm ermittelt das Alter, den Wochentag der Geburt und den Wochentag des nächsten Geburtstags.
________________________________________
Funktionen:
1. Berechnung des Alters:
	 Das Programm berechnet das aktuelle Alter des Benutzers basierend auf dem Geburtsdatum.
2. Wochentag der Geburt:
   ZodiacFusion gibt den Wochentag an, an dem der Benutzer geboren wurde (z.B. Montag, Dienstag).
3. Nächster Geburtstag:
   Es wird das genaue Datum des nächsten Geburtstags sowie der entsprechende Wochentag ermittelt.
4. Westliches Sternzeichen:
	 Auf Grundlage des Geburtsdatums wird das westliche Sternzeichen (z.B. Widder, Stier) ausgegeben.
5. Chinesisches Sternzeichen:
   Das Programm berechnet das chinesische Sternzeichen basierend auf dem Geburtsjahr (z.B. Ratte, Büffel).
________________________________________
Eingaben:
Das Programm fordert den Benutzer auf, folgende Daten einzugeben:
•	Tag: Der Tag der Geburt (1–31)
•	Monat: Der Monat der Geburt (1–12)
•	Jahr: Das Geburtsjahr (positiver Wert)
Fehlerbehandlung:
•	Ungültige Eingaben (z.B. ein Tag über 31 oder ein Monat über 12) werden erkannt und dem Benutzer mit einer entsprechenden Fehlermeldung angezeigt. Der Benutzer wird aufgefordert, nur den fehlerhaften Teil erneut einzugeben.
•	Ungültige Datumswerte wie der 30. Februar werden ebenfalls abgefangen und führen dazu, dass nur Tag und Monat neu eingegeben werden müssen.
________________________________________
Beispielausgabe:
Nach der Eingabe des Geburtsdatums gibt ZodiacFusion folgende Informationen aus:
Code kopieren
Du wurdest am 15.07.1990 geboren, das war ein ---Sonntag---.
Du bist ---33--- Jahre alt.
Dein nächster Geburtstag ist am 15.07.2024 und das ist ein ---Montag---.
Dein westliches Sternzeichen ist ---Krebs---.
Dein chinesisches Sternzeichen ist ---Pferd---.
________________________________________
Installation und Ausführung:
1.	Stelle sicher, dass Python auf deinem System installiert ist (mindestens Version 3.6).
2.	Lade die zodiacfusion.py Datei herunter.
3.	Führe das Programm über die Kommandozeile oder eine IDE aus:
bash
Code kopieren
python zodiacfusion.py
4.	Folge den Anweisungen auf dem Bildschirm, um dein Geburtsdatum einzugeben.
________________________________________
Lizenz:
ZodiacFusion ist ein Open-Source-Projekt und unterliegt der Apache-Lizenz. Anpassungen und Beiträge sind willkommen!
________________________________________
Autor:
Michael Reetz
ZodiacFusion 
