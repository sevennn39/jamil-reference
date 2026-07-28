print("Hello! Welcome to 37039!")
print("Options: High Card, Low Card, Coin Flip, Fun Facts, Quiz, Predictions")
choice = input("Choose one! (type exactly as written above) ")

if choice == "Quiz": 
        print("You have chosen Quiz!")
        totalscore = 0

        questionone = input("What is the capital of Australia? ")
        if questionone == "Canberra": 
                print ("Correct!") 
                totalscore += 1
        if questionone == "canberra": 
                print("Correct!") 
                totalscore += 1

        questiontwo = input("What is 12 x 29? ")
        if questiontwo == "348": 
                print("Correct!") 
                totalscore += 1

        questionthree = input("What is the powerhouse of the cell? ")
        if questionthree == "Mitochondria": 
                print("Correct!") 
                totalscore += 1
        if questionthree == "mitochondria": 
                print("Correct!") 
                totalscore += 1

        print("This is the end of the quiz!")
        print(f"Total Score: {totalscore}")
        print("Rerun the project to play something else!")

if choice == "High Card, Low Card": 
        print("You have chosen High Card, Low Card!")
        import random
        num = random.randint(1, 12)
        print([num])
        input ("Will the next number be higher or lower? ")
        other = random.randint(1, 12)
        if num < other:
            print(f"It was higher! [{other}]")
        if num > other:
            print(f"It was lower! [{other}]")

if choice == "Coin Flip": 
        print("You have chosen Coin Flip!")
        import random
        num = random.randint (1,2)
        if num == 1: print("Heads!")
        if num == 2: print("Tails!")

if choice == "Fun Facts": 
        print("You have chosen Fun Facts!")
        fun_facts = ["Cat urine glows under a blacklight.","A shrimp's heart is in its head.", "Dreamt is the only English word that ends in the letters mt.", "A dime has 118 ridges around the edge.", "A crocodile cannot stick its tongue out.", "The 'sixth sick sheik's sixth sheep's sick' is believed to be the toughest tongue twister in the English language."]
        import random
        facts = random.choice(fun_facts)

        print(f"Your fact is: {facts}")

if choice == "Predictions":
        print("You have chosen Predictions! Here's how your day will go today: ")
        predict = ["You'll have a great day!", "Someone will derail your plans...", "Things won't work out how you think.", "You may end up tired by the end of the day.", "It'll just be a day.", "You may run into some issues."]
        import random
        pchan = random.choice(predict)
        print(pchan)