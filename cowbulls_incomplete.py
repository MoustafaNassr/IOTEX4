import random

print("Let's play a game of Cowbull!",
    "\nI will generate a number, and you have to guess the numbers one digit at a time.",
    "\nFor every number that exists in the sequence but is in wrong place, you get a cow. For every one in the right place, you get a bull.",
    "\nThe game ends when you get 4 bulls!",
    "\nType exit at any prompt to exit." ) #explanation

#gotta play the game
playing = True


# Returns list of digits  of a number

def LiOfDigit(num):
    return [int(i) for i in str(num)]

generateNum = random.randint(1000, 9999)
print(generateNum)

# Returns number of bulls and ows

def BullsAndCows(num, guess):
    bull_cow = [0, 0]
    num_li = LiOfDigit(num)
    guess_li = LiOfDigit(guess)
    for i, j in zip(num_li, guess_li):
        if j in num_li:
            if j == i:
                bull_cow[0] += 1
            else:
                bull_cow[1] += 1
    return bull_cow



while playing == True:
    guess = input("Enter your guess: ")
    if guess == "exit":
        break
    bull_cow = BullsAndCows(generateNum, guess)
    print(f"{bull_cow[0]} bulls, {bull_cow[1]} cows")
    if bull_cow[0] == 4:
        print("You guessed right!")
        break
else:
    print(f"You ran out of tries. Number was {generateNum}")

