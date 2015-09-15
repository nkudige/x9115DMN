"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""
from __future__ import division
from Card import *



class PokerHand(Hand):

    def suit_hist(self):
        """Builds a histogram of the suits that appear in the hand.

        Stores the result in attribute suits.
        """
        self.suits = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1
            
    def rank_hist(self):
        self.ranks = {}
        for card in self.cards:
            self.ranks[card.rank] = self.ranks.get(card.rank, 0) + 1

    def has_flush(self):
        """Returns True if the hand has a flush, False otherwise.
      
        Note that this works correctly for hands with more than 5 cards.
        """
        self.suit_hist()
        for val in self.suits.values():
            if val >= 5:
                return True
        return False
        
    def has_pair(self):
        self.rank_hist()
        for val in self.ranks.values():
            if val >= 2:
                return True
        return False
        
    def has_twopair(self):
        self.rank_hist()
        pair_count = 0
        for val in self.ranks.values():
            if val >= 2:
                pair_count += 1
        if pair_count == 2: 
            return True
        return False
    
    def has_threeofakind(self):
        self.rank_hist()
        for val in self.ranks.values():
            if val >= 3:
                return True
        return False
        
    def has_fourofakind(self):
        self.rank_hist()
        for val in self.ranks.values():
            if val >= 4:
                return True
        return False
        
    def has_fullhouse(self):
        self.rank_hist()
        twokind = False
        threekind = False
        for val in self.ranks.values():
            if val == 2:
                twokind = True
            if val == 3:
                threekind = True
        return twokind and threekind
        
    def has_straight(self):
        ranks = []
        ranks.append(self.rank_hist())
        ranks.sort()
        if ranks[0]==1:
            #appending 14 as we will be checking difference in ranks to determine presence of straight
            ranks.append(14) 
        straight_count = 0
        for i in range(len(ranks)-1):
            if(ranks[i+1]-ranks[i]==1):
                straight_count += 1
        if straight_count==5:
            return True
        return False
        
    def has_straightflush(self):
        return self.has_flush() and self.has_straight()
        
    def classify(self):
        if (self.has_straightflush()):
            return "Straight Flush"
        elif (self.has_fourofakind()):
            return "Four of a kind"
        elif (self.has_fullhouse()):
            return "Fullhouse"
        elif (self.has_flush()):
            return "Flush"
        elif (self.has_straight()):
            return "Straight"
        elif (self.has_threeofakind()):
            return "Three of a kind"
        elif (self.has_twopair()):
            return "Two pair"
        elif (self.has_pair()):
            return "Pair"
        else:
            return "Highcard"
 

def update_classification_count(classification):   
    classifications[classification] = classifications[classification]+1
    
classifications = {"Highcard":0, "Pair":0, "Two pair":0, "Three of a kind":0,
        "Four of a kind":0, "Straight":0, "Flush":0, "Fullhouse":0, "Stright Flush":0}

def print_probability_table(players, iterations):      
    probabilities = dict()
    for classification in classifications:
        probabilities[classification] = (classifications[classification]/(iterations*players))
    return probabilities
    
if __name__ == '__main__':
    
    iterations = 1000
    players = 4
    cards_per_hand = 7
    for i in range(iterations):
        deck = Deck()
        deck.shuffle()
        for i in range(players):
            poker_hand = PokerHand()
            deck.move_cards(poker_hand, cards_per_hand)
            poker_hand.sort()
            classification = poker_hand.classify()
            update_classification_count(classification)
            
    print "Classification count: "
    print classifications
    
    print "Probability table: "
    print print_probability_table(players, iterations)
    
    # make a deck
    #deck = Deck()
    #deck.shuffle()

    # deal the cards and classify the hands
    #for i in range(7):
     #   hand = PokerHand()
     #   deck.move_cards(hand, 7)
     #   hand.sort()
     #   print hand
     #   print hand.has_straight()
     #   print hand.classify()
     #   print ''
