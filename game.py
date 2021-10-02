from os import *
from time import sleep
Developer = """
||--------------------------------------|
| |---------------------------------|***|
| |  programmer : soheil Vanaee	    |***|
| | instagram : soheil_developer_99 |***|
| | rubika : soheil_dev_99	    |***|
| |---------------------------------|***|
| |-------------------------------------|
"""

system("clear")

bala = ["[]" , "[]" , "[]"]

vasat = ["[]" , "[]" , "[]"]

payeen = ["[]" , "[]" , "[]"]

print(bala)
print (vasat)
print (payeen)

def name():
	input_user1 = input("user1 pleas enter number  1 , 3 : ")

	if input_user1 == "1":
		sooton1 = input("user1 >> ")
		if sooton1 == "1":
			# ---------------
			bala[0] = "[X]"
			# ---------------
		elif sooton1 == "2":
			bala[1] = "[X]"
			# ---------------
		elif sooton1 == "3":
			bala[2] = "[X]"

		system("clear")
		print(bala)
		print (vasat)	
		print (payeen)

	elif input_user1 == "2":
		sooton2 = input("===> ")
		if sooton2 == "1":
			# ---------------
			vasat[0] = "[X]"
			# ---------------
		elif sooton2 == "2":
			vasat[1] = "[X]"
			# ---------------
		elif sooton2 == "3":
			vasat[2] = "[X]"

		system("clear")
		print(bala)
		print (vasat)
		print (payeen)

	elif input_user1 == "3":
		sooton3 = input("===> ")
		if sooton3 == "1":
			# ---------------
			payeen[0] = "[X]"
			# ---------------
		elif sooton3 == "2":
			payeen[1] = "[X]"
			# ---------------
		elif sooton3 == "3":
			payeen[2] = "[X]"

		system("clear")
		print(bala)
		print (vasat)
		print (payeen)

	input_user2 = input("user 2 pleas enter number  1 , 3 : ")

	if input_user2 == "1":
		sooton1 = input("user2 >> ")
		if sooton1 == "1":
			# ---------------
			bala[0] = "[O]"
			# ---------------
		elif sooton1 == "2":
			bala[1] = "[O]"
			# ---------------
		elif sooton1 == "3":
			bala[2] = "[O]"

		system("clear")
		print(bala)
		print (vasat)	
		print (payeen)

	elif input_user2 == "2":
		sooton2 = input("===> ")
		if sooton2 == "1":
			# ---------------
			vasat[0] = "[O]"
			# ---------------
		elif sooton2 == "2":
			vasat[1] = "[O]"
			# ---------------
		elif sooton2 == "3":
			vasat[2] = "[O]"

		system("clear")
		print(bala)
		print (vasat)
		print (payeen)

	elif input_user2 == "3":
		sooton3 = input("===> ")
		if sooton3 == "1":
			# ---------------
			payeen[0] = "[O]"
			# ---------------
		elif sooton3 == "2":
			payeen[1] = "[O]"
			# ---------------
		elif sooton3 == "3":
			payeen[2] = "[O]"

		system("clear")
		print(bala)
		print (vasat)
		print (payeen)


while True:
	name()

