import random
import time 

class Card:
	text_values = (None,None,"2","3","4","5","6","7","8","9","10","Jack","Queen", "King", "Ace")
	suits = ("Clubs", "Diamonds", "Hearts", "Spades")
	
	def __init__(self, value, suit):
		self.value = value
		self.suit = suit
		
	def show(self):
		print ( '{0} of {1}'.format(Card.text_values[self.value], self.suit) )
		
	def get_value(self):
		return self.value
		
	def get_suit(self):
		return self.suit
		
	def __lt__(self, card):
		if self.value < card.value:
			return True
		if self.value == card.value:
			if Card.suits.index(self.suit) < Card.suits.index(card.suit):
				return True
		return False
		
	def __gt__(self, card):
		if self.value > card.value:
			return True
		if self.value == card.value:
			if Card.suits.index(self.suit) > Card.suits.index(card.suit):
				return True
		return False	
		
	def __eq__(self, card):
		if (self.value == card.value):
			return True
		return False
			
	def between(self, card1, card2):
		if (card1.value == card2.value) or (card1.value < card2.value):
			return card1 < self < card2
		else:
			return card2 < self < card1
	
	def __str__(self):
		return '{0} of {1}'.format(Card.text_values[self.value], self.suit)

class Deck:
	def __init__(self):
		random.seed()
		self.construct()

	def construct(self):
		self.cards = []
		for suit in Card.suits:
			for value in range(2,15):
				self.cards.append(Card(value,suit))
				
	def shuffle(self):
		random.shuffle(self.cards)
		
	def choose(self, remove = False):
		if len(self.cards) == 0:
			return None
		card = random.choice(self.cards)
		if remove:
			self.cards.remove(card)
		return card
		
	def get_next(self,remove = True):
		if len(self.cards) == 0:
			return None
		card = self.cards.pop(0)
		if remove==False:
			self.cards.append(card)
		return card
		
	def len(self):
		return len(self.cards)

	def show(self):
		for card in self.cards:
			card.show()

print ("""
This is the game of Acey-Duecy.  

You start with $200 and each turn you will be dealt two cards.  You will
then place a bet,betting whether the next card dealt will be between the
first two cards.

In this game, the value of an Ace = 13
Suit order is clubs, diamonds, hearts, spades.

The game continues until you have no money or the deck runs out.
""")

deck = Deck()
deck.shuffle()
money = 200

while money > 0 and deck.len() >0:
	
	time.sleep(1)
	print(80*"=")
	print("You have ${0}".format(money) )
	
	card1 = deck.get_next()
	card2 = deck.get_next()
	
	print ("Card 1:", card1)
	print ("Card 2:", card2)
	
	bet = money+1
	while (bet > money) and (bet > 0):
		bet = input ("What is your bet? ")
		bet = int(bet)
	time.sleep(2)
	if bet == 0:
		print("Thats a chicken bet!")
		time.sleep(1)
		
	card3 = deck.get_next()
	print ("Card 3:", card3)
	time.sleep(1)
	if card3.between(card1,card2) and bet > 0:
		print ("YOU WIN!!!")
		money += bet
	elif bet > 0:
		print ("Sorry, you lose!")
		money -= bet
	time.sleep(1)
	
	time.sleep(1)
	print ("Cards left in the deck {0}".format( deck.len() ) )
	


	if deck.len() <=2:
		print("We have run though the deck!")
		break

print(80*"=")
for i in range(10):		
	print (" "*i+"Game over!")
	time.sleep(.1)
for i in range(10,0,-1):
	print (" "*i+"Game over!")
	time.sleep(.1)

print ("You ended with ${0}".format(money))
		
		
	


