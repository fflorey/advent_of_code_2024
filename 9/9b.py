diskfield = ""

def read_file(filepath):
    global diskfield
    with open(filepath, 'r') as file:
        diskfield = file.readline().strip()


# read_file("input.xs")
# read_file("input.txt.small")
read_file("input.txt.large")

print(diskfield)

# build hashmap of diskfield - diskfield contains blank spaces and used spaces
empty_space=0
used_space=0
file_list=[]
id=0
for i in range(len(diskfield)):
    if i%2 == 0:
        used_space+=int(diskfield[i])
        file_list.append((id,i,int(diskfield[i])))
        id+=1
    else:
        empty_space+=int(diskfield[i])
        file_list.append((-1,i,int(diskfield[i])))


print(f"Used space: {used_space} Empty space: {empty_space}")

# find a file which fits into the gap with len empty_len
def findFile(list, empty_len, pos):
    for i in range(len(list)-1,-1,-1):
        file = list[i]
        file_len = file[2]
        if file_len <= empty_len and file[0] != -1 and i > pos:                        
            # add an empty element at this position
            list.insert(i,(-1,file[1],file_len))
            return list.pop(i+1)
    return None

pos=0
i=0
sum_size=0
while True:
    if i >= len(file_list):
        print("that's it")
        break
    elem=file_list[i]
    id=elem[0]
    pos=elem[1]
    flen=elem[2]
    if id != -1:
        sum_size+=flen
    else:
        file=findFile(file_list,flen, i)
        if not file:
            i+=1
            continue
        file_list[i] = file
        sum_size+=file[2]
        if ( flen > file[2] ):
            file_list.insert(i+1,(-1,i,flen-file[2]))
    i+=1
    if (sum_size == used_space):
        print("sum_size == used_space")
        break
    
result = 0
pos=0
for elem in file_list:
    for n in range(elem[2]):
        id = elem[0]
        if id != -1:
            result += id*pos
        pos+=1
print(f"result: {result}")
