Telefonboken - lite större Pythonövning
=======================================

Uppgift 3
---------

_Strukturera om programmet från uppgift 2 till objekt._

OK, så nu kommer vi till klasser (keyword: `class`) eller,
som jag föredrar att tänka på dem, objekt.

Lite bakgrund: på 90-talet kom det en stor trend inom
programmering som kallas "objektorienterad programmering",
eller "OOP". Denna trend blev det enormt stor "hype" kring
då, och väldigt många system skrevs med denna paradigm som
religös dogm snarare än genomtänkt och medvetet. Idag är
OOP mycket svagare och till och med ifrågasatt på många håll.

Jag är praktiskt lagd och använder objekt/klasser som ett
verktyg för att få läsbar kod, undviker "arvshierarkier"
(det som gett mest problem inom OOP) i stor utsträckning,
men skyr det inte som elden.

Så vad betyder då objekt/klasser? Tja mycket enkelt sagt är
bara objekt "säckar" där man kan lägga variabler och funktioner.
Kanske tänker du "men är inte det precis som dictionaries"? och
då tänker du ganska rätt. En skillnad är att objekt har en
bekvämare syntax där man slipper hakparenteser `[]` och
fnuttar `""`:

    # Dictionary
    d = {}
    d['abc'] = 5
    d['listdir'] = os.listdir  # inbyggd funktion för att lista directory
    # Objekt
    o = MyClass()
    o.abc = 5
    o.listdir = os.listdir

En annan skillnad är att objekt har saker i sig från början,
medan dictionaries är tomma. Det som avgör vad som finns i objektet
från början är `MyClass()`-anropet ovan, det som kallas "konstruktorn"
i OOP-sammanhang. "Konstruktorn" (constructor) "konstruerar", eller
bygger upp, objektets initiala tillstånd.

Konstruktorer i Python har alltid namnet `__init__`, men när man
anropar dem använder man klassnamnet, som `MyClass()`. `MyClass()`
innebär alltså ett anrop till `__init__`-metoden som ligger i
klassen med namnet `MyClass`:

    class MyClass(object):
        def __init__(self):
            self.b = 6

        def double(self, a):
            return a * 2

Om vi tittar tillbaka på min lösning av uppgift 2 ser vi att vi
namnet "`book`" är vanligt. Det antyder att det finns ett koncept
som vill födas där... En idé är att helt enkelt bygga en klass
som heter "`PhoneBook`", som kan göra det vi vill att den ska göra
(ladda, spara, slå upp namn, lägga till namn, ...).

Så här skulle det se ut att använda klassen interaktivt:

    >>> book = PhoneBook("bok.txt"):
    >>> book.add_number("39393939", "Bob Dylan")
    >>> book.lookup_number("Bob Dylan")
    "39393939"
    >>> book.count_numbers()
    3

Laddning- och sparning kan ske "automatiskt" i konstruktorn,
och när man lägger till nya telefonnummer. Kort och koncist,
och lite som att uppfinna ett "språk" för programmet, eller hur?

Så här ser skelettet för klassen `PhoneBook` ut:

    class PhoneBook(object):
        def __init__(self, bookpath):
            pass

        def add_number(self, number, name):
            pass

        def lookup_number(self,  name):
            pass

        def count_numbers(self):
            pass

Notera keyword `pass`, som betyder "gör ingenting" i Python.
Bra för att fylla i funktioner som inte är implementerade ännu.

Din uppgift blir att fylla i funktionerna samt att skriva om loopen
från uppgift 2 till att använda en PhoneBook istället för en
dictionary.
