
def main() :
    students = [
        {"name": "신남규", "korean": 99, "math": 99, "english": 99, "science": 99},
        {"name": "이명철", "korean": 88, "math": 88, "english": 88, "science": 88},
        {"name": "변새롬", "korean": 77, "math": 77, "english": 77, "science": 77},
        {"name": "강민수", "korean": 66, "math": 66, "english": 66, "science": 66},
        {"name": "정도현", "korean": 55, "math": 55, "english": 55, "science": 55},
        {"name": "김승기", "korean": 44, "math": 44, "english": 44, "science": 44},
    ]
    print("이름\t총점\t평균")
    for student in students:
        score_sum = (student["korean"]+student["math"]+student["english"]+student["science"])
        score_average = score_sum/4
        print(f"{student['name']}\t{score_sum}\t{score_average:.2f}")

if __name__ == "__main__":
    main()
