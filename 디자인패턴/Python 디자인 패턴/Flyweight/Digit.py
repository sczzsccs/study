class Digit():
    data = ""
    def __init__(this, filename:str):
        with open(filename, "r") as f:
            for line in f.readlines():
                this.data+=line
        pass
    
    def getData(this):
        return this.data
    pass

# i = 4
# data = ["", "", "", "", "",
#         "", "", "", "", ""]

# digit = Digit(f'./deta/{1}.txt')
# data[1] = digit.getData()

# digit = Digit(f'./deta/{2}.txt')
# data[2] = digit.getData()