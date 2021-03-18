

def partition(arr, low, high):
    i = (low-1)
    pivot = arr[high]

    for j in range(low, high):
        if(arr[j] <= pivot):
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return(i+1)


def QuickSort(arr, low, high):
    if(len(arr) == 1):
        return arr
    if low < high:
        piv = partition(arr, low, high)

        QuickSort(arr, low, piv-1)
        QuickSort(arr, piv+1, high)


def menu():
    arr = []
    # number of elemetns as input
    n = int(input())
    # iterating till the range
    arr = list(map(int, input().strip().split()))[:n]
    low = 0
    high = n-1
    QuickSort(arr, low, high)
    print(arr)


def main():
    menu()


if __name__ == "__main__":
    main()
