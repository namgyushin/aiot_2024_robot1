def main() :
    score = input("학점을 입력하세요.> ")
    try:
        if not score.isdigit:
            raise
        score = float(score)
        if score > 4.5:
            raise
        if score < 0:
            raise
    except:
        exit()

    if score == 4.5:
        print(f"{score} 점은 '신' 입니다.")
    elif score >= 4.2:
        print(f"{score} 점은 '교수님의 사랑' 입니다.")
    elif score >= 3.5:
        print(f"{score} 점은 '현 체제의 수호자' 입니다.")
    elif score >= 2.8:
        print(f"{score} 점은 '현 체제의 수호자' 입니다.")
    elif score >= 2.3:
        print(f"{score} 점은 '일탈을 꿈꾸는 소시민' 입니다.")
    elif score >= 1.75:
        print(f"{score} 점은 '오락문화의 선구자' 입니다.")
    elif score >= 1.0:
        print(f"{score} 점은 '불가촉천민' 입니다.")
    elif score >= 0.5:
        print(f"{score} 점은 '자벌레' 입니다.")
    elif score > 0:
        print(f"{score} 점은 '플랑크톤' 입니다.")
    else:
        print(f"{score} 점은 '시대를 앞서가는 혁명의 씨앗' 입니다.")

if __name__ == "__main__":
    main()
