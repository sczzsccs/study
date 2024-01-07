import matplotlib.pyplot as plt
import numpy as np

# plot
fig, ax = plt.subplots()

def Input_Step():
    A = [0]
    B = [0]

    i = 0
    while i >= 0:
        plt.cla()
        i = int(input("A :"))
        A.append(i)
        if len(A) > 8:
            A = A[1:]
        if len(B) < 8:
            B.append(B[-1]+1)
            
        print("A:", A)
        print("A:", B)

        ax.step(B, A, linewidth=1)

        ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
               ylim=(0, 8), yticks=np.arange(1, 8))
        
        plt.pause(0.5)
        pass
    pass

if __name__ == "__main__":
    Input_Step()