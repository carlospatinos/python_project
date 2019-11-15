# Python project 

## Problem statement
I want to be able to generate fibonacci sequence and store those result in files, having an index of all the generated files for reference. 

The purpose is just to play a bit with python.

## How to run
The program should be run as follows: 
```sh
python programa.py prefix_name
```
The only argument should be prefix_name, a string that will be appended to all the generated files. 

## Options listed

After the application starts, it should present a menu like this:

Menu:
1- list generated file names
2- Generate a new sequence (and store it in file)

### Inputs required for option 2

The only input required is a valid number. Then the file name will be generated as: prefix + number + date with format as dd-mm-yy

Fibonacci sequence will be generated based on the input value (provided by end user) and stored in a file. All the generated file names will be listed if end user choses option 1. 

Its important to manage error conditions like invalid characters and provide tests where applicable. 
