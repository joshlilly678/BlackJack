import random
import itertools
import os
    
def clear():
    if os.name == 'nt':
        os.system('CLS')
    if os.name == 'posix':
        os.system('clear')

def createDeck():
    # Define options for cards
    rank = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    suit = ["Hearts", "Spades", "Diamonds", "Clubs"]
    # Create deck using cartesian product
    deck = list(itertools.product(rank,suit))
    # Shuffle deck
    random.shuffle(deck)
    return deck
       
def drawCard(deck, hand):
    # Take card from deck
    card = deck.pop()
    # Add card to hand
    hand.append(card)
    
def deal(deck):
    # Initialise hand
    hand = []
    # Draw 2 cards
    for i in range(2):
        drawCard(deck, hand)
    return hand
    
def checkValue(hand):
    # Initialise value of hand at zero
    val = 0
    for i in range(len(hand)):
        # Take highest value of Ace possible. 11 until bust, then 1
        if hand[i][0] == "Ace":
            if val >= 11:
                val += 1
            else:
                val += 11
        # Take face cards to have value 10
        elif hand[i][0] in ("Jack", "Queen", "King"):
            val += 10
        else:
            val += int(hand[i][0])
    return val
    
def showHand(hand):
    show = []
    for i in range(len(hand)):
        show.append(hand[i][0] + " of " + hand[i][1])
    return ', '.join(show)
    
def printHand(hand):
    show = []
    for i in range(len(hand)):
        show.append(hand[i][0] + " of " + hand[i][1])
    print("Your hand is: ", ', '.join(show))
    print("Total = ", checkValue(hand), end="\n\n")
    
def printDealerCard(hand):
    show = hand[0][0] + " of " + hand[0][1]
    print("Dealer is showing:", show, end="\n\n")
    
def getName(name):
    if name == "":
        name = input("Enter Name: ")
        clear()
        print("Welcome to BlackJack", name, end="\n\n")
        input("Click enter to continue")
        return name
    else:
        print("Lets play again " + name + "!", "\n\n")
        input("Click enter to continue")
        return name
 
def playAgain(username):
    # Ask user if they want to continue
    again = input("Do you want to play again " + username + "? (Y/N) : ").lower()
    print()
    if again == "y":
        # Play again
        game(username)
    else:
        # Thank user for playing and exit
        clear()
        print("Thanks for playing Blackjack", end="\n\n")
        print("Bye.", end="\n\n")
        exit()

def blackjack(userHand, dealerHand, username):
    # Check for blackjack. (Ace and "10"-card on deal)
    if checkValue(userHand) == 21:
        if checkValue(dealerHand) != 21:
            print("You have Blackjack!", end="\n\n")
        else:
            print("You and the dealer have Blackjack. Its a Tie")
        print("Your score:", checkValue(userHand), end="\n\n")
        print("Dealers score:", checkValue(dealerHand), end="\n\n")
        playAgain(username)
    
        
def score(userHand, dealerHand):
    # Check all possibilities for results. Print outcome of game
    if checkValue(userHand) == checkValue(dealerHand):
        printScores(dealerHand, userHand)
        print("Its a tie!\n")
    elif checkValue(userHand) == 21:
        printScores(dealerHand, userHand)
        print("Congratulations! You got a Blackjack!\n")
    elif checkValue(dealerHand) == 21:
        printScores(dealerHand, userHand)		
        print("Sorry, you lose. The dealer got a blackjack.\n")
    elif checkValue(userHand) > 21:
        printScores(dealerHand, userHand)
        print("Bust. You lose.\n")
    elif checkValue(dealerHand) > 21:
        printScores(dealerHand, userHand)			   
        print("Dealer busts. You win!\n")
    elif checkValue(userHand) < checkValue(dealerHand):
        printScores(dealerHand, userHand)
        print("Sorry. Your score isn't higher than the dealer. You lose.\n")
    elif checkValue(userHand) > checkValue(dealerHand):
        printScores(dealerHand, userHand)	
        print("Congratulations. Your score is higher than the dealer. You win\n") 

def printScores(dealerHand, userHand):
    # Print scores of user and dealer
    print("You have a " + showHand(userHand) + " for a total of " + str(checkValue(userHand)), end="\n\n")     
    print("The dealer has a " + showHand(dealerHand) + " for a total of " + str(checkValue(dealerHand)), end="\n\n")

def game(username):
    # Game loop
    clear()
    username = getName(username)
    clear()
    deck = createDeck()
    userHand = deal(deck)
    dealerHand = deal(deck)
    # Check for blackjack on initial cards
    blackjack(userHand, dealerHand, username)
    choice = ""
    while choice != "Q":
        clear()
        printHand(userHand)
        printDealerCard(dealerHand)
        choice = input("(S)tick, (T)wist or (Q)uit? (S/T/Q): ").upper()
        if choice == "S":
            clear()
            while checkValue(dealerHand) < 17:
                drawCard(deck, dealerHand)
            score(userHand, dealerHand)
            playAgain(username)
        elif choice == "T":
            clear()
            drawCard(deck, userHand)
            if checkValue(userHand) > 21:
                score(userHand, dealerHand)
                playAgain(username)
        elif choice == "Q":
            print("Bye.")
            exit()
    
if __name__ == "__main__":
    username = ""
    game(username)