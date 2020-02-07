from sys import exit


def gold_room():
    print("The room are full of gold! How much you will take?")

    choise = input("> ")
    if '0' in choise or '1' in choise:
        how_much = int(choise)
    else:
        print("Hey, you have to enter a number!")

    if how_much < 50:
        print("Great! You are not greedy, so you won!")
        exit(0)
    else:
        print("FOOOOOOOOOO")
        exit(0)

gold_room()