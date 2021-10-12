import random
def show(deck):
	for card in deck:
		print( '{0} of {1}'.format( card_values [card[0]], card[1]) )

def shuffle(deck):
	random.shuffle(deck)
	
def choose_random(deck, discards, remove = True):
	if len(deck) == 0:
		return None
		
	card = random.choice(deck)
	if remove:
		deck.remove(card)
		deck.append(card)
	return card
	
def get_next(deck, discards, remove = True):
	if len(deck) == 0:
		return None
	card = deck.pop(0)
	if remove==False:
		deck.append(card)
	else:
		self.discards.append(card)
	return card

deck = []
discards = []

suits = ("Clubs", "Diamonds","Hearts", "Spades")
card_values = {2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9",10:"10",11:"Jack",12:"Queen", 13:"King", 14:"Ace"}
for suit in range (0,4):
	for val in range(2,15):
		card = (val, suits[suit])
		deck.append(card)
		
show(deck)
shuffle(deck)
print ("\n\n\n\n\Shuffled\n\n\n\n")
show(deck)


