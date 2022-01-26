import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
len_list = len(names)
random_choice = random.randint(0, len_list - 1)
person_who_will_pay = names[random_choice]
print("{} is going to buy the meal today!".format(person_who_will_pay))
