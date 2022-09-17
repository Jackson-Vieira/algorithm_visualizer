from settings import *

def bubbleSort(draw_setts):
    lst = draw_setts.lst
    for i in range(len(lst)):
        for k in range(len(lst)-i-1):
            num1, num2 = lst[k], lst[k+1]
            if num1 > num2: 
                lst[k], lst[k+1] = lst[k+1], lst[k]
                draw_setts.drawList({k: DARK_RED, k + 1: RED})
                yield 1
    return lst


def selectionSort(draw_setts):
    lst = draw_setts.lst
    for i in range(len(lst)):
        min_index = i
        for j in range(i, len(lst)):
            if lst[min_index] > lst[j]:
                min_index = j

        draw_setts.drawList({min_index: RED, j: DARK_RED})
        yield 1
        lst[i], lst[min_index] = lst[min_index], lst[i]
        
    return lst


def insertionSort(draw_setts):
    lst = draw_setts.lst
    for i in range(1,len(lst)):
        key = lst[i]

        j = i-1

        while key < lst[j] and j >= 0:
            lst[j+1] = lst[j]
            draw_setts.drawList({i : (0,255,0), j-1: RED, j: RED})
            j -= 1
            yield

        lst[j+1] = key

    return lst


merges = []
def mergeSort(draw_setts, i=0, end=None):
    
    lst = draw_setts.lst
    if end == None:
        end = len(lst)
    
    if (end-i) > 1:
        md = (i+end)//2
        mergeSort(draw_setts, i, md)
        mergeSort(draw_setts, md, end)
        merges.append(merge(lst, draw_setts, i, md, end))
        
    return merges
def merge(lst, draw_setts, i, md, end):
    left = lst[i:md]
    right = lst[md:end]
    
    top_left, top_right = 0, 0

    for j in range(i, end):
        if top_left > len(left)-1:
            lst[j] = right[top_right]
            top_right += 1
        elif top_right > len(right)-1:
            lst[j] = left[top_left]
            top_left += 1
        elif left[top_left] < right[top_right]:
            lst[j] = left[top_left]
            top_left += 1
        else:
            lst[j] = right[top_right]
            top_right += 1
        draw_setts.drawList()
        yield