from dataclasses import dataclass

@dataclass
class Student:
    name: str
    korean: int
    math: int
    english: int
    science: int 

def main() :
    students = [
        Student("신남규", 99, 99, 99, 99),
        Student("이명철", 88, 88, 88, 88),
        Student("변새롬", 77, 77, 77, 77),
        Student("강민수", 66, 66, 66, 66),
        Student("정도현", 55, 55, 55, 55),
        Student("김승기", 44, 44, 44, 44),
    ]
    print("이름\t총점\t평균")
    for student in students:
        score_sum = (student.korean + student.math + student.english + student.science)
        score_average = score_sum/4
        print(f"{student.name}\t{score_sum}\t{score_average:.2f}")

if __name__ == "__main__":
    main()
