print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
n1 = name1.lower()
n2 = name2.lower()
combined_names = n1 + n2
t = combined_names.count("t")
r = combined_names.count("r")
u = combined_names.count("u")
e = combined_names.count("e")

true = t+r+u+e

l = combined_names.count("l")
o = combined_names.count("o")
v = combined_names.count("v")
e = combined_names.count("e")

love = l+o+v+e

true = str(true)
love = str(love)
love_score = true + love
love_score = int(love_score)
if love_score < 10 or love_score > 90:
    print("Your score is {}, you go together like coke and mentos.".format(love_score))
elif 40 < love_score < 50:
    print("Your score is {}, you are alright together.".format(love_score))
else:
    print("Your score is {}.".format(love_score))