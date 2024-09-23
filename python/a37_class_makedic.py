def create_student(name, korean, math, english, science):
    return {
        "name": name,
        "korean": korean,
        "math": math,
        "english": english,
        "science": science}
def main() :
    students = [
        create_student("신남규", 99, 99, 99, 99),
        create_student("이명철", 88, 88, 88, 88),
        create_student("변새롬", 77, 77, 77, 77),
        create_student("강민수", 66, 66, 66, 66),
        create_student("정도현", 55, 55, 55, 55),
        create_student("김승기", 44, 44, 44, 44),
    ]
    print("이름\t총점\t평균")
    for student in students:
        score_sum = (student["korean"]+student["math"]+student["english"]+student["science"])
        score_average = score_sum/4
        print(f"{student['name']}\t{score_sum}\t{score_average:.2f}")

if __name__ == "__main__":
    main()
