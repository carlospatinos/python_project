#!/usr/bin/python
import argparse
import sys
from function import mymath

from consolemenu import *
from consolemenu.items import *

listFiboGenerated = {}

def generateFibonacciSequence():
	fibInput = raw_input("Enter a number: ")
	try:
		fibNumber = int(fibInput)
		print "Generating sequence for {}".format(fibNumber);
		fileName = args.prefix + "_" + str(fibNumber) + ".txt";
		file = open(fileName, "w") 
		file.write("FibSeq of {} is {}".format(str(fibNumber) ,str(mymath.fibFunction(fibNumber)))) 
		file.close()
		listFiboGenerated[str(fibNumber)] = fileName
		Screen().input("==Enter to return to the main menu==")
	except ValueError:
		print("That's not an int!")
   		print("No.. input string is not an Integer. It's a string") 
	
def listPrevFunctions():
	print "This are the generated files on this session"
	for ref in listFiboGenerated:
  		print(listFiboGenerated[ref])
	Screen().input("==Enter to return to the main menu==")


# define the program description
text = 'Application used to generate and list fibonnaci sequence and store results on files.'

# initiate the parser with a description
parser = argparse.ArgumentParser(description = text)
parser.add_argument("-p", "--prefix", help="Prefix appended to the generated fibonnaci files.", required=True)


args = parser.parse_args()


print "Application running with prefix: [{}]".format(args.prefix)

menu = ConsoleMenu("Fibonnaci Program", "This will generate files per number you pass")

generateFibo = FunctionItem("Generate fibonnaci data", generateFibonacciSequence)
listFibo = FunctionItem("List generated fibonnaci files", listPrevFunctions)
menu.append_item(listFibo)
menu.append_item(generateFibo)
menu.show()


