#frequency count using dictionary
arr=[1,2,3,4,5,5,3,3,3,3,4,5,5]
freq_map = {}
for num in arr:
    freq_map[num] = freq_map.get(num, 0) + 1
print(freq_map)