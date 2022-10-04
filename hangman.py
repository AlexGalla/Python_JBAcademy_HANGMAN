import random


def create_mask(wrd, ltr, msk):
    new_mask = msk
    if len(new_mask) == 0:
        for j in range(len(wrd)):
            new_mask = new_mask + "-"
    else:
        msk_list = list(new_mask)
        for k in range(len(wrd)):
            if ltr == wrd[k]:
                msk_list[k] = ltr
        new_mask = "".join(msk_list)
    return new_mask


def play_my_game():
    words = "python", "java", "swift", "javascript"
    word = random.choice(words)
    attempts_number = 8
    mask = create_mask(word, "", "")
    i = 1
    inputs_set = set()
    result = 0

    while i <= attempts_number:
        print()
        print(mask)
        letter = input("Input a letter: ")

        if len(letter) > 1 or len(letter) == 0:
            print("Please, input a single letter.")
            continue
        elif not letter.islower():
            print("Please, enter a lowercase letter from the English alphabet.")
            continue

        if letter in inputs_set:
            print("You've already guessed this letter.")
        else:
            inputs_set.add(letter)
            if letter in word:
                if letter in mask:
                    print("No improvements.")
                    i = i + 1
                else:
                    mask = create_mask(word, letter, mask)
            else:
                print("That letter doesn't appear in the word.")
                i = i + 1
            if mask == word:
                break

    if mask == word:
        print()
        print(mask)
        print("You guessed the word {}!".format(word))
        print("You survived!")
        result = 1
    else:
        print()
        print("You lost!")
        result = -1

    return result


print("H A N G M A N")
win_rate = 0
lose_rate = 0

while True:
    user_input = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ')
    if user_input == "play":
        if play_my_game() > 0:
            win_rate = win_rate + 1
        else:
            lose_rate = lose_rate + 1
    elif user_input == "results":
        print("You won: {} times".format(win_rate))
        print("You lost: {} times".format(lose_rate))
    elif user_input == "exit":
        break




