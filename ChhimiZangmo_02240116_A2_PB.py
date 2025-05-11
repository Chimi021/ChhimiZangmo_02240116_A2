class PokemonBinder:

    def __init__(self):
        # Self Notes - Initializes an empty set to store unique Pokemon cards
        self.collected_cards = set() # set because we want to store unique values and not duplicates
        # Dictionary to store card positions {pokedex_num: (page, row, column)}
        self.card_positions = {}
        # Maximum Pokedex number
        self.max_pokedex = 1025
        
    def add_card(self, pokedex_num):
        # Add a Pokemon card to the binder if it's valid and not a duplicate
        # Returns dictionary with placement info or error message
        # 

        try:
            # Convert input to integer in case it comes as string
            pokedex_num = int(pokedex_num)
            
            # Validate Pokedex number range
            if pokedex_num < 1 or pokedex_num > self.max_pokedex:
                return {"error": f"Invalid Pokedex number. Must be between 1 and {self.max_pokedex}"}
            
            # Check for duplicate
            if pokedex_num in self.collected_cards: # This line checks if the card is already collected

                page, row, col = self.card_positions[pokedex_num] # This line retrieves the position of the card..(page row and column)
                return { # Need a dictionary and not other data types because we need to return many values 
                    "page": page,
                    "position": (row, col), 
                    "status": "Duplicate card" # 
                }
            
            # Calculate placement - cards that is placed in sequence
            # Page number calculation: (n-1)//64 + 1 (since 64 cards per page) n-1 because the first card is 1 and not 0
            # one page will have 64 cards, so the first page will have cards 1-64, second page = 65-128 etc etc.. .
            # therefore their will be 16 pages (1025/64 = 16.015625):; the last page will have 9 cards (1025-1024 = 1)
            #  SELF note - 1025 is not a multiple  of 64 but 1024 is (64*16 = 1024) ..... Therefore (pokedex_num - 1)  ** reason for -1
            page = (pokedex_num - 1) // 64 + 1  # for example for pokedex-num(100) = (100-1)//64 + 1 = page 2, 765 = (765-1)//64 + 1 = page 12
            # 64 + 1 .. the +1 in the above line is because the first page is 1 and not 0
            # Position within page (0-63)
            position_in_page = (pokedex_num - 1) % 64 # % operation gives the remainder of the division of the pokedex number by 64 so 
            # Eg - for pokedex_num(100) = (100-1)%64 == *** rough (99/64 = 1.546875) = 35 (99-64 = 35) 
            # (1-1)%64 = 0, (2-1)%64 = 1, (3-1)%64 = 2, (4-1)%64 = 3, (5-1)%64 = 4, (6-1)%64 = 5, (7-1)%64 = 6, (8-1)%64 = 7
            #
            
            # Row (1-8) and column (1-8) calculation
            row = position_in_page // 8 + 1  # 8 cards per row Eg - pokedex_num(100) = (99//8 + 1) = (99/8 = 12.375) = (12 + 1) = 13 pokedec_num(101) = (100//8 + 1) = (100/8 = 12.5) = 12 + 1 = 13
            col = position_in_page % 8 + 1    # 8 columns.. Eg - pokedex_num(100) = (99%8 + 1) = (99/8 = 12.375) = (3 + 1) = 4 pokedex_num(101) = (100%8 + 1) = (100/8 = 12.5) = 4 + 1 = 5
            
            # Store the card
            self.collected_cards.add(pokedex_num)
            self.card_positions[pokedex_num] = (page, row, col)
            
            return { # to return the position of the card in the binder
                "page": page,
                "position": (row, col),
                "status": "New card"
            }
            # Error is not a built in function but a dictionary that is used to store the error message
        except ValueError: # This line checks if the input is a number or not
            # types of errors - ValueError, TypeError, KeyError, IndexError, AttributeError, ImportError, NameError, ZeroDivisionError - this errors are called exceptions that are raised when the code is not working properly
            # Self note extar information .. had to use exceptions -- - we can name new errors as well 
            return {"error": "Pokedex number must be an integer"}

    def reset_collection(self):
        """Clear all collected cards""" # docstring - comments that wont be displayed in the output another way to add coments other than '#'
        self.collected_cards = set()
        self.card_positions = {} # Self Note - curly braccket cause i used a dictionary above.. to store data
        return "Collection has been reset. Binder is now empty."

    def get_status(self): # TO get the current status of the collection - wether complete. new or duplicate 
        """Return collection statistics"""
        total = len(self.collected_cards)
        percentage = (total / self.max_pokedex) * 100
        return { #  Displays #
            "total_cards": total,
            "percentage": round(percentage, 2), # rounds the percentage to 2 decimal places
            "is_complete": total == self.max_pokedex
        }

def main_menu_of_pokemon_card_binder():# The main menu - like Home page menu
    print("WELCOME! WELCOME! WELCOME. >u<..")
    print("This is the Pokemon Card Binder!")
    print("I collecct Pokemon card for thr Deep Pocket Monster (DPM)")
    print("Here IS what you can do here:")

    binder = PokemonBinder() # Self note - renaming so that i can call the class and its functions in the main menu
    
    while True:
        print("\nPokemon Card Binder MENU:")
        print("1. Add a Pokemon card")
        print("2. Reset binder")
        print("3. Collection Status")
        print("4. Exit Pokemon Card Binder")
        
        choice = input("What choice would you like to make? \n ^U^ Select any from (1-4) : ")
        
        if choice == "1":
            # Mode 1: Add a card    
            pokedex_num = input("Enter Pokedex number: ")
            result = binder.add_card(pokedex_num) # Binder 
            
            if "error" in result: # this is a key in the dictionary that is used to check if there is an error or not.. defined above in add_card function
                print(f"Error: {result['error']}")# result['error'] - [] brackets because it is a dictionary and we are trying to access the value of key 'error' in the dictionary
            else:
                print(f"Page: {result['page']}") # acessing data from the dictionary using the key 'page'
                print(f"Position: Row {result['position'][0]}, Column {result['position'][1]}") # similiar """"
                print(f"Status: {result['status']}")
                
                # Checking if collection is complete
                status = binder.get_status()
                if status["is_complete"]: # is_complete is a key in the dictionary defined above in get_status function
                    print("\nCONGRATULATIONSS! You've caught them all [>]U[<] !")
        
        elif choice == "2":
            # Mode 2: Reset 
            sub_choice = input("Type 'CONFIRM' to reset or 'EXIT' to return: ").upper()
            if sub_choice == "CONFIRM":
                print(binder.reset_collection())
            elif sub_choice == "EXIT":
                continue
            else:
                print("Invalid input. Please try again.")
        
        elif choice == "3":
            # Mode 3: View stats
            stats = binder.get_status()
            print(f"\nCollection Statistics:")
            print(f"Total cards: {stats['total_cards']}/{binder.max_pokedex}")
            print(f"Completion: {stats['percentage']}%")
            if stats["is_complete"]:
                print("You've caught them all!")
        
        elif choice == "4":
            # Mode 4: Exit
            stats = binder.get_status()
            print(f"\n Session Summary:")
            print(f"You collected {stats['total_cards']} Pokemon cards.")
            print("BYE BYE PEOPLE! ^._.^ ")
            break
        
        else:
            print("What you enetered is not valid.. Please enter 1 or 2 or 3 or 4.")



main_menu_of_pokemon_card_binder()