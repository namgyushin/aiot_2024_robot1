class Abc:
    def __getitem__(self, idx):
        return idx

def main() :
    print("문자 선택 연산자에 대해 알아볼까요?")
    print("안녕하세요"[0])
    print("안녕하세요"[1])
    print("안녕하세요"[2])
    print("안녕하세요"[3])
    print("안녕하세요"[4])
    #print("안녕하세요"[5])      #indexerror ,out of range
    a = Abc()
    print(a[3:4])
    print("안녕하세요"[-1])
    print("안녕하세요"[-2])
    print("안녕하세요"[-3])
    print("안녕하세요"[-4])
    print("안녕하세요"[-5])
    #print("안녕하세요"[-6])     #indexerror ,out of range
    print("안녕하세요"[1:4])    #1포함 4미포함 = 1~3
    print("안녕하세요"[1:4:1])  #1칸씩 띄면서
    print("안녕하세요"[1:4:2])  #2칸씩
    print("안녕하세요"[::])     #처음부터 끝까지
    print("안녕하세요"[::-1])   #역순



if __name__ == "__main__":
    main()
