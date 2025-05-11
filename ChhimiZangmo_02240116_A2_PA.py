# ASSIGNMENT 2
# PART A 
# Guess the number game

from random import randint


from random import randint

class Guess_the_Number_Game:
    def __init__(self, max_number = 100, min_number = 0):
        self.max_number = max_number    
        self.min_number = min_number
        self.target = randint (0,100)
        self.guess = []

    def verify_game(self, guess):
        if guess < self.min_number or guess > self.max_number:
            print("Your guess is out of range!")
            return False
        elif guess == self.target:
            print("Congratulations! You guessed the number!")
            return True
        elif guess < self.target:
            print("You Guessed low! Try again.")
            self.guess.append(guess)
            return False
        else:
            print("You Gussed high! Try again.")
            self.guess.append(guess)
            return False
        
    def Score(self):
        total_guesses = len(self.guess)
        valid_points = 0
        
        for guess in self.guess:
            difference = guess - self.target
            
            if difference == 0:  # Exact guess
                valid_points += 10
            elif difference <= 5:
                valid_points += 5
            elif difference <= 10:
                valid_points += 4
            elif difference <= 15:
                valid_points += 3
            elif difference <= 20:
                valid_points += 2
            elif difference <= 25:
                valid_points += 1 # No points for >25 difference
    
        final_score = valid_points - total_guesses
        return max(final_score, 0)

def play_Guess_the_Number_Game():
    print("Welcome User! You are now in the areana of Guess the Number.")
    print("You have to guess a number between 0 and 100.")
    print("You will get a score based on how close your guesses are to the target number.")
    print ("Scoring system:")
    print ("10 points for finding the target, 5 points for within 5 of target, 4 points for within 10 of target, 3 points for within 15 taget, 2 points for within 20 target, and 1 point for within 25 target range.")

    game = Guess_the_Number_Game()
    while True:
        try:
            guess = int(input("Enter your guess : "))
            if game.verify_game(guess):
                print(f"Your score is: {game.Score()}")
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

#     play_Guess_the_Number_Game()

# ROCK PAPERS SISSORS 
import random

class Rock_Paper_Sissors_Game:
    def __init__(self):
        self.player_score = 0
        self.computer_score = 0
        
    def _computers_weapon(self):
        self.computer = random.choice(["Rock", "Paper", "Scissor"])
        return self.computer
    
    def _player_weapon(self):
        self.Player_Weapon = input("Choose Your Weapon:")
        return self.Player_Weapon
    
    def competing(self):
        if self.Player_Weapon == self.computer:
            self.player_score += 1  # A score for lost energy..
            self.computer_score += 1 # self note - the scores have to be above the print statement or it jumps to the last else statement
            print(f"My weapon{self.Player_Weapon} and your weapon {self.computer} clashes .. Its a Tie! >_<")
            # self.computer_score += 1
            # self.player_score += 1 # Type 'Rock' or 'Paper' or 'Sissors' Check for the spellling correctness of your measly weapon.. Or type 'Quit' to exit.
        elif self.Player_Weapon == "Rock" and self.computer == "Paper":
            self.computer_score += 1
            print(f"My weapon, {self.computer} defeats Your weapon {self.Player_Weapon}.. You lose ^u^ .. Hohoho >o<")
        elif self.Player_Weapon == "Rock" and self.computer == "Scissor":
            self.player_score += 1
            print(f"Your weapon {self.Player_Weapon} defeats My weapon, {self.computer}.. You win! -_-.. Just you wait..")
        elif self.Player_Weapon == "Paper" and self.computer == "Rock":
            self.player_score += 1
            print(f"Your weapon {self.Player_Weapon} defeats My weapon, {self.computer}.. You win! -_-.. Just you wait..")
        elif self.Player_Weapon == "Paper" and self.computer == "Scissor":
            print(f"My weapon {self.computer} defeats Your weapon {self.Player_Weapon}.. You lose ^u^.. Hehe")
            self.computer_score += 1
        elif self.Player_Weapon == "Scissor" and self.computer == "Rock":
            self.computer_score += 1
            print(f"My weapon {self.computer} defeats Your weapon {self.Player_Weapon}.. You lose ^u^..Well Look at a human competing with a machine.. Heh ")  
        elif self.Player_Weapon == "Scissor" and self.computer == "Paper": 
            self.player_score += 1
            print (f"Your weapon {self.Player_Weapon} defeats My weapon, {self.computer}.. You win! -_-.. Luck huh 0_0..")
        else:
            print("Type 'Rock' or 'Paper' or 'Scissor' Check for the spellling correctness of your weapon.. Or type 'Quit' to exit.")
    
    def score_calculating(self):
        print("\n--- Score Board ---") # SELF note - \n is used for new line
        print(f"Your Score: {self.player_score}")
        print(f"My Score: {self.computer_score}")
        if self.player_score > self.computer_score:
            print("You're leading! But don't get too comfortable...")
        elif self.player_score < self.computer_score:
            print("I'm winning! As expected from superior AI!")
        else:
            print("We are Tied ^.0 and The battle continues...")
        print("-------------------\n")
    
    def play_game(self):
        print("Welcome to Rock-Paper-Scissors Battle!")
        print("Prepare to be defeated by my superior algorithms!\n")
        print("Each of us 0.< (You and Me) have three weapons to choose from 'Rock', 'Paper', 'Sissor'")
        print("You can raise a WHITE FLAG (type - WF) to give up.. 0.0 \nOr it is an endless Battel!")
        print("Our Battel Now Beggins!")
        
        while True:
            self._computers_weapon()
            player_choice = self._player_weapon()
            
            if player_choice in ("WF","wf") :
                print("\nFinal Scores:")
                self.score_calculating()
                print("Thanks for playing! Run away while you still can!")
                break
                
            if player_choice not in ["Rock", "Paper", "Scissor"]:
                print("Invalid choice! Try again.\n")
                continue
                
            print(f"\nYou chose: {player_choice}")
            print(f"I chose: {self.computer}")
            
            self.competing()
            self.score_calculating()
            
#game.play_game()

#TRIVIA PURSUIT QUIZ GAME
import random

class Question:
    """
    Represents a single question in the quiz.

    Attributes:
        Type (str): The category or type of the question.
        question (str): The question text.
        User_choice (list): A list of multiple-choice options (A, B, C, D).
        right_answer (str): The correct answer for the question.
    """
    def __init__(self, Type, question, User_choice, right_answer):
        """
        Initializes a Question object with its type, question, choices, and correct answer.

        Argument.. -- Args :
            Type (str): The category or type of the question.
            question (str): The question text.
            User_choice (list): A list of multiple-choice options.
            right_answer (str): The correct answer for the question.
        """
        self.Type = Type
        self.question = question
        self.User_choice = User_choice
        self.right_answer = right_answer

    def ask_question(self):
        """
        Displays the question and its multiple-choice options to the user.
        """
        print(f"\nCategory: {self.Type}")
        print(f"Question: {self.question}")
        for option in self.User_choice:
            print(option)

    def check_answer(self, user_answer):
        """
        Checks if the user's answer is correct.

        Args:
            user_answer (str): The user's selected answer (A, B, C, or D).

        Returns:
            bool: True if the user's answer is correct, False otherwise.
        """
        return user_answer.upper() == self.right_answer.upper()


class Quiz:
    """
    Represents a quiz containing multiple questions.

    Attributes:
        questions (list): A list of Question objects.
        score (int): The user's score for the quiz.
    """
    def __init__(self, questions):
        """
        Initializes a Quiz object with a list of questions.

        Args:
            questions (list): A list of Question objects.
        """
        self.questions = questions
        self.score = 0

    def start_quiz(self):
        """
        Starts the quiz, asks each question, and calculates the user's score.
        """
        for question in self.questions:
            question.ask_question()
            user_answer = input("Your answer (A/B/C/D): ").strip().upper()

            if question.check_answer(user_answer):
                print("Correct!")
                self.score += 1
            else:
                print(f"Wrong! The correct answer was {question.right_answer}.")

        print(f"\nQuiz ended! Your score: {self.score}/{len(self.questions)}")
        return self.score

class Game:
    """
    Represents the Trivia Pursuit game with multiple quizzes.

    Attributes:
        quizzes (dict): A dictionary of quizzes categorized by type.
    """
    def __init__(self):
        """
        Initializes a Game object with an empty dictionary of quizzes.
        """
        self.quizzes = {}

    def add_quiz(self, Type, questions):
        """
        Adds a quiz to the game.

        Args:
            Type (str): The category or type of the quiz.
            questions (list): A list of Question objects for the quiz.
        """
        self.quizzes[Type] = Quiz(questions)

    def start_game(self):
        print("Welcome to Trivia Pursuit!")
        print("Available categories:")

        for category in self.quizzes.keys():
            print(f"- {category}")

        selected_category = input("Choose a category: ").strip()

        if selected_category in self.quizzes:
            print(f"\nStarting {selected_category} quiz...")
            self.quizzes[selected_category].start_quiz()
        else:
            print("Invalid category. Please try again.")


# ===== Sample Questions =====
stupid_questions = [
    Question("Stupid", "Who is the most beautiful..?", ["A. The developer", "B. You", "C. Snow white", "D. Your crush"], "A"),
    Question("Stupid", "What did you not do today?", ["A. Open your eyes", "B. Breathe", "C. Smile", "D. Move"], "C"),
    Question("Stupid", "What are the dumbest reasons to be born?", ["A. Your mother wanted to carry have back pain for 9 months and a life long emotional damege", "B. God had too much of your stupidity", "C. To increase population and pollution", "D.To die of cancer at 2 "], "B")
]

serious_questions = [
    Question("Serious", "You have no choice but to choose, so if you had a gun in your hand \npointed at two of the most precious people in your life. Who will you unalive?", ["A. The first face that flashed in your mind when you read the question", "B. The second face", "C. Yourself", "D. All"], "D"),
    Question("Serious", "Where do you see yourself after 5 years?", ["A. Pokto", "B. With your dream job", "C. Still lingering", "D. Outcountry"], "A"),
    Question("Serious", "What is the meaning of life?", ["A. Helping others", "B. Finding Happiness", "C. You have no idea", "D. To die"], "C")
]

#     game = Game()
#     game.add_quiz("Stupid", stupid_questions)
#     game.add_quiz("Serious", serious_questions)S
#     game.start_game()


class Checking_current_overall_score:
    def __init__(self):
        self.guess_game_score = 0
        self.rps_game_score = 0
        self.trivia_score = 0

    def update_guess_game_score(self, score):
        self.guess_game_score = score

    def update_rps_game_score(self, player_score):
        self.rps_game_score = player_score

    def update_trivia_quiz_score(self, score):
        self.trivia_quiz_score = score

    def calculate_overall_score(self):
        overall_score = self.guess_game_score + self.rps_game_score + self.trivia_score
        return overall_score

    def display_overall_score(self):
        print("\n--- Overall Score ---")
        print(f"Guess the Number Game Score: {self.guess_game_score}")
        print(f"Rock-Paper-Scissors Game Score: {self.rps_game_score}")
        print(f"Trivia Pursuit Game Score: {self.trivia_score}")
        print(f"Total Overall Score: {self.calculate_overall_score()}")
        print("---------------------\n")





class Menu:
    def __init__(self):
        self.options = {
            "1": "Play Guess the Number Game",
            "2": "Play Rock-Paper-Scissors Game",
            "3": "Try Quizes in Trivia Pursuit Game",
            "4": "Check Current Overall Score",
            "5": "Pokememon Python Card Card",
            "6": "EXIT"
        }
        self.score_tracker = Checking_current_overall_score() 
    def display_menu(self):
        while True:
            print("\n--- Main Menu ---")
            print("Hello Plyer! ^U^ What game would you like to play choose from the options below.. >U< ")
            for key, value in self.options.items(): # 
                print(f"{key}. {value}")

            user_option = input("ENTER YOUR OPTION:")
            if user_option == "1":
                play_Guess_the_Number_Game()
                game = Guess_the_Number_Game()
                self.score_tracker.update_guess_game_score(game.Score())
            elif user_option == "2":
                game = Rock_Paper_Sissors_Game()
                game.play_game()
                self.score_tracker.update_rps_game_score(game.player_score)
            elif user_option == "3":
                game = Game()
                game.add_quiz("Stupid", stupid_questions) 
                game.add_quiz("Serious", serious_questions)  
                game.start_game()
                self.score_tracker.update_trivia_quiz_score(game.quizzes[game.start_game()].score)#AI borrowed .. REAlly didnt know how to do this sir..
            
            elif user_option == "4":
                self.score_tracker.display_overall_score() 
            elif user_option == "5":
                print ("The Pokemon Card Binder is in PART B.. 0U0 ")
                continue
            elif user_option == "6":
                print("Byeeeee Byee.. I'll miss you T.T")
                break

            else:
                print ("Their seems to be an error.. Please recheck your options.. ")

            play_again =  input("Would you like to Play again? (Y/N): ")
            if play_again == 'Y' :
                continue #
            elif play_again == 'N':
                print("BYE BYE... ^U^")
                break 
            else:
                print("Invalid input. Please enter just the letter 'Y' or 'N'.")
        
menu = Menu()
menu.display_menu()
