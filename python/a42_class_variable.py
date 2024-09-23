class Student:
    count = 0
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
        self.sum = self.get_sum()
        self.average = self.get_average()
        Student.count += 1

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

    def __eq__(self, value):
        return self.sum == value.sum
        
    def __ne__(self, value):
        return self.sum != value.sum
    
    def __gt__(self, value):
        return self.sum > value.sum
    
    def __ge__(self, value):
        return self.sum >= value.sum
    
    def __lt__(self, value):
        if isinstance(value, Student):
            return self.sum < value.sum
        elif isinstance(value, int):
            return self.sum < value
    def __le__(self, value):
        return self.sum <= value.sum

def main() :
    students = [
        Student("신남규", 99, 99, 99, 99),
        Student("이명철", 88, 88, 88, 88),
        Student("변새롬", 77, 77, 77, 77),
        Student("강민수", 66, 66, 66, 66),
        Student("정도현", 55, 55, 55, 55),
        Student("김승기", 44, 44, 44, 44),
    ]

    print(f"총 학생수: {Student.count}")
    print(f"총 학생수: {students[0].count}")
    print("이름\t총점\t평균")
    for student in students:
        print(student.to_string())
        # print(student)
        
if __name__ == "__main__":
    main()
