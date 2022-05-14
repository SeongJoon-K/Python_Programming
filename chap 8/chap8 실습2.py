import random
counters = [0, 0, 0, 0, 0, 0]  # 1부터 6까지 카운트

for i in range(1000):
    counters[random.randrange(0, 6)] += 1

for i in range(6):
    print("주사위가 ", i + 1, "인 경우는", counters[i], "번")
