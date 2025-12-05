import re

try:
    with open('test.txt', 'r') as f:
        s = f.read()
        result = [list(map(int, part.split("-"))) for part in s.split(",")]
        total = 0;
        for i in result:
            for j in range (i[0], i[1] + 1):
                # print("Checking number: ", j)
                num = str(j)
                curr, temp, flag, p, q = 0,0,0,0,0
                pattern = []
                checked = []
                while q < len(num):
                    # print("Pattern: ", pattern, " Checked: ", checked)
                    if not pattern:
                        pattern.append(num[q])
                    elif num[q] == pattern[curr]:
                        checked.append(num[q])
                        curr += 1
                        if curr > len(pattern) - 1:
                            curr = 0
                    elif curr == 0 and q != len(num) and 0 == len(checked):
                        pattern.append(num[q])
                    else:
                        for k in checked:
                            # print("Adding ", k, " to pattern")
                            pattern.append(k)
                        checked = []
                        curr = 0
                        q-=1
                    q+=1
                while p != len(num):
                    if temp == len(pattern):
                        temp = 0
                    elif pattern[temp] == num[p]:
                        p += 1
                        temp += 1
                        if p == len(num) and temp == len(pattern) and len(pattern) < len(num):
                            flag = 1
                    else:
                        break
                if flag:
                    # print("Success ", j, " with pattern ", pattern)
                    total += j
        print(total)
except FileNotFoundError:
    print("Error: The file 'your_file.txt' was not found.")
