def main() :
    # 선언
    dict_a = {'a':123}
    set_a = set()
    set_a.add(1)
    set_b = {1,2,3}
    print(type(dict_a))
    print(type(set_a))
    print(type(set_a))
    print(dict_a, set_a, set_b)

    # 요소 추가
    dict_a['b'] = 654
    dict_a['a'] = 987
    dict_a['c'] = 321

    print(dict_a)

    # 요소 접근
    print(dict_a['a'], dict_a['b'])
    # print(dict_a['c'])
    print(dict_a.get('c'))
    # 'c'가 없으면 에러가 나지만, get은 None을 반환하고 중단되지 않아서 안전하다.

if __name__ == "__main__":
    main()
