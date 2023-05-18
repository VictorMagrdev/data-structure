import pygame
import random
from Card import Card
from Deck import Deck
from Player import Player
from Dealer import Dealer

class Game:
    def __init__(self, num_players):
        self.deck = Deck()
        self.players = [Player(i) for i in range(1, num_players+1)]
        self.dealer = Dealer()
        self.current_player_index = 0
        self.round_over = False

    def play_round(self):
        # Shuffle the deck and deal cards to players and dealer
        self.deck.shuffle()
        for i in range(2):
            for player in self.players:
                player.add_card(self.deck.draw())
            self.dealer.add_card(self.deck.draw())
        
        # Check for blackjack
        for player in self.players:
            if player.get_hand_value() == 21:
                player.set_blackjack()
                print(f"Player {player.get_id()} got blackjack!")
        
        # Player turns
        while not self.round_over:
            current_player = self.players[self.current_player_index]
            print(f"Player {current_player.get_id()}, it's your turn.")
            print(f"Your hand: {current_player.get_hand()}")
            choice = input("Do you want to hit or stand? (h/s): ")
            while choice not in ["h", "s"]:
                choice = input("Invalid choice. Do you want to hit or stand? (h/s): ")
            if choice == "h":
                current_player.add_card(self.deck.draw())
                print(f"You drew a {current_player.get_hand()[-1]}.")
                if current_player.get_hand_value() > 21:
                    current_player.set_bust()
                    print(f"Player {current_player.get_id()} has busted!")
            else:
                self.current_player_index += 1
                if self.current_player_index == len(self.players):
                    self.round_over = True
        
        # Dealer turn
        while self.dealer.get_hand_value() < 17:
            self.dealer.add_card(self.deck.draw())
            print(f"Dealer drew a {self.dealer.get_hand()[-1]}.")
        if self.dealer.get_hand_value() > 21:
            self.dealer.set_bust()
            print("Dealer has busted!")
        
        # Determine winners
        for player in self.players:
            if not player.is_bust() and not player.is_blackjack():
                if self.dealer.is_bust():
                    player.set_winner()
                    print(f"Player {player.get_id()} wins!")
                elif player.get_hand_value() > self.dealer.get_hand_value():
                    player.set_winner()
                    print(f"Player {player.get_id()} wins!")
                elif player.get_hand_value() == self.dealer.get_hand_value():
                    player.set_push()
                    print(f"Player {player.get_id()} pushed.")
                else:
                    print(f"Player {player.get_id()} loses.")
        
        # Reset players and dealer for next round
        for player in self.players:
            player.reset()
        self.dealer.reset()
        self.current_player_index = 0
        self.round_over = False
