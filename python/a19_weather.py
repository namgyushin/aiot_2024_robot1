# datetime을 활용해서 month 데이터를 얻어와서
# 조건문으로 3~5월 봄, 6~8 여름, 9~11 가을, 나머지 겨울을 출력하는 코드 작성
import datetime


def main() :
    month = datetime.datetime.now().month

    # if month >= 3 and month <= 5:
    #     print(f"이번달은 {month}월로 봄입니다")
    # elif month >= 6 and month <= 8:
    #     print(f"이번달은 {month}월로 여름입니다")
    # elif month >= 9 and month <= 11:
    #     print(f"이번달은 {month}월로 가을입니다")
    # else:
    #     print(f"이번달은 {month}월달로 겨울입니다")

    if 3 <= month <= 5:
        print(f"이번달은 {month}월로 봄입니다")
    elif 6 <= month <= 8:
        print(f"이번달은 {month}월로 여름입니다")
    elif 9 <= month <= 11:
        print(f"이번달은 {month}월로 가을입니다")
    else:
        print(f"이번달은 {month}월로 겨울입니다")




if __name__ == "__main__":
    main()
