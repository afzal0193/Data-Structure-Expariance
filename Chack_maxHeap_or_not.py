

def left(i):
    return 2*i

def right(i):
    return 2*i+1

def parent(i):
    return i//2

def is_max_heap(H):       ### Chack heap is max or not .....
    n =len(H) - 1
    for i in range(n,1,-1):
        p = parent(i)
        if H[p]<H[i]:
            return False
    return False

if __name__ =="__main__":
    H = [None,19,7,17,3,5,12,10,1,2]
    if is_max_heap(H) is True:

        print("it is max_heap")
    else:
        print("it is min_heap")


