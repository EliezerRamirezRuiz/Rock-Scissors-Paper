import random


options = ["Rock", "Scissors", "Paper"]

def check_input(var) -> bool:
    if var not in options:
        return False
    else:
        return True


def random_option():
    return random.choice(options)
        

def game(answer:str):
    option = random_option()
    if check_input(answer):
        if answer == option:
                print('Empate')
        elif answer != option:
            if answer == 'Rock' and option == 'Scissors':
                print(f'{answer} vs {option}: you win')
        
            elif answer == 'Rock' and option == 'Paper':
                print(f'{answer} vs {option}: you lost')
        
            elif answer == 'Scissors' and option == 'Rock':
                print(f'{answer} vs {option}: you lost')
        
            elif answer == 'Scissors' and option == 'Paper':
                print(f'{answer} vs {option}: you win')
        
            elif answer == 'Paper' and option == 'Rock':
                print(f'{answer} vs {option}: you win')
        
            elif answer == 'Paper' and option == 'Scissors':
                print(f'{answer} vs {option}: you lost')

        else:
            print(f"Option not available")
    

if __name__ == '__main__':
    flag =True
    while flag:
        answer = input('Rock, Paper and Scissors:').capitalize()
        try:
            if answer == 'Exit':
                flag = False
                break
            else:
                game(answer)
        except Exception as error:
            print(f'Error: {error}')

