import random
digits=list("123456789")
random.shuffle(digits)
secret=''.join(digits[:4])

print("Welcome to Bulls and Cows!")
print("The game's gonna generate a 4-digit number from 1 to 9")
print("Try to guess! type 'exit' to quit \n")

while True:
    guess=input("Enter your guess:")
    if guess == 'exit':
        print(f"The number was {secret}. BYEEE!")
        break

    if len(guess)!=4 or not guess.isdigit() or '0' in guess or len(set(guess))!=4:
        print("Invalid guess.Mkae sure to enter a 4 unique digits from 1 to 9.")
        continue
    if guess==secret:
        print("YAYYY! You got it right!")
        break

    bulls=sum(guess[i]==secret[i] for i in range(4))
    cows=sum(guess[i] in secret and guess[i]!=secret[i] for i in range(4))

    print(f"{bulls} Bulls,{cows} Cows")