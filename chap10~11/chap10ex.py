# outfile = open("happy.txt", "a")
# outfile.write("와그러노\n")
# outfile.write("와그러노\n")
# outfile.write("와그러노\n")
# outfile.close()
infile = open("happy.txt", "r")

for line in infile:
    word_list = line.split()
    for word in word_list:
        print(word)

infile.close()
