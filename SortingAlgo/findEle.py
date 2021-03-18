def find()


def menu():
    arr = []
    # number of elemetns as input
    n = int(input())
    # iterating till the range
    arr = list(map(int, input().strip().split()))[:n]
    low = 0
    high = n-1
    k = (high//2)
    ind = Find(arr, low, high, k)
    print(arr[ind])


def main():
    menu()


if __name__ == "__main__":
    main()
