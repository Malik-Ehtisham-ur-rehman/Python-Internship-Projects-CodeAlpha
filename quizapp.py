class Question:
    def __init__(self, text, choices, correct_answer):
        self.text = text
        self.choices = choices
        self.correct_answer = correct_answer

    def is_correct(self, user_answer):
        return user_answer == self.correct_answer

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def take_quiz(self):
        for question in self.questions:
            print(question.text)
            for index, choice in enumerate(question.choices, start=1):
                print(f"{index}. {choice}")
            
            user_answer = int(input("Enter the number of your answer: ")) - 1
            if 0 <= user_answer < len(question.choices):
                if question.is_correct(user_answer):
                    print("Correct!\n")
                    self.score += 1
                else:
                    print(f"Wrong! The correct answer was: {question.choices[question.correct_answer]}\n")
            else:
                print("Invalid choice. Skipping this question.\n")

    def display_score(self):
        print(f"Your score: {self.score}/{len(self.questions)}")

def main():
    # Create questions
    question1 = Question("What is the capital of France?", ["Paris", "London", "Berlin", "Madrid"], 0)
    question2 = Question("What is 2 + 2?", ["3", "4", "5", "6"], 1)
    question3 = Question("Which planet is known as the Red Planet?", ["Earth", "Mars", "Venus", "Jupiter"], 1)

    # Create a quiz
    quiz = Quiz([question1, question2, question3])

    # Take the quiz
    print("Welcome to the Quiz Application!")
    quiz.take_quiz()

    # Display the score
    quiz.display_score()

if __name__ == "__main__":
    main()
print("hello devops sample")
