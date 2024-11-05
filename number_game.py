import random

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def divide(a, b):
    return a / b

def multiply(a, b):
    return a * b

def math_quiz(operator, user_answers):
    score = 0
    questions = []
    for i in range(5):
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        if operator == '/' and b == 0:
            b = 1

        if operator == '+':
            answer = add(a, b)
        elif operator == '-':
            answer = subtract(a, b)
        elif operator == '*':
            answer = multiply(a, b)
        elif operator == '/':
            answer = divide(a, b)
        
        questions.append((a, b, answer))

        if i < len(user_answers) and user_answers[i] == answer:
            score += 1

    return score, questions
