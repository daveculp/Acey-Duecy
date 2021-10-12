from playing_cards import *

print ("""
This is the game of Acey-Duecy.  

You start with $200 and each turn you will be dealt two cards.  You will
then place a bet, betting whether the next card dealt will be between 
the first two cards.

Numerical values of face cards:
Jack = 11
Queen = 12
King = 13
Ace = 14

Suit order from low to high is clubs, diamonds, hearts, spades.

Minimum bet is $10.

The game continues until you have no money or the deck runs out.
""")

deck = Deck()
deck.shuffle()
money = 200
game_running = True

while game_running:
	
	card1 = deck.get_next()
	card2 = deck.get_next()
	
	#this while loop prints the cards and gets the player bet
	while True:
		time.sleep(.5)
		print(80*"=")
		print("You have ${0}".format(money) )
		print ("Card 1:{0}".format(card1) )
		print ("Card 2:{0}".format(card2) )
		
		#get player bet and check that it is legal
		bet = input ("What is your bet [$10]? ")
		if bet == "":
			bet = "10"
		if bet.isdigit() == False:
			print("You have to enter an actual number!")
			continue
		bet = int(bet) #we passed the above test, its a number
		if bet<10:
			print("The minimum bet is $10.  Please try again!")
			continue
		if (bet <= money) and (bet >= 0):
			break  #break out of while loop, bet has been taken
		time.sleep(.5)
		print("That is not a legal bet! Try again!")
	
	#get the third card
	card3 = deck.get_next() 
	print ("Card 3:{0}".format(card3) )
	time.sleep(.5)
	
	#check if it is between the first two
	if card3.between(card1,card2) and bet > 0:
		print ("YOU WIN!!!")
		money += bet
	elif bet > 0:
		print ("Sorry, you lose!")
		money -= bet
	
	print ("Cards left in the deck {0}".format( len(deck) ) )
	time.sleep(.5)
	
	#check game end
	if money < 10 :
		game_running = False
		print ("YOU HAVE RUN OUT OF MONEY!!")
	elif len(deck) < 3:
		print("We have run though the deck! There will not be enough")
		print("cards for another draw.")
		game_running = False
		
	#if over, print message and ask the user if they want to play again!	
	if game_running == False:
		print(80*"=")
		print ("You ended with ${0}".format(money))
		for i in range(10):		
			print (" "*i+"Game over!")
			time.sleep(.1)
		for i in range(10,-1,-1):
			print (" "*i+"Game over!")
			time.sleep(.1)
		again = input("Play again? (y/n)")
		if again[0].lower() == "y":
			print ("Resetting game....")
			money = 200
			deck.shuffle()
			game_running = True

print ("Thanks for playing acey duecy!!")

		
		
	


