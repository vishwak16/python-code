def bubblesort(arr):
    size=len(arr)
    for i in range(size-1):
        swapped=False
        for j in range(size-1-i):
            if arr[j]>arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
                swapped=True
        if not swapped:
            break
if __name__=="__main__":
    n=int(input("num of elements:"))
    n_str=input()
    elements=[int(x) for x in n_str.split()]
    bubblesort(elements)
    print(elements)