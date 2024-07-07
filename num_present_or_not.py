def main():
    n, num=map(int,input().split())
    array=list(map(int,input().split()))

    for i in range(n):
        if array[i]==num:
            return i
    return -1
print(main())

