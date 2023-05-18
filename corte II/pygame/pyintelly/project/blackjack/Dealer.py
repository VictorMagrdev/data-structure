
class Dealer:
    def __init__(self, deck, players):
        self.deck = deck
        self.players = players
        self.hand = []
        self.bet = 0
        
    def deal(self):
        """Reparte dos cartas a cada jugador y al crupier."""
        for i in range(2):
            for player in self.players:
                card = self.deck.draw()
                player.add_card(card)
            card = self.deck.draw()
                
    def play(self):
        """El crupier juega su mano según las reglas."""
        while self.hand_value() < 17:
            card = self.deck.draw()
            self.add_card(card)
            
    def add_card(self, card):
        """Añade una carta a la mano del crupier."""
        self.hand.append(card)
        
    def reveal_hidden_card(self):
        """Revela la carta oculta del crupier."""
        self.hand.insert(0)
        
    def hand_value(self):
        """Calcula el valor de la mano del crupier."""
        value = sum(card.value for card in self.hand if card.rank != 'Ace')
        aces = [card for card in self.hand if card.rank == 'Ace']
        for ace in aces:
            if value + 11 <= 21:
                value += 11
            else:
                value += 1
        return value
    
    def reset(self):
        """Reinicia la mano y la apuesta del crupier."""
        self.hand = []
        self.bet = 0
