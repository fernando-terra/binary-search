data = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

min = 0 
max = len(data) - 1

def search(n):
    global min
    global max

    avg = round((min + max) / 2)
    
    if(data[avg] < n):
        min = avg + 1
    else:
        max = avg - 1
    
    if(data[avg] == n):
        return avg
    else:
        if(min > max):
            return -1
        else:
            return search(n)

def reset():
    global min
    global max
    min = 0 
    max = len(data) - 1

print(search(60))
reset()

print(search(41))
reset()

print(search(13))
reset()

print(search(11))
reset()