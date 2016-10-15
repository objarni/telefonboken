Telefonboken - lite större Pythonövning
=======================================

Uppgift 1
---------

Skriv ett program som frågar användaren efter ett namn, och skriver ut personens
telefonnummer om det hittas i telefonboken (som är fördefinierad), eller "hittar
inte XXX i telefonboken!" annars.

Exempel på interaktion:

    Välkommen till Telefonboken!
    Jag känner till 2 telefonnummer.
    Ange namn: Olof Bjarnason
    Olof Bjarnasons nummer är: 0703980021

Telefonboken defineras av en fil "bok.txt", formatterad på följande sätt:

    olof bjarnason;0703980021
    jens bernpainter;0707123456

Varje namn+telefonnummer är separerade med semikolen, och avslutade med nyrad (\n).

Observera att alla namn står med små bokstäver i filen. Alla uppslag sker mot
strängar som består av enbart små bokstäver.

**Tips 1** Använd for-loop mot open("bok.txt"), samt datastrukturen dictionary.

Dictionaries används så här:

    >>> d = {}
    >>> d["abc"] = 5
    >>> d['def'] = 70
    >>> d['ghi'] = '505'
    >>> d['abc']
    5
    >>> d["OJOJ"]
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    KeyError: 'OJOJ'
    >>> d
    {'abc': 5, 'ghi': '505', 'def': 70}
    >>> len(d)
    3
    >>> if 'def' in d: print 'hej'
    ... 
    hej

**Tips 2** Använd ett textredigeringsprogram som förstår unicode, t.ex. IDLE eller
Sublime Text. Om Python gnäller på "encoding" errors (sannolikt p.g.a. att du använt
Å, Ä eller Ö i filen), så lägg till följande magiska rad som första rad i filen:

    # coding: utf-8

.. och se till så filen sparas i utf-8 (syns på statusbaren i Sublime vilken kodning
filen man jobbar i har).

**Tips 3** Läs på om "string formatting" i Python. Ex:

    print "Längd: %d %s" % (millimeter, enhet)

