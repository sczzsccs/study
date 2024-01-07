It_list = [
    [1,2,3,4],
    [[1,2],[1,3,4]],
    [2,3,7,8]
]

def Iterator(it_list:list):
    if(type(it_list)==list):
        it = iter(it_list)
        it_nt = next(it, 0)
        while(it_nt):
            Iterator(it_nt)
            it_nt = next(it, 0)
        if(it_nt!= 0): print(it_nt)
        else: print()
    else: print(it_list)

def Two_it(it_list:list):
    Iterator(it_list)
    print("-"*10)
    Iterator(it_list)
    pass

Two_it(It_list)