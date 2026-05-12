#|| random  module ||

import random
#* random()  0.0 ~ 1.0
print(random.random())

#* randint(a, b)  a ~ b
print(random.randint(a=10, b=15))

#* choice()  list, tuple, string
options = ["rock", "paper", "scissors"]
print(random.choice(options))

#*  shuffle()  list
cards = ["Ace", "King", "Queen", "Jack"]
random.shuffle(cards)
print(cards)