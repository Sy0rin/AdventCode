import re

total = 0;

try:
    with open('sample.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            val = 0
            for index,p in enumerate(line):
                try:
                    q=max(line[index+1:])
                    if int(p+q) > val:
                        val = int(p+q)
                except ValueError:
                    continue
            total+=val
    print(total)
except FileNotFoundError:
    print("Error: The file 'your_file.txt' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
