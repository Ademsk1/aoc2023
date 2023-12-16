from part1 import Card, CARD_VALUES, Hand, Game



def read(file):
    with open(file) as f:
        rawdata = f.readlines()
    return rawdata


class Hand2(Hand):
	def __init__(self,rawcards,bet):
		self.bet = bet
		self.rawcards = rawcards
		self.cards = []
		self.value_counter = {}
		self.original_value_counter = {}
		self.hand_value = []
		self.generate_cards()
		self.get_value_counter()
		self.check_jokers()
		self.evaluate_hand_values()
		self.evaluate_card_values()
		
	def get_max_card_value(self,none_joker_hand):
		return max(none_joker_hand, key=lambda card:CARD_VALUES[f'{card[0]}'])

	def check_jokers(self):
		self.original_value_counter = self.value_counter
		if 'J' in list(self.value_counter.keys()):
			
			key_values = list(self.value_counter.items())
			if len(key_values) == 1:
				return
			none_joker_values = [(card,count) for card,count in key_values if card !='J']
			if len(none_joker_values) == 2 and (all([card[1] ==1  for card in none_joker_values]) or all([card[1] ==2  for card in none_joker_values])): #e.g JJJAK
				maxcard,_ = self.get_max_card_value(none_joker_values)
			elif len(none_joker_values) == 4:
				maxcard,_ = self.get_max_card_value(none_joker_values)
			else:
				maxcard,_ = max(none_joker_values, key=lambda card:card[1])
			self.value_counter[maxcard] +=self.value_counter['J']
			del self.value_counter['J']
			



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
			self.hands.append(Hand2(hand,int(bet)))
		
	def get_ranking(self):
		self.hands.sort(key=lambda hand: hand.hand_value)
		for i,hand in enumerate(self.hands):
			print(hand.rawcards,' ', hand.hand_value, hand.bet * (i+1) )
			self.winnings += hand.bet * (i+1)

if __name__ == '__main__':
	CARD_VALUES['J'] = 1
	game = Game()
	print(game.winnings)
