import time

def main() :
    number = 0
    fps = 60
    delay_time = 1/60
    pre_time = time.time()
    while time.time() < pre_time + 5:
        number += 1
        time.sleep(delay_time)

    print(f"number of tick 5second : {number}")

if __name__ == "__main__":
    main()
