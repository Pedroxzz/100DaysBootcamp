# Exercise 1 - Average Height
# You are going to write a program that calculates the average student height from a List of heights.

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
total_height = 0
for height in student_heights:
    total_height += height

number_std = 0
for std in student_heights:
    number_std += 1

av_height = round(total_height / number_std)
print(av_height)

