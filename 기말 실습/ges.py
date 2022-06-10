import random

guesses = ' '
turns = 10

infile = open('word.txt', "r")
lines = infile.readlines()  # 한 줄씩 리스트로 받기위함
word = random.choice(lines)

while turns > 0:  # 턴이 0 이상 남았을 때 반복
    failed = 0
    for char in word:
        if char in guesses:
            print(char, end='')
        else:
            print("_", end='')
            failed += 1
    if failed == 0:
        print("사용자 승리")
        break
    print("")
    guess = input("단어를 추측하시오 : ")
    guesses += guess
    if guess not in word:
        turns -= 1
        print("틀렸음!")
        print(str(turns) + "기회가 남았음!")
        if turns == 0:
            print("사용자 패배 정답은 : " + word)

infile.close()
