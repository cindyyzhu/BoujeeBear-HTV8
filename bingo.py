import random
#arry

# List of Bingo words
bingo_words = [
    "bl",
    "cl",
    "th",
    "ch",
    "nt",
    "gl",
    "st",
    "wh",
    "ng",
]

# Function to create a random Bingo card
def create_bingo_card(words):
    random.shuffle(words)
    card = [words.pop() for _ in range(9)]
    return [card[i:i+3] for i in range(0, 9, 3)]

# Function to display a Bingo card
def display_bingo_card(card):
    print("\nBINGO CARD")
    for row in card:
        print(" | ".join(row))
        print("-" * 18)

# Function to check if a Bingo card is a winning card
def is_winning_card(card):
    for row in card:
        if all(word == "X" for word in row):
            return True
    for col in range(3):
        if all(card[row][col] == "X" for row in range(3)):
            return True
    if all(card[i][i] == "X" for i in range(3)) or all(card[i][2-i] == "X" for i in range(3)):
        return True
    return False

# Main game loop
bingo_card = create_bingo_card(bingo_words)
display_bingo_card(bingo_card)



print("Thanks for playing Bingo!")
