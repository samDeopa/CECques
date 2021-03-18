def FindMaj(arr):
    ele = -1
    maxCount = 0
    for i, val in enumerate(arr):
        curr = val
        count = 1
        for j in range(1, len(arr)):
            if(arr[j] == curr):
                count += 1
        if(count > maxCount):
            maxCount = count
            ele = curr
    if(maxCount > (len(arr)//2)):
        return [ele, maxCount]
    else:
        return [-1, -1]


def menu():
    case = int(input())
    result = []
    for i in range(case):
        arr = []
        # number of elemetns as input
        n = int(input())
        # iterating till the range
        arr = list(map(int, input().strip().split()))[:n]
        result.append(FindMaj(arr))

    for i in range(case):
        if(result[i][0] == -1):
            print("No majority Element Found")
        else:
            print("Majority Element is ",
                  result[i][0], "\nits frequncy is ->", result[i][1])


def main():
    menu()


if __name__ == "__main__":
    main()
