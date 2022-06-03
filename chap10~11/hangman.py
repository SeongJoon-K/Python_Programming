import random
guesses = ''
turns = 10


infile = open("words.txt", "r")
lines = infile.readlines()
word = random.choice(lines)
print(word)

while turns > 0:
    fail = 0
    for char in word:
        if char in guesses:
            print(char, end='')
        else:
            print("_", end='')
            fail += 1
    if fail == 0:
        print("사용자 승리")
        break
    print("")
    guess = input("단어를 추츠하시오 : ")
    guesses += guesses
    if guess not in word:
        turns -= 1
        print("틀렸습니다")
        print(str(turns) + "번 기회가 남음")
        if turns == 0:
            print("사용자 패배 정답은", word)

infile.close()
