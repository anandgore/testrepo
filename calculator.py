#This is a simple python calculator
import sys
import os

global e_e
while True:
	try:
		rl=sys.stdin.readline()
		e_e=eval(rl);
	except SyntaxError as s:
		os.system(rl)
	except ValueError as v:
		#print(v)
		print("Ignoring input " + rl)
	except NameError as n:
		try:
			e_e=eval("0x"+rl);
		except NameError as n1:
			os.system(rl)
		except SyntaxError as s:
			os.system(rl)
		#print("Ignoring input " + rl)
		#print(n)
	try:
		evaluated=int(e_e)
		print( str(e_e) + " " + str(evaluated) + " " + str(bin(evaluated)) + " " 
			+ str(hex(evaluated)) + " " 
			+ str(oct(evaluated)))
	except TypeError as t:
		#e_e(100)
		print(t)
		pass
