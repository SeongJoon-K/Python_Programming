filename = input("파일이름을 입력하세요 : ")
infile = open(filename, "r")

count = 0
strarr = infile.read()
strList = []
for i in len(strarr):
    strList[i] = strarr[i:i+1]
    print(strList[i])

# print(strList)
# for line in infile:
#     a = infile.read()
#     count += 1
# # 먼저 infile에 있는 것을 한 글자씩 배열에 넣는다.

# print("파일 안에 총 : ", count, "개의 글자가 있습니다.")
# infile.close()
