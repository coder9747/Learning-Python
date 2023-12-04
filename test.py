def binary_search(list:list,ele):
    s = 0
    e = len(list)-1
    while(s<=e):
        mid = (s+e)//2
        if(list[mid]==ele):return mid
        elif(list[mid]<ele):s = mid+1
        elif(list[mid]>ele):e = mid-1
    return -1;



list = [3,5,2,5,6,9,7,6,4,2,5,0,100,50];
list = sorted(list);

print(binary_search(list=list,ele=8));
    