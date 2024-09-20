def main() :
    list_a = [1, 2, 3]
    print(list_a)

    # append
    list_a.append(4)
    list_a.append(5)
    print(list_a)

    # insert
    list_a.insert(0, 0)
    list_a.insert(3, 2.5)
    print(list_a)

    # del
    del list_a[0]
    print(list_a)
    a = "a variable"
    list_a.insert(0, a)     # 0번에 a를 추가
    print(list_a)
    del list_a[0]           # 요소를 지웠다고 변수가 지워지진 않는다
    print(list_a)
    print(a)

    # pop
    list_a.append("last element")
    re = list_a.pop(2)        # 괄호 안에 안쓰면 뒤에서부터 삭제
    print(list_a, re)

    # remove by value 특정값 삭제
    list_a.remove("last element")
    print(list_a)    


if __name__ == "__main__":
    main()
