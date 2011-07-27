#!/usr/bin/env python
# encoding: utf-8

from random import *

# första meningen
personer = ["Joshua", "Läromästaren", "Eleven", "Tao", "Koh", "Bon"]
objekt = ["en skål med ris", "ett elstängsel", "en hammare", "en spik", "ett sågspån", "en myra", "små skalbaggar", "ett nedfallande blad", "en påle som fallit över vägen"]
handlingar_imperfekt = ["åt upp", "bestämde sig för att handla", "funderade på", "kontemplerade över", "fylldes av skräck på grund av", "tappade bort", "mediterade över", "ångrade", "svalde sin sorg", "gömde sig inte"]
tider = ["Det var en sen höstdag i september", "Skymningen hade precis börjar falla", "Solen gick en dag upp"]


# andra meningen
kommunicera = ["sade sålunda: ", "framlade: ", "anförde: ", "sade då: ", "talte sålunda: ", "talte: "]

uppmaning = ["Var beredd!", "Svaret vet du själv.", "Börja med att städa på din bakgård.", "Var försiktig med analogierna", "Pissa på ett elstängsel"]


#motfraga = ["Varför 


# tredje meningen
slutsatser = ["blev upplyst", "såg in i vinden, och nickade", "förstod", "mediterade över svaret", "fortsatte sin fotvandring", "antecknade något i sitt block", "skissade något på en sten", "drog ett tecken i sanden", "ritade cirklar i sanden", "nickade och blev upplyst"]

# programmet:
person = choice(personer)
personer.remove(person) # ta bort vald person

objektet = choice(objekt)
objekt.remove(objektet)

print person, choice(handlingar_imperfekt), objektet
print "  ", choice(personer), choice(kommunicera), ("``" + choice(uppmaning) + "''")
print "    ", person, choice(slutsatser)