#Module imports
import time
import random

#Goal tracker



#//////////STAGES///////#

def stage_enemyUpfield():
	time.sleep(0.4)
	print("""CB: Southampton make a break with the ball past your midfielders. They're through on the back four...

		1. Tackle
		2. Slide Tackle
		3. Jockey""")

def stage_defMid():
	time.sleep(0.4)
	print("""CDM: The opposition come through the midfield. You go to intercept.
	1. Tackle
	2. Slide Tackle
	3. Jockey""")
	defMidChoice = input("Choose action: ")
	
	if defMidChoice == "1":
		defMidTackleChance = random.random()
		if defMidTackleChance > 0.5:
			print("""CDM: You successfully tackle the opposition.
			1. Pass forwards""")

			defMidSuccess = input("Choose action: ")
			if defMidSuccess == "1":
				stage_attMid()
		else:
			print("""CDM: You fail to tackle your opponent, and they get through to the final third.""")
			time.sleep(0.4)
			stage_enemyUpfield()

	if defMidChoice == "2":
		defMidSlideTackleChance = random.random()
		if defMidSlideTackleChance > 0.4:
			print("""CDM: You slide towards your opponent and kick the ball towards your attacking midfielder.""")
			time.sleep(0.4)
			stage_attMid()
		else:
			print("""CDM: You try to slide tackle your opponent, however you miss - they make a run to get past your centre-backs!""")
			stage_enemyUpfield()

	if defMidChoice == "3":
		print("CDM: You cast your limbs wide and jockey your opponent, trying to harass the ball away...")
		for count in [1,2,3]:
			time.sleep(0.2)
			print(".")
			jockeyChance = random.random()
			if jockeyChance > 0.6:
				print("You manage to tap the ball away from the opposition and up to your attacking midfielder.")
				stage_attMid()
			else:
				print("You fail to jockey Southampton's attacker and he's through on your back four.")
				stage_enemyUpfield()



def stage_attMid():
	time.sleep(0.4)
	print("""CAM: The ball comes to you in midfield.
	
	1. 1-2 pass
	2. Long Shot
	3. Make a run""")
	am_Choice = input("Select: ")
	if am_Choice == "1":
		stage_UpfieldOneTwoPlayer()
	elif am_Choice == "2":
		stage_UpfieldLongShot()
		
def stage_UpfieldOneTwoPlayer():
		time.sleep(0.4)
		print("CF: You pass the ball back, approaching the keeper. Your winger shoots...")
		time.sleep(0.1)
		print(".")
		time.sleep(0.1)
		print(".")
		time.sleep(0.1)
		print(".")
		time.sleep(0.4)
		OneTwoChance = random.random()
		if OneTwoChance > 0.75:
			time.sleep(0.4)
			print("CF: GOAL!!! Your winger fires a chip shot over the keeper and in to the back of the net.")
		else:
			time.sleep(0.4)
			print("Your winger boots the ball over the crossbar. Goal kick for Southampton.")
			enemyGoalKick()
		
def stage_UpfieldLongShot():
		print("Placeholder")
		
def enemyGoalKick():
		time.sleep(0.4)
		print("The keeper lines up for a goal kick.")
		time.sleep(0.5)
		print(".")
		time.sleep(0.5)
		print(".")
		time.sleep(0.5)
		print(".")
		time.sleep(0.3)
		print("Southampton's keeper boots the ball up to the central midfield.")
		gkLottery = random.random()
		if gkLottery > 0.6:
			stage_attMid()
		else:
			stage_defMid()
		


#///////////Kick Off
def kickoff():
	time.sleep(0.4)
	print("It's 3:00PM at the Textball Stadium - time for kickoff.")
	time.sleep(0.4)
	print("CF: You have the ball at your feet. Pass?")
	time.sleep(0.2)
	
	ko_Pass = input("Y: ")
	if ko_Pass == "Y" or "y":
		time.sleep(0.4)
		print("CF: You pass the ball and kick off. A short, fast ground pass goes to your winger.")
		ko_WingerChance = random.random()
		if ko_WingerChance < 0.4:
			time.sleep(0.4)
			print("CF: The ball arrives at your winger, but before they get to the ball Southampton's forward intercepts.")
			stage_defMid()
		else:
			print("CF: The ball arrives at your winger, who catches it on the right foot and starts to make a run upfield.")
			stage_attMid()
	else:
		print("Invalid Input")

#///////////Help Menu
def helpMenu():
	print("""TEXTBALL is a game of Football where you make choices. It's a Football text adventure.
	
	Version 1.
	
	Credits: 
	George Fitzgerald - Writer
	Harry Prentice - Professional Bandersnatcher
	""")
	helpChoice = input("Return? Y")
	if helpChoice == "Y" or "y":
		introMenu()
		


#///////////Intro menu
def introMenu():

	print("""Welcome to TEXTBALL. Please select an option: 

1. Play Kick Off
2. Help""")
	in_men_choice = input("Select: ")
	if in_men_choice == "1":
		kickoff()
	if in_men_choice == "2":
		helpMenu()
	if in_men_choice == "DEBUG":
		print("Secret")

####Game start
introMenu()