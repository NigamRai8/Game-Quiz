print("     WELCOME TO QUIZ GAME")

name = input("Enter your name: ")
print(f"\nHello {name}! Best of Luck.\n")

score = 0

# Question 1
print("Q1. Who developed Python?")
print("A. James Gosling")
print("B. Guido van Rossum")
print("C. Dennis Ritchie")
print("D. Bjarne Stroustrup")
ans = input("Enter your option: ")

if ans == "B":
    print("Correct\n")
    score += 1
else:
    print("Wrong\n")
    score -= 0.4

# Question 2
print("Q2. In which year was Python first released?")
print("A. 1989")
print("B. 1995")
print("C. 1991")
print("D. 2000")
ans = input("Enter your option: ")

if ans == "C":
    print("Correct\n")
    score += 1
else:
    print("Wrong\n")
    score -= 0.4

# Question 3
print("Q3. Python file extension?")
print("A. .java")
print("B. .cpp")
print("C. .py")
print("D. .html")
ans = input("Enter your option: ")

if ans == "C":
    print("Correct\n")
    score += 1
else:
    print("Wrong\n")
    score -= 0.4

# Question 4
print("Q4. 5 + 7 = ?")
print("A. 10")
print("B. 12")
print("C. 14")
print("D. 15")
ans = input("Enter your option: ")

if ans == "B":
    print("Correct\n")
    score += 1
else:
    print("Wrong\n")
    score -= 0.4

# Question 5
print("Q5. List uses which bracket?")
print("A. []")
print("B. {}")
print("C. ()")
print("D. <>")
ans = input("Enter your option: ")

if ans == "A":
    print("Correct\n")
    score += 1
else:
    print("Wrong\n")
    score -= 0.4

# Question 6
print("Q6. Which function takes input?")
print("A. print()")
print("B. display()")
print("C. scan()")
print("D. input()")
ans = input("Enter your option: ")

if ans == "D":
    print("Correct\n")
    score += 1
else:
    print("Wrong\n")
    score -= 0.4

# Question 7
print("Q7. Which keyword is used to create a function in Python?")
print("A. def")
print("B. function")
print("C. fun")
print("D. define")
ans = input("Enter your option: ")

if ans == "A":
    print("Correct\n")
    score += 1
else:
    print("Wrong\n")
    score -= 0.4

# Question 8
print("Q8. Which symbol is used for comments in Python?")
print("A. //")
print("B. /* */")
print("C. #")
print("D. <!-- -->")
ans = input("Enter your option: ")

if ans == "C":
    print("Correct\n")
    score += 1
else:
    print("Wrong\n")
    score -= 0.4

# Question 9
print("Q9. Which data type stores True or False?")
print("A. int")
print("B. bool")
print("C. float")
print("D. str")
ans = input("Enter your option: ")

if ans == "B":
    print("Correct\n")
    score += 1
else:
    print("Wrong\n")
    score -= 0.4

# Question 10
print("Q10. Which company developed Windows?")
print("A. Microsoft")
print("B. Google")
print("C. Apple")
print("D. IBM")
ans = input("Enter your option: ")

if ans == "A":
    print("Correct\n")
    score += 1
else:
    print("Wrong\n")
    score -= 0.4


print("           QUIZ FINISHED")


print(f"{name}, Your Final Score = {score}")

if score == 10:
    print("Outstanding! Perfect Score.")
elif score >= 8:
    print("Excellent")
elif score >= 5:
    print("Average")
else:
    print("Fail")