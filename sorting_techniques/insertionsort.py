def insertionsort(arr):
    size=len(arr)
    for i in range(1,size):
        anchor= arr[i]
        j=i-1
        while j>=0 and anchor < arr[j]:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=anchor

  
if __name__=="__main__":
    n=int(input())
    arr_str=input()
    arr1=[int(x) for x in arr_str.split()]
    insertionsort(arr1)
    print(arr1)
