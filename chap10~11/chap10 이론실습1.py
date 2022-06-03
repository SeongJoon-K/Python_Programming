# 입력 파일 이름과 출력파일 이름을 받는다.
infilename = input("입력 파일 이름 : ")
outfilename = input("출력 파일 이름 : ")

# 입출력을 위한 파일을연다.
infile = open(infilename, "r")
s = infile.read()


outfile = open(outfilename, "w")
outfile.write(s)


# 파일 닫기.
infile.close()
outfile.close()
