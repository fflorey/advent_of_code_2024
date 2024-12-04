def read_input_file(filename):
    with open(filename, 'r') as file:
        lines = [list(line.strip()) for line in file.readlines()]
    return lines

def rotate_90_degrees(array):
    return [list(row) for row in zip(*array[::-1])]

def search_sequence(array, sequence):
    number_of_hits = 0  
    sequence_length = len(sequence)
    for row in array:
        print("row) ", row)
        for i in range(len(row) - sequence_length + 1):
            if row[i:i + sequence_length] == list(sequence):
                print("hit!: ",row[i:i + sequence_length])
                number_of_hits += 1
    return number_of_hits

def search_diagonal(array, sequence):
    def check_diagonal(x, y, dx, dy):
        for i in range(len(sequence)):
            if not (0 <= x < len(array) and 0 <= y < len(array[0])) or array[x][y] != sequence[i]:
                return False
            x += dx
            y += dy
        return True

    sequence = list(sequence)
    number_of_hits = 0
    for i in range(len(array)):
        for j in range(len(array[0])):
            if check_diagonal(i, j, 1, 1):
                print ("hit!: ", i,j)
                number_of_hits += 1
            if check_diagonal(i, j, 1, -1):
                print ("hit!: ", i,j)
                number_of_hits += 1
            if check_diagonal(i, j, -1, 1): 
                print ("hit!: ", i,j)
                number_of_hits += 1
            if check_diagonal(i, j, -1, -1):
                print ("hit!: ", i,j)
                number_of_hits += 1
    return number_of_hits

input_data = read_input_file('input.txt')

result=0
print(input_data)
result += search_sequence(input_data, 'XMAS')
print("result: ", result)
input_data = rotate_90_degrees(input_data)
result +=search_sequence(input_data, 'XMAS')
print("result: ", result)
input_data = rotate_90_degrees(input_data)
result += search_sequence(input_data, 'XMAS')
print("result: ", result)
input_data = rotate_90_degrees(input_data)
result +=search_sequence(input_data, 'XMAS')
print("Result: ", result)
input_data = rotate_90_degrees(input_data)
result +=search_diagonal(input_data, 'XMAS')
print("Result: ", result)

