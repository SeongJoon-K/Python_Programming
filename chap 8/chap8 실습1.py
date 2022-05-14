alist = []
sum = 0
num = 0

for i in range(5):
    num = int(input("정수를 입력하세요 : "))
    alist.append(num)

for j in range(5):
    sum += alist[j]

avg = sum/len(alist)
print("평균 = ", avg)
