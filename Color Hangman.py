from random import shuffle

colors = 'R B G Y V W O P'.split(" ")
shuffle(colors)

chosenCode = "".join(colors[:4])
n = int(input("Enter number of tries ==> "))

won = False

for _ in range(n):
    userGuess = input("Enter Guess ==> ").upper()

    correctPosition = 0
    incorrectPosition = 0

    for c in userGuess:
        if c in chosenCode:
            incorrectPosition += 1

    for i, c in enumerate(userGuess):
        if c == chosenCode[i]:
            correctPosition += 1
            incorrectPosition -= 1
    if correctPosition == 4:
        won = True
        break
    print(f"({correctPosition}, {incorrectPosition})")
if won:
    print("You win!")
else:
    print("You lose!")
x = input()
