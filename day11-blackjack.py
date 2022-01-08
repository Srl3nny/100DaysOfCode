import random

logo = """    
.------.            _     _            _    _            _        
|A_  _ |.          | |   | |          | |  (_)          | |       
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __    
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /    
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   <     
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\    
      |  \/ K|                            _/ |                    
      `------'                           |__/               
""" 

# The deck is unlimited in size
#there are no jockers
#the Jack/Quenn/King all count 10
#The ace can count as 11 or 1
#Use the following list as deck of cards
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10 ]
#the cards in the list have equal probability of being drawn
#the computer is the dealer

def deal_card():
    """Return cards from deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10 ]
    card = random.choice(cards)
    return card

def compare(user_score, computer_score):
    """Compare and find the winner"""
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "You lose, computer has Blackjack"
    elif user_score == 0:
        return "you win with a Blackjack"
    elif user_score > 21:
        return "You went over and lose"
    elif computer_score > 21:
        return "You win, computer went over"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"

def calculator_score(cards):
    """Check for blackjack and return 0 that is blackjack or return the sum"""
    if sum(cards) == 21 and len(cards):
        return 0
    #if the score is already over 21, replace 11 by 1
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

#Deal the cards using deal_cards function
user_cards = []
computer_cards = []
is_game_over = False
print(logo)
for i in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

while not is_game_over:
    user_score = calculator_score(user_cards)
    computer_score = calculator_score(computer_cards)

    print(f"Your cards: {user_cards}, current score: {user_score}\n")
    print(f"computer's first card is: {computer_cards[0]}\n")
    
    #check if has blackjack or user is over 21
    if user_score == 0 or computer_score == 0 or user_score > 21:
        is_game_over = True
    else:
        user_shoud_deal = input("Type 'y' tp another card and 'n' to pass\n")
        if user_shoud_deal == 'y':
            user_cards.append(deal_card())
        else:
            is_game_over = True

while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculator_score(computer_cards)

print(f"Computer score {computer_score} and computer cards {computer_cards}\n")
print(f"User score {user_score} and user cards {user_cards}\n")


print(compare(user_score, computer_score))

