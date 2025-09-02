import random, json

def questions(filename = "quiz_list.json"):
    with open(filename, "r") as f:
        return json.load(f)
    

def do_quiz():
    while True:
        all_questions = questions()
        shuffled_quetions = all_questions.copy()
        random.shuffle(shuffled_quetions)
        score = 0

        print("Rules: Only enter the letter you choose or Type 'exit' to back to menu")

        for random_question in shuffled_quetions[:10]:
            print(random_question["question"])
            for key , value in random_question["options"].items():
                print(f"{key}: {value}")

            answer = input("Answer: ").lower()

            if answer == "exit":
                return

            if answer == random_question["answer"]:
                print("✅correct")
                score += 1

            else:
                print(f"❌wrong. Correct answer is {random_question['answer']}") 
            
        print(f'/nCongratulations! Your score is {score}/10')

        choice = input("Click 'enter' to do it again or type 'exit' to back to menu?").lower()

        if choice == "exit":
            break    

def add_quiz():
    while True:    
        print("Add questions")

        new_question = input("Enter your Question: ")
        option_a = input("Enter option a: ") 
        option_b = input("Enter option b: ") 
        option_c = input("Enter option c: ") 
        option_d = input("Enter option d: ") 
        correct_answer = input("Correct answer: ").lower()

        question_dict = {
            "question": new_question,
            "options": {"a": option_a, "b": option_b, "c": option_c, "d": option_d},
            "answer": correct_answer
        }

        all_questions = questions()
        all_questions.append(question_dict)

        with open("quiz_list.json", "w") as f:
            json.dump(all_questions, f, indent=4)
        
        print("✅ Question is saved successfully")
        choice = input("Type '+' to add another question or 'exit' to back to menu").lower()

        if choice == "exit":
            break

def main():
    while True:
        print("-" * 40)
        print("Welcome to mad quiz")
        print("-" * 40)
        print("1. Do the Quiz")
        print("2. Add Quiz")
        print("3. Exit")

        choice = input("Please choose the option: ")

        if choice == "1":
            do_quiz()
        
        elif choice == "2":
            add_quiz()

        elif choice == "3":
            print("Thanks for choosing us...")
            break
        else:
            print("Please enter option")

if __name__ == "__main__":
    main()