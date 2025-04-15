# in.txt 생성
with open("in.txt", "w") as infile:
    infile.write("1000000\n")  # 첫 줄에 1000000 출력
    infile.write("1 " * 500000 + "2 " * 500000)  # 50만 개의 1과 50만 개의 2 작성

# out.txt 생성
with open("out.txt", "w") as outfile:
    outfile.write("1000000")  # 첫 줄에 1000000 출력
