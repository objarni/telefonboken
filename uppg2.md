Telefonboken - lite större Pythonövning
=======================================

Uppgift 2
---------

Utöka programmet från uppgift 1 med lite mera struktur, och interaktion.

Man ska bli serverad en trevlig textmeny när man startar,
och kunna ställa flera frågor innan man avslutar programmet,
och dessutom kunna lägga till nya nummer i telefonboken:

    Välkommen till Telefonboken!

    ** Meny **
    Jag känner till 2 telefonnummer.
    1. Slå upp telefonnummer
    2. Lägg till nytt telefonnummer
    3. Avsluta
    Ange val: 1
    Ange namn: Olof Bjarnason
    Olof Bjarnasons nummer är: 0703980021

    ** Meny **
    Jag känner till 2 telefonnummer.
    1. Slå upp telefonnummer
    2. Lägg till nytt telefonnummer
    3. Avsluta
    Ange val: 20
    Det finns inget sådant val!
    Ange val: 2
    Nytt telefonnummer: 39393939
    Nytt namn: Bob Dylan

    ** Meny **
    Jag känner till 3 telefonnummer.
    1. Slå upp telefonnummer
    2. Lägg till nytt telefonnummer
    3. Avsluta
    Ange val: 3
    Tack och adjö!

I denna uppgift ska du använda dig av funktioner, som har nyckelordet "def"
i Python. Så här ser en exempelfunktion ut:

    def print_menu(bok):
        print "** Meny **"
        print "Jag känner till %d telefonnummer." % len(bok)
        print "1. Slå upp telefonnummer"
        print "2. Lägg till nytt telefonnummer"
        print "3. Avsluta"

Dessutom kommer du sannolikt vilja använda while, samt open("bok", "w") för att
skriva till fil (när man lägger till nytt telefonnummer). 

**Tips 1** Skapa funktioner som känns "lagom stora". T.ex. verkar "ladda_bok" och
"spara_bok" lämpliga i denna uppgift.

**Tips 2** Att strukturera program är en konst. Det finns många sätt att stycka upp
programmet på, använd din fantasi och försök eftersträva "grokkability" alltså att
koden är lätt att förstå / läsa för en annan person än dig själv.

**Tips 3** Google är din vän!

