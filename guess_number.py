secret_number = 777

# print(
# """
# +================================+
# | Welcome to my game, muggle!    |
# | Enter an integer number        |
# | and guess what number I've     |
# | picked for you.                |
# | So, what is the secret number? |
# +================================+
# """)
number = int(input("enter your guess number: "))
while number > 0:
    if number != secret_number:
        print("Ha ha! You're stuck in my loop!")
    elif number == secret_number:
        print("Well done, muggle! You are free now")
    number = int(input("enter your guess number: "))
