def main():
    n=int(input())
    array=[]
    
    for i in range(n):
        num=int(input(i+1))
        array.append(num)
    tot_sum=sum(array)
    
    return tot_sum
print(main())
    
    