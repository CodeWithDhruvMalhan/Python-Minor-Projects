import time
import lorem

s = lorem.sentence()  
a = s.split(" ")

def speed_testing():
    s = lorem.sentence()  
    a = s.split(" ")
    print("Write Given below sentence")
    print(s)

    start = time.time()
    d = input(">>> ")
    end = time.time()

    b = d.split(" ")
    correct = 0
    for i in range(0,len(a)):
        if (a[i]==b[i]):
            correct+=1
    print()
    print(f"Your result is {correct} out of {len(a)} Words")
    print("Total Time Taken is ",(end-start)," seconds")
    print(f"Accuracy = {(correct/len(a))*100}")



if __name__ == "__main__": 
    print("Welcome to our Speed Tester!".center(80))
    print("Type A to Start or E to Exit")

    inp = input(">>> ")

    if(inp.upper() == "A"):
        speed_testing()
    else:
        print("Thanks for Visting".center(80))