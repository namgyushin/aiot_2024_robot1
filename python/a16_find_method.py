def main() :
    output_a = "안녕안녕안녕하세요안녕.".find("안녕")
    print(output_a)
    while output_a != -1 :
        output_a = "안녕안녕안녕하세요안녕.".find("안녕",output_a+1)
        # 있으면 0, 없으면 -1
        print(output_a)

    print("안녕" in "안녕하세요")       # 뒤쪽에 앞쪽이 있나 없나

    a = "10 20 30 40 50".split()
    print(a)
    str1 = " ".join(a)
    print(str1)

if __name__ == "__main__":
    main()
