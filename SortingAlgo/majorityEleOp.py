import random


def partition(arr, low, high):
    i = (low-1)
    pivot = arr[high]

    for j in range(low, high):
        if(arr[j] <= pivot):
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return(i+1)


def QuickSort(arr, low, high, k):
    # print(low, high, end=" ")
    if low < high:
        ind = random.randint(low, high)
        # print(arr[ind])
        arr[ind], arr[high] = arr[high], arr[ind]
        piv = partition(arr, low, high)

        if piv == k:
            return piv
        if piv > k:
            return QuickSort(arr, low, piv-1, k)
        elif piv < k:
            return QuickSort(arr, piv+1, high, k)
        return ind


def menu():
    arr = []
    # number of elemetns as input
    n = int(input())
    # iterating till the range
    arr = list(map(int, input().strip().split()))[:n]
    low = 0
    high = n-1
    k = (high//2)
    ind = QuickSort(arr, low, high, k)
    print(arr[ind])


def main():
    menu()


if __name__ == "__main__":
    main()
