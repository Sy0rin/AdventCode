import re

try:
    with open('test.txt', 'r') as f:
        s = f.read()
        flag = 0
        result = [list(map(int, part.split("-"))) for part in s.split(",")]
        total = 0;
        for i in result:
            for j in range (i[0], i[1] + 1):
                num = str(j)
                way = len(num)//2
                first_half = num[:way]
                second_half = num[way:]
                if first_half == second_half:
                    total += j
        print(total)
except FileNotFoundError:
    print("Error: The file 'your_file.txt' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
