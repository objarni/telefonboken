# coding: utf-8

d = {}
for rad in open('bok.txt'):
    (namn, _, nummer) = rad.partition(';')
    d[namn] = nummer


print "Välkommen till Telefonboken!"
print "Jag känner till %d telefonnummer." % len(d)
namn = raw_input("Ange namn: ")
uppslag = namn.lower()
if uppslag in d:
    print "%s nummer är: %s" % (namn, d[uppslag])
else:
    print "Hittar inte %s i telefonboken!" % namn
