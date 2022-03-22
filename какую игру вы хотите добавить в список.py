game_list = []

while True:
    game_name = input()
    if game_name == 'exit':
        break
    game_rating = input()
    if game_rating == 'exit':
        break
    else:
        game_rating = int(game_rating)

    pair = game_name, game_rating
    game_list.append(pair)

    print(game_list)
