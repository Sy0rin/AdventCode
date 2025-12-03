import re

try:
    with open('test.txt', 'r') as f:
        s = f.read()
        result = [list(map(int, part.split("-"))) for part in s.split(",")]
        for i in result:
            for j in range (i[0], i[1] + 1):
                print(j)
except FileNotFoundError:
    print("Error: The file 'your_file.txt' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
