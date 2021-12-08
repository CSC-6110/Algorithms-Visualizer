
descriptionsDict = {'insertion'         : 'Insertion sort is a simple sorting algorithm that works \nsimilar to the way you sort playing cards in your hands. The \narray is virtually split into a sorted and an unsorted \npart. Values from the unsorted part are picked and placed \nat the correct position in the sorted part.',
                  'bubble'              : 'Bubble sort, also referred to as comparison sort, is a simple \nsorting algorithm that repeatedly goes through the list, \ncompares adjacent elements, and swaps them if they are in \nthe wrong order. Time complexity is O(n2).',
                  'selection'           : 'Selection sort divides the input list into two parts: a sorted\n sublist of items and a sublist of the remaining unsorted \nitems. The algorithm proceeds by finding the smallest \n(or largest) element in the unsorted sublist, exchanging \nit with the leftmost unsorted element and moving the sublist\n boundaries one element to the right.',
                  'merge'               : 'Merge Sort is a Divide and Conquer algorithm. It divides the \ninput array into two halves, calls itself for the two halves, \nand then merges the two sorted halves. The merge() \nfunction is used for merging two halves. The merge(arr, l, m, r)\n is a key process that assumes sub-arrays are sorted \nand merges two sorted sub-arrays into one. ',
                  'quick'               : 'Quicksort is a divide-and-conquer algorithm. It works by \nselecting a pivot element from the array and partitioning the other\nelements into two sub-arrays, according to whether \nthey are less than or greater than the pivot. Quicksort \nis a recursive comparison sort technique',
                  'counting'            : 'Counting sort is an algorithm that counts the keys of \nspecific range. It counts the number of elements in a specific \nindex position, The runtime of the algorithm is O(n). \nWorst case space complexity is higher than O(n) if the range \nof numbers are greater.',
                  'cocktail'            : 'Cocktail sort is the variation of Bubble Sort, which traverses \nthe list in both directions alternatively. It is different \nfrom bubble sort in the sense that bubble sort traverses \nthe list in the forward direction only, while this \nalgorithm traverses in forward as well as backward direction \nin one iteration. Time complexity is O(n2).',
                  # 'cycle'             : '1.to be written',
                  #'bogo'               : 'Bogo sort is an algorithm used to sort the elements of an \narray by randomly generating different permutations of an \narray and then checking whether it is sorted or not. Time \ncomplexity is O(n! * n).',
                  'heap'                : 'Heapsort is a sorting algorithm that uses element comparison.\n Like selection sort, heapsort creates area of sorted and\n unsorted portions. In each iteration, the algorithm \nextract the largest element of the array, thus shrink \nthe unsorted region. Runtime: O(n * log n).',
                  'radix'               : 'Radix sort is a non-comparative sorting algorithm. It avoids \ncomparison by creating and distributing elements into buckets\n according to their radix. For elements with more than \none significant digit, this bucketing process is repeated\n for each digit, while preserving the ordering of the \nprior step, until all digits have been considered.',
                  'shell'               : 'Shellsort is a generalization of sorting by exchange or \nsorting by insertion. The method starts by sorting pairs of \nelements far apart from each other, then progressively \nreducing the gap between elements to be compared. By \nstarting with far apart elements, it can move some out-of-place\n elements into position faster.',
                  'gnome'               : 'Gnome sort works by looking into previous and next element, \nif they are in right order, moves to next element. Otherwise,\n swap out of order elements and move backwork. If \nno previous previous cell, step forward. If no forward \ncell, Done !!! Runtime: O(n^2).',
                  'comb'                : 'Comb sort is an improvement of bubble sorting concept. In \neach step, bubble sort works on two elelemts and sort them, \nbut comb sort can work on multiple elements simultaniously.\n As comb sort works on multiple items at a time, \nthe runtime improves for comb sort.',
                  'bitonic'             : 'Bitonic sort is a comparison-based sorting algorithm that \ncan be run in parallel. It focuses on converting a random \nsequence of numbers into a bitonic sequence, one that \nmonotonically increases, then decreases. Time complexity \nis O(n log2 n).',
                  'pancake'             : 'Pancake sorting is the mathematical problem of sorting a \ndisordered stack of pancakes in order of size when a spatula \ncan be inserted at any point in the stack and used to \nflip all pancakes above it. A pancake number is the minimum\n number of flips required for a given number of pancakes.',
                  'binary insertion'    : 'Binary Insertion Sort uses binary search to find the proper \nlocation to insert the selected item at each iteration. \nTime complexity is O(n2).',
                  'bucket'              : 'Bucket sort, or bin sort, is a sorting algorithm that works \nby distributing the elements of an array into several buckets. \nEach bucket is then sorted individually, either \nusing a different sorting algorithm, or by recursively \napplying the bucket sorting algorithm. Time complexity is O(n^2).',
                  'tim'                 : 'Timsort is a hybrid stable sorting algorithm, derived from \nmerge sort and insertion sort, designed to perform well \non many kinds of real-world data. The algorithm finds \nsubsequences of the data that are already ordered and uses\n them to sort the remainder efficiently. This is done by merging\n runs until certain criteria are fulfilled.',
                  'stooge'              : 'Stooge sort is a recursive sorting algorithm. If the value at \nthe start is larger than the value at the end, swap them. \nIf there are 3 or more elements in the list, then: \n(1)Stooge sort the initial 2/3 of the list, (2)Stooge sort \nthe final 2/3 of the list, (3)Stooge sort the initial 2/3 \nof the list again.',
                  'strand'              : 'Strand sort is a recursive sorting algorithm which initially \nmoves the first elements of a list into a sub-list and \ncompare it with last. Once there is an element in the \noriginal list that is greater than the last element in the \nsub-list, the element is removed from the original list \nand added to the sub-list.',
                  'odd-even'            : 'Odd Even Sort algorithm is divided into two phases- Odd and \nEven Phase. The algorithm runs until the array elements are \nsorted and in each iteration two phases occurs- Odd \nand Even Phases.In the odd phase, we perform a bubble sort \non odd indexed elements and in the even phase, we perform a \nbubble sort on even indexed elements.',
                  'pigeonhole'          : 'Pigeonhole sorting is a sorting algorithm that is suitable \nfor sorting lists of elements where the number of elements and \nthe number of possible key values are approximately \nthe same. It requires O(n + Range) time where n is number \nof elements in input array and ‘Range’ is number of possible \nvalues in array. ',
                  'exchange'            : 'Exchange sort is a sorting algorithm that works similarly \nas bubble sort. The difference of exchange sort with bubble sort \nis that, exchange sort compares the first element of \nthe array with other elements. Runtime O(n^2).',
                  'iterative-merge'     : 'to be written',
                  'recursive insertion' : 'to be written',
                  'wiggle'              : 'to be written'}


