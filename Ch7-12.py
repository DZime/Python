#Chapter 7 Strings-addtional-exercises number 12

def main():
    words = str(input("Input Sentence:")).split()
    for word in words:
        print(word[1:] + word[0] + "ay", end = " ")
    print ()

main()
