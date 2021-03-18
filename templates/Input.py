def menu():
    case = int(input())
    result = []
    for i in range(case):
        arr = []
        # number of elemetns as input
        n = int(input())
        # iterating till the range
        arr = list(map(int, input().strip().split()))[:n]
        key = int(input())
        result.append(function(arr, key))

    for i in range(case):
        print(result[i])


def main():
    menu()


if __name__ == "__main__":
    main()
