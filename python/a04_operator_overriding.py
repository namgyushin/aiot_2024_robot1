class Abc():
    def __add__(self, bb):
        return 'result of add'

def main():
    a = Abc()
    b = Abc()
    c = a + b
    print(c)

if __name__ == "__main__":
    main()