def menu():
    n = int(input())
    for i in range(n):
        for j in range(n-i-1):
            print(" ", end="")
        for j in range(i+1):
            print("*", end="")
        print()


def main():
    menu()


if __name__ == "__main__":
    main()
