# coding: utf-8


def load_book(path):
    d = {}
    for rad in open('bok.txt'):
        (namn, _, nummer) = rad.partition(';')
        d[namn] = nummer.strip()
    return d


def save_book(book, path):
    f = open('bok.txt', 'w')
    for name in book:
        f.write('%s;%s\n' % (name, book[name]))


def print_menu(bok):
    print "\n** Meny **"
    print "Jag känner till %d telefonnummer." % len(bok)
    print "1. Slå upp telefonnummer"
    print "2. Lägg till nytt telefonnummer"
    print "3. Avsluta"


def do_lookup(book):
    namn = raw_input("Ange namn: ")
    uppslag = namn.lower()
    if uppslag in book:
        print "%ss telefonnummer är: %s" % (namn, book[uppslag])
    else:
        print "Hittar inte %s i telefonboken!" % namn


def do_add_number(book, path):
    nummer = raw_input("Nytt nummer: ")
    namn = raw_input("Nytt namn: ")
    uppslag = namn.lower()
    book[uppslag] = nummer
    save_book(book, path)


def run():
    print "Välkommen till Telefonboken!"
    book = load_book('bok.txt')
    while True:
        print_menu(book)
        choice = int(raw_input("Ange val: "))
        if choice == 0:
            print book
        if choice not in [1, 2, 3]:
            print "Det finns inget sådant val!"
            continue
        if choice == 1:
            do_lookup(book)
        if choice == 2:
            do_add_number(book, 'bok.txt')
        if choice == 3:
            break


if __name__ == '__main__':
    run()
