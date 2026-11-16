hash_map = {}
input_list = []
output_list = []

for i in range(0,5):
    input_int = int(input(f"Enter the list item no {i+1}: "))
    input_list.append(input_int)

target = 15

for j in range(len(input_list)):
    complement = target - input_list[j]
    if complement in hash_map:
        output_list.append(hash_map[complement])
        output_list.append(j)
        break
    else :
        hash_map[input_list[j]] = j

print(output_list)

