def wiggleSort(array, *args):
    for i in range(len(array)):
        if (i % 2 == 1) == (array[i - 1] > array[i]):
            array[i - 1], array[i] = array[i], array[i - 1]
            yield array, i, -1 , i+1, -1