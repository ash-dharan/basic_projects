# Bubble sort implementation

data = [5,4,3,2,1]
swap = True
l = len(data)
count = 0

while swap:
    swap= False
    for i in range(l-1):
        count += 1
        if data[i] > data[i+1]:
            data[i],data[i+1] = data[i+1],data[i]
            swap = True
        
    l -= 1

print(count)

