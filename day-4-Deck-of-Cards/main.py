import random
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    def present(self):
        return f'{self.value} of {self.suit}'

class Deck:
    def __init__(self):
        self.cards = []
        self.suits = ['hearts', 'diamonds', 'clubs', 'spades']
        self.values = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        for suit in self.suits:
            for value in self.values:
                self.cards.append(Card(suit, value))
    def shuffle(self):
        random.shuffle(self.cards)
    def deal(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            return None
    def count_remaining(self):
        return len(self.cards)
    def get_remaining(self):
        return [card.present() for card in self.cards]

deck = Deck()
print(deck.count_remaining())   
deck.shuffle()
card = deck.deal()
print(card.present())          
print(deck.count_remaining())  
print(deck.get_remaining())     
