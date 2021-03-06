#!/bin/python3

## Hackerrank
## May-world Codesprint 2016: Richie Rich
## Moderate Level
## Logic #2

## Inputs: n k arr
## n :length of number
## k :number of digits that can be changed
## arr : array of digits (original number)


## format to print properly
def string(arr):
    s = ''
    for each in arr:
        s = s+str(each)
    return s

## if the number is a palindrome then how can we modify it, given k operations can be done
## modifies the array
def modify_pal(arr, n, k):
    ## if k is even, we can change digit at any place
    ## but if it is odd, n must be odd and only the middle digit will be replaced by '9'
    if k%2 == 0:
        for i in range(n//2):
            if k <= 0:
                break
            if arr[i] < '9':
                arr[i] = arr[n-i-1] = '9'
                k = k-2

    elif n%2 == 1 and k > 0:
        arr[n//2] = '9'

## same as make_pal, but
## it is invoked only when k is more than minimum count
def make_big_pal(arr, n, k, count):
    posi = 0
    pose = n-1
    while posi<pose and k>count:
        if arr[posi] != arr[pose]:
            if arr[posi] == '9':
                arr[pose] = '9'
            elif arr[pose] == '9':
                arr[posi] = '9'
            else:
                arr[posi] = arr[pose] = '9'
                k = k-1
            k = k-1
            count = count-1
        elif arr[posi] != '9':
            arr[posi] = arr[pose] = '9'
            k = k-2
        posi = posi+1
        pose = pose-1
    if k>=count and count!= 0:
        make_pal(arr, n, k)
    else:
        modify_pal(arr, n, k)

## if a number is NOT a palindrome, make it a palindrome
## comparing first and last digits, if the first and last digit are not same
## replace the smaller digit with bigger digit and decrement k by 1
def make_pal(arr, n, k):
    for i in range(n//2):
        if arr[i] == arr[n-i-1]:
            continue
        elif arr[i] < arr[n-i-1]:
            arr[i] = arr[n-i-1]
        else:
            arr[n-i-1] = arr[i]
        k = k-1

## check if a number can be converted to a palindrome or not, or if it is already one
## if conversion is not possible, i.e., if count > k, it prints -1
def possible_pal(arr, n, k):
    flag = 0
    ## count number of (pairs) differences to be a palindrome
    count = 0
    ## for odd n, we don't need to check the middle digit
    for i in range(n//2):
        if arr[i] != arr[n-i-1]:
            count = count + 1
            ## not a palindrome
            flag = 1
    ## the number is a palindrome
    if flag == 0:
        modify_pal(arr, n, k)
        print(string(arr))
    ## the number is not a palindrome, but can be converted to it
    elif count == k:
        make_pal(arr, n, k)
        print(string(arr))
    elif count < k:
        k = make_big_pal(arr, n, k, count)
        print(string(arr))
    ## not possible
    else:
        print(-1)
    return string(arr)

## take input here, store each digit in as an array element

n, k = input().strip().split(' ')
n = int(n)
k = int(k)
arr = list(input())
##print(arr)
ans = possible_pal(arr, n, k)
