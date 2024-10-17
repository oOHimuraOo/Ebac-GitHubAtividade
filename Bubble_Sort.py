
def bubble_sort(ar):
    for i in range(len(ar)):

        for j in range(len(ar) - 1):
            if ar[j] > ar[j+1]:
                ar[j], ar[j+1] = ar[j+1], ar[j]
            print(ar)

    return ar