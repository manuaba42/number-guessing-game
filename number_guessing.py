import random
logo = '''
  ________                            .__                   ________                       
 /  _____/ __ __   ____   ______ _____|__| ____    ____    /  _____/_____    _____   ____  
/   \  ___|  |  \_/ __ \ /  ___//  ___/  |/    \  / ___\  /   \  ___\__  \  /     \_/ __ \ 
\    \_\  \  |  /\  ___/ \___ \ \___ \|  |   |  \/ /_/  > \    \_\  \/ __ \|  Y Y  \  ___/ 
 \______  /____/  \___  >____  >____  >__|___|  /\___  /   \______  (____  /__|_|  /\___  >
        \/            \/     \/     \/        \//_____/           \/     \/      \/     \/ 
'''

print(logo)
print('Welcome to number guessing game !!')
print("I'm thinking of a number between 1 to 100")
randoNumber = random.randint(1,100)
level = input("Choose dificulity, type 'easy' or 'hard': ")
if level == 'easy':
    guess = 10
    print("You have 10 attempts to guess the number")
else:
    guess = 5
    print("You have 5 attempts to guess the number")

iteration = guess
for i in range(0,guess):
    guess = int(input("Make a guess: "))
    if guess > randoNumber:
        print("Too High")
    elif guess < randoNumber:
        print("Too Low")
    else:
        print("You're Right!!")
        break
    iteration -= 1
    if iteration == 0:
        print("You Lose")
    else:
        print(f"You have {iteration} attempts left")
