
from random import randint

game_running = True


def calculate_monster_attack():
    return randint(monster['attack_min'], monster['attack_max'])

def game_ends(winner_name):
    print(f'{winner_name} won the game')




while game_running:
    new_round = True
    player = {'name': 'Faisal', 'attack': 13, 'heal': 16, 'health': 100}
    monster = {'name': 'Max', 'attack_min': 10,'attack_max':20 ,'health': 100}

    print('---' * 7)
    print('Enter Player name:')
    player['name'] = input()

    print('---' * 7)
    print(player['name'] + ' has ' + str(player['health']) + '% health')
    print(monster['name'] + ' has ' + str(monster['health']) + '% health')
    while new_round:

        player_won = False
        monster_won = False

        print('---' * 7)
        print('Please Select action')
        print('1. Attack')
        print('2. Heal')
        print('3. Exit Game')

        player_choice = int(input())  # type casting


        if player_choice == 1:
            monster['health'] = monster['health'] - player['attack']
            if monster['health'] <= 0:
                player_won = True
            else:

                player['health'] = player['health'] - calculate_monster_attack()
                if player['health'] <= 0:
                    monster_won = True

        elif player_choice == 2:
            player['health'] = player['health'] + player['heal']

            player['health'] = player['health'] -  calculate_monster_attack()

            if player['health'] <= 0:
                monster_won = True

        elif player_choice== 3:
            new_round = False
            game_running = False
        else:
            print("Invalid Input")

        if player_won == False and monster_won == False:
            print(player['name'] + ' has ' +  str(player['health']) + '% life left')
            print(monster['name'] + ' has ' + str(monster['health']) + '% life left')

        elif player_won:
            game_ends(player['name'])
            new_round = False
        elif monster_won:
            game_ends(monster['name'])
            new_round = False


