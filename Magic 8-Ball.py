import random
from tracemalloc import stop

name = input("what is your name: ")
question = input("Yes or No question: ")
answer = ""
random_number = random.randint(1,9)

if random_number == 1 : answer = "Yes - Definitley."
elif random_number == 2 : answer = "It is decidely so."
elif random_number == 3 : answer = "Without a doubt."
elif random_number == 4 : answer = "Reply hazy, try again."
elif random_number == 5 : answer = "Ask again later."
elif random_number == 6 : answer = "Better not tell you now."
elif random_number == 7 : answer = "My sources say no."
elif random_number == 8 : answer = "Out look not so good."
elif random_number == 9 : answer = "Very doubtful."
else : "Error"

if question == "":
    print("No Question Given")
else:

    if name != "":
        print(name + " asks: " + question)
        print("Magic 8-Ball's answer: " + answer )

    else:
        print(question)
        print("Magic 8-Ball's answer: " + answer )