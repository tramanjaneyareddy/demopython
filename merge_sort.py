" merge sort program will divide and merge list "

def merge_sort(li):
    if len(li)>1:
        m=len(li) // 2
        left=li[:m]
        right=li[m:]
        merge_sort(left)
        merge_sort(right)
        i=0
        j=0
        k=0
        while len(left)>i and len(right)>j:
            if left[i]<right[j]:
                li[k]=left[i]
                i+=1
                k+=1
            else:
                li[k]=right[j]
                j+=1
                k+=1
        while i<len(left):
            li[k]=left[i]
            i += 1
            k += 1
        while j<len(right):
            li[k]=right[j]
            j += 1
            k += 1


n=int(input('enter:'))
l=[int(input())for x in range(n)]
merge_sort(l)
print("sorted list is:",l)
