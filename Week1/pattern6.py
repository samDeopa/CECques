def menu():
    n = int(input())
    for i in range(n):
        for j in range(n-i):
            print(j+1, end="")
        print()


def main():
    menu()


if __name__ == "__main__":
    main()
