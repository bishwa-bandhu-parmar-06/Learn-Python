import random

def game():
    print("You are Playing The game...")
    score = random.randint(1, 62)
    with open("highscore.txt") as f:
        highscore = f.read()
        if(highscore != ""):
            highscore = int(highscore)
        else:
            highscore = 0

    print(f"Your High Score : {score}")
    if(score > highscore):
        with open("highscore.txt", "w") as f:
            f.write(str(score))
    return score


game()