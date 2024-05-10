
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    re=arr[0];
    for i in range(n-1,0,-1):
        if ( arr[n-1] > arr[i]) :
            re=arr[i]
            break
    print(re)