def start_game():
    print("Pomysl liczbe od 0 do 1000 a ja ja zgadne w max. 10 probach")
    print("Enter aby kontynuowac")
    input()

def draw_lottery():
    while True:
        start_game()
        min = 0
        max = 1000
        guess = int((max-min) / 2) + min
        print(f"Zgaduję: {guess}")
        control_number = 10
        chosen = [guess]
        while len(chosen) < 11:
            user_choice = input("napisz: za duzo, za malo, zgadles: ")
            if user_choice == 'za duzo':
                max = guess

                guess = int((max - min) / 2) + min
                chosen.append(guess)
                print(f"Zgaduję: {guess}")

            elif user_choice == 'za malo':
                min = guess
                guess = int((max - min) / 2) + min
                chosen.append(guess)
                print(f"Zgaduję: {guess}")
            elif user_choice == 'zgadles':
                return "wygralem!"
        print("nie oszukuj!")

print(draw_lottery())
