from func import game as g

initial = True

print("끝말잇기 게임!\n")

while True:
    print()
    word = input("플레이어: ")
    game = g.word_relay(word)
    if initial == True:
        last_answer = game.choose_word()
        print(f"\n로봇: {last_answer}")
        initial = False
    else:
        if last_answer[-1] == word[0]:
            last_answer = game.choose_word()
            print(f"\n로봇: {last_answer}")
            initial = False
        else:
            print(f"{last_answer}의 끝 글자와 일치하지 않아서 패배 ㅠ")
            game.reset_game()
            break