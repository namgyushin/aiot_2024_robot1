class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

    def get_sum(self):
        return self.korean + self.math + self.english + self.science
    
    def get_average(self):
        return self.get_sum()/4
    
    def to_string(self):
        return f"{self.name}\t{self.get_sum()}\t{self.get_average():.2f}"
    
    # def __repr__(self):
    #     return f"{self.name}\t{self.get_sum()}\t{self.get_average():.2f}"
    # def __str__(self):
    #     return f"{self.name}\t{self.get_sum()}\t{self.get_average():.2f}"
    # 위 2개로 36번라인 출력

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
        print(student.to_string())
        # print(student)

if __name__ == "__main__":
    main()
