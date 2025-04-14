#파일 "input.txt"을 전부 읽는 프로그램을 작성하라.

infile = open("D:\\input.txt", "r")
lines = infile.read()
print(lines)
infile.close()
