def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for keys in questions:
        print("----------------------------------------------")
        print(keys)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter A, B, C or D?: ").upper()
        guesses.append(guess)
        correct_guesses += check_answer(questions.get(keys), guess)
        question_num += 1

    print("-----------------------------")
    display_score(correct_guesses, guesses)



def check_answer(answer, guess):
    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0

def display_score(correct_guesses, guesses):
    print("RESULTS:")
    print(f"CORRECT GUESSES: {correct_guesses} \nYOUR GUESSES: {guesses}")
    print("CORRECT ANSWERS: ", end="")
    for keys, values in questions.items():
        print(values, end=", ")

    score = (correct_guesses/len(questions))*100
    print("Your score is " + str(score) + "%")

def play_again():
    yes_no = input("Do you want to play again (Yes or No)?: ").upper()
    if yes_no == "YES":
        return True
    else:
        return False

questions = {"Who created Python?: ": "A",
             "What year was Python created?: ": "B",
             "Who's the richest Person in the world?:": "C",
             "Is the Earth round?: ": "A"}

options = [["A.Guido Van Rossum", "B.Justin Bieber", "C.Bill Gates", "D.Mark Zuckerberg"],
           ["A.1970", "B.1991", "C.1940", "D.1920"],
           ["A.Jeff Bezos", "B.Bill Gates", "C.Elon Musk", "D.Samson Rizz"],
           ["A.Yes", "B.No", "C.Sometimes", "D.What's Earth?"]]

new_game()

while play_again():
    new_game()
print("Okay bye!")