import os
import sys

def main() :
    print(os.path)
    print(__file__)
    print(os.getcwd())
    os.chdir("/home/lmc/aiot_2024_robot1/python/data")
    if os.path.exists("basic.txt"):
        print("파일이 이미 있습니다.")
        with open("basic.txt", 'a', encoding='utf-8') as file:
            file.write("this is file save data! add\n")
    else:
        with open("basic.txt", "w", encoding = 'utf-8') as file:
        # 주의! "w" -> 파일에 데이터가 있으면 다 지우고 파일을 엶
            file.write("this is file save data! 1\n")
            file.write("this is file save data! 2\n")
    
if __name__ == "__main__":
    main()
