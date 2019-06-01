import random

def r(list):
	return random.choice(list)

startwords = ["Every", "This", "One", "Each", "Singular"]

noun1 = ["dog", "man", "snail", "entity", "dinosaur", "alligator"]

verb1 = ["has", "wishes for", "must have", "chooses to reach for", 
	"has lost", "strives for", "must strive for"]

conjunction = ["its", "a", "their", "others'", "inner"]

noun2 = ["day", "night", "luck", "fortune", "inspiration"]

# print("{} {} {} {} {}".format( r(startwords), r(noun1), r(verb1), r(conjunction), r(noun2) ))

def getQuote():
	return "{} {} {} {} {}".format( r(startwords), r(noun1), r(verb1), 
		r(conjunction), r(noun2) )

