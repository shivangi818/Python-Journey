def main():
    array=[1,2,3,4,5,6,7,8,9,10]
    item=int(input())
    
    flag=False
    
    for element in array:
        if element==item:
            flag = True
            break
    if flag:
        print("Item found")
        
    else:
        print("Item not found")
if __name__=="__main__":
    main()