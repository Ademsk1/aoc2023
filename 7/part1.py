def read(file):
    with open(file) as f:
        rawdata = f.readlines()
    return rawdata

CARD_VALUES = {
	'2':2,
	'3':3,
	'4':4,
	'5':5,
	'6':6,
	'7':7,
	'8':8,
	'9':9,
	'T':10,
	'J':11,
	'Q':12,
	'K':13,
	'A':14,
}

class Card:
	def __init__(self,card):
		self.card = card
		self.value = CARD_VALUES[f'{card}']
	def __str__(self):
		return f'{self.card}-{self.value}'


class Hand:
	def __init__(self,rawcards,bet):
		self.bet = bet
		self.rawcards = rawcards
		self.cards = []
		self.value_counter = {}
		self.hand_value = []
		self.generate_cards()
		self.get_value_counter()
		self.evaluate_hand_values()
		self.evaluate_card_values()

	def generate_cards(self):
		self.cards = []
		for card in self.rawcards:
			self.cards.append(Card(card))

	def get_value_counter(self):
		self.value_counter = {}
		for card in self.cards:
			if card.card in self.value_counter.keys():
				self.value_counter[f'{card.card}'] +=1
			else:
				self.value_counter[f'{card.card}'] =1

	def evaluate_hand_values(self):
		#ordered values from 1-7 based on high card - 5 of a kind
		unique_values = len(self.value_counter.values())
		if unique_values == 1:
			#5 of a kind
			self.hand_value = [7]
		elif unique_values ==2:
			#either four of a kind, or full house
			if 4 in self.value_counter.values():
				self.hand_value = [6]
			else:
				self.hand_value = [5]
		elif unique_values == 3:
			#Either 3 of a kind, or two pair
			if 3 in self.value_counter.values():
				self.hand_value =  [4]
			else:
				self.hand_value = [3]
		elif unique_values == 4: 
			#One pair
			self.hand_value = [2]
		elif unique_values == 5:
			#Nada
			self.hand_value = [1]

	def evaluate_card_values(self):
		for card in self.cards:
			self.hand_value.append(card.value)

class Game:
	def __init__(self):
		self.hands = []
		self.winnings = 0
		self.generate_cards()
		self.get_ranking()

	def generate_cards(self):
		raw_data = read('./7/data.txt')
		for hand_bet in raw_data:
			hand,bet = hand_bet.split(' ')
			self.hands.append(Hand(hand,int(bet)))
		
	def get_ranking(self):
		self.hands.sort(key=lambda hand: hand.hand_value)
		for i,hand in enumerate(self.hands):
			print(hand.rawcards,' ', hand.hand_value, hand.bet * (i+1) )
			self.winnings += hand.bet * (i+1)

if __name__ == '__main__':
	game = Game()
	print(game.winnings)
