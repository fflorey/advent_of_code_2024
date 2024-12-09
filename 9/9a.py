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
empty_space_list = []
id=0
for i in range(len(diskfield)):
    if i%2 == 0:
        used_space+=int(diskfield[i])
        file_list.append((id,i,int(diskfield[i])))
        id+=1
    else:
        empty_space+=int(diskfield[i])
        empty_space_list.append((-1,i,int(diskfield[i])))


print(f"Used space: {used_space} Empty space: {empty_space}")
print(f"file_list: {file_list} \n{empty_space_list}")

final_file_list=[]
final_list=[]
while empty_space_list:
    if not file_list:
        break
    else:
        final_list.append(file_list.pop(0))
    empty_file=empty_space_list.pop(0)
    empty_file_pos=empty_file[1]
    empty_file_len=empty_file[2]
    while True:
        if not file_list:
            break
        last_file = file_list.pop()
        file_id=last_file[0]
        file_pos=last_file[1]
        file_len=last_file[2]
        print(f"empty_file: {empty_file} last_file: {last_file} file: {file_id} {file_pos} {file_len}")
        if empty_file_len >= file_len:
            final_list.append(last_file)
            empty_file_len-=file_len
        else:
            file_list.append((file_id,file_pos,file_len-empty_file_len))
            final_list.append((file_id,empty_file_pos,empty_file_len))
            break
        
print(f"final_list: {final_list}")
result = 0
pos=0
for elem in final_list:
    for n in range(elem[2]):
        id = elem[0]
        result += id*pos
        pos+=1

print(f"result: {result}")
