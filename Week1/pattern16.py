def menu():
    n = int(input())
    for i in range(n):
        for j in range(n-i-1):
            print(" ", end="")
        for j in range(i+1):
            print(j+1, end="")
        for j in range(1, i+1):
            print(i-j+1, end="")
        print()
    for i in range(n):
        for j in range(i+1):
            print(" ", end="")
        for j in range(n-i-1):
            print(j+1, end="")
        for j in range(n-i-3, -1, -1):
            print(j+1, end="")
        print()


def main():
    menu()


if __name__ == "__main__":
    main()
