
def left(i):
    return 2*i

def right(i):
    return 2*i+1

def parent(i):
    return i//2


def is_max_heap(H):
    n = len(H)-1

    for i in range(n,1,-1):
        p = parent(i)
        if H[p]<H[i]:
            return False
    return True

if __name__ =="__main__":
    H = [None,12,44,5,3,5,7,3]
    if is_max_heap(H):
        print("Yes")
    else:
        print("No")