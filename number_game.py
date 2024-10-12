import random

def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def divide(a,b):
    return a/b

def multiply(a,b):
    return a*b

# a = int(input("enter your first number: "))
# b = int(input("enter your second number: "))
# operator = input("what operator e.g[+,-,*,/]: ")

def math_quiz(operator):

    score = 0
    if operator == 'exit':
        return 0

    for i in range(5):

        a = random.randint(1, 10)
        b = random.randint(1, 10)

        if operator == '/' and b == 0:
            b=1
        
        if operator == '+' :
            answer = add(a,b)
            print(f"What is {a} + {b} = ?")
            user_answer = int(input("Enter your answer: "))
        elif operator == '-':
            answer = subtract(a,b)
            print(f"What is {a} - {b} = ?")
            user_answer = int(input("Enter your answer: "))
        
        elif operator == '*':
            answer = multiply(a,b)
            print(f"What is {a} * {b} = ?")
            user_answer = int(input('Enter your answer: '))
        
        elif operator == '/' :
            answer = divide(a,b)
            print(f"What is {a} / {b} = ?")
            user_answer = int(input('Enter your answer: '))
        
        if user_answer == answer:
            score += 1
            print("Correct")
        
        else:
            print(f"Sorry, that's incorrect. The correct answer was {answer}")
        

if __name__ == "__main__":

    operators = ['+', '-', '*', '/', 'exit']

    operator = input("choose an operator: ")

    if operator in operators:
        math_quiz(operator)
    else:
        print("Invalid operator. Please choose from +, -, *, /")
    # if operator == "+":
    #     print(add(a,b))

    # elif operator == "-":
    #     print(subtract(a,b))

    # elif operator == "*":
    #     print(multiply(a,b))

    # elif operator == "/":
    #     print(divide(a,b))