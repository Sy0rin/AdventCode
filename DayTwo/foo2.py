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
                curr = 0
                pattern = []
                checked = []
                for i in range(len(num)):
                    if num[i] == pattern[curr]:
                        checked.append(num[i])
                        curr += 1
                    elif curr == 0:
                        pattern.append(num[i])
                    else:
                        for k in checked:
                            pattern.append(k)
                        curr = 0
                        i-=1      
        print(total)
except FileNotFoundError:
    print("Error: The file 'your_file.txt' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
