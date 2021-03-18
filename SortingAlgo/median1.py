def findMed(arr):
    arr.sort()
    if(len(arr) % 2 == 0):
        return (arr[len(arr)//2] + arr[(len(arr)//2)+1])//2
    else:
        return arr[len(arr)//2]


def menu():
    arr = []
    # number of elemetns as input
    n = int(input())
    # iterating till the range
    arr = list(map(int, input().strip().split()))[:n]
    median = findMed(arr)
    print(median)


def main():
    menu()


if __name__ == "__main__":
    main()
