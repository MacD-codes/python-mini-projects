import time

def counter(start,end):
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print('Done!')

start=int(input("Enter a start time: "))
end=int(input("Enter an end time: "))
counter(start,end)