#You and your friend are in a team to write a two-player game, human against computer, such as Tic-Tac-Toe / Noughts and Crosses.
# Your friend will write the logic to play one round of the game, while you will write the logic to allow many rounds of play, keep score, decide who plays, first, etc.
# The two of you negotiate on how the two parts of the program will fit together, and you come up with this simple scaffolding (which your friend will improve later):

def play_once():
    win_of_user = 0
    win_of_computer = 0

    while True:
        import random
        rng = random.Random()
        result = rng.randrange(-1,2)

        human_plays_first = int(input("Lütfen -1, 0 veya 1 sayısını giriniz: "))

        print("Sizin tahmininiz: ={0}, Kazanan sayı: ={1} ".format(human_plays_first, result))
        if result == human_plays_first:
            print("Kazandınız.")
            win_of_user += 1
        else:
            print("Kaybettiniz. ")
            win_of_computer += 1

        win_rate = (win_of_user) / (win_of_user + win_of_computer) * 100
        print("Sizin kazanma sayınız {}, bilgisayarın kazanma sayısı {}'dır. Kazanma oranınız ise %{}'dır. ".format(win_of_user,win_of_computer,win_rate))

        response = input("Tekrar oynamak ister misiniz? evet veya hayır .")
        if response != "evet":
            return False

play_once()