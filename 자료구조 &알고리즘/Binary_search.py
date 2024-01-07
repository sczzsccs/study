def binary_search(n:int, array:list):
    array.sort()
    Mid = int(array.__len__()/2)
    while(array[Mid] != n):
        if(array[Mid] > n):
            Mid /= 2
        else:
            Mid += (Mid/2)
        Mid = int(Mid)
    
    return array[Mid]

Array = [9,4,1,3,5]
print(binary_search(4, Array))