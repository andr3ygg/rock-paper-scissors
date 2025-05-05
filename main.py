# Rock beats Scissors
# Scissors beats paper
# Paper beats Rock
# Elección del usuario
# Elección aleatoria de la maquina
# User_Prompt => 1-3
# Machine_Prompt (Random)
# 3 Opciones => 1, 2, 3 => Randint
# Verificar ganador
# Mostrar resultado
# user = 1 => rock. If machine_prompt == jugadas[1] (scissors)
# then gana user, else pierde
from random import choice


def welcome():
    mensaje = "1 -> Piedra|| 2 -> Papel|| 3 -> Tijera"
    return mensaje


def user_prompt(plays):
    election_user = input("Elije  ")

    if election_user in plays:
        return election_user
    elif election_user.isnumeric():
        index = int(election_user) - 1
        if index < len(plays):
            return plays[index]
    else:
        election_user = election_user.capitalize()


def machine_prompt(plays):
    election_machine = choice(plays)
    return election_machine


def win(first, second, plays, winners):
    index_play = plays.index(first)
    return second in winners[index_play]


def main():
    plays = [
        "Rock",
        "Paper",
        "Scissors",
    ]
    winners = [
        ["Scissors"],
        ["Rock"],
        ["Paper"]
    ]
    message = welcome()
    user_input = user_prompt(plays)
    print(user_input)
    machine = machine_prompt(plays)
    print(machine)

    if user_input == machine:
        print("Empate")
        # return 0
    elif win(user_input, machine, plays, winners):
        print("Gana jugador 1")
        # return 1
    else:
        print("Gana maquina")
        # return -1


if __name__ == '__main__':
    main()