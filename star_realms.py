def main(input_function, print_function):
    # set players' intial scores to 50
    player_one_score = 50
    player_two_score = 50

    # start round one and prompt player 1 for damage against player 2
    print_function("Player one - Round one")
    # request input for damage against player 2
    print_function("Enter damage against Player 2 ")

    # set variable 'damage' input
    damage_against_player_2 = input_function()
    # calculate player 2 new score
    sum1 = float(player_two_score) - float(damage_against_player_2)
    # update variable player_two_score
    player_two_score = sum1

    # print player 2 current score
    print_function('Player 2 current score: ' + format(sum1))

    # request input for player 1 healing
    print_function("Enter Player 1 healing")

    # set variable 'player_one_healing' to input
    player_one_healing = input_function()
    sum2 = float(player_one_score + float(player_one_healing))

    player_one_score = sum2

    print_function("Player one current score: " + format(sum2))
    print_function("End of Player one -  Round one")

    damage_against_player_2 = 0
    player_one_healing = 0

    # End of Player one Round one

    # print PLayer two Round one
    print_function("Player two - Round one")

    # request input for damage against Player 1
    print_function("Enter damage against Player one")

    # set variable damage_against_player_1 to input
    damage_against_player_1 = input_function()

    # calculate player 1 current score
    sum1 = float(player_one_score) - float(damage_against_player_1)

    # update player one score
    player_one_score = sum1

    # print player one current score
    print_function('Player 1 current score: ' + format(sum1))

    # request input for player 2 healing
    print_function("Enter Player 2 healing")

    # set variable 'player_two_healing' to input
    player_two_healing = input_function()
    sum2 = float(player_two_score + float(player_two_healing))

    player_two_score = sum2

    # should I be using 'global' -- how?

    print_function("Player two current score: " + format(sum2))
    print_function("End of Player two -  Round one")


if __name__ == "__main__":
    main()
