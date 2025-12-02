import re

count = 50;
password = 0;
try:
    with open('test.txt', 'r') as f, open('log.txt', 'w') as f2:
        lines = f.readlines()
        for line in lines:
            prev = count
            temp = 0
            parts = re.findall(r'[A-Za-z]+|\d+', line)
            character = parts[0]
            number = int(parts[1])
            if character == 'L':
                for _i in range(number):
                    count -= 1
                    if count == 0:
                        password += 1
                    elif count < 0:
                        count = 99
            elif character == 'R':
                for _i in range(number):
                    count += 1
                    if count == 100:
                        count = 0
                    if count == 0:
                        password += 1
            f2.write(f"Character: {character}, Number: {number}, Count: {count}, Password: {password}\n")
    print(f"Password: {password}")
except FileNotFoundError:
    print("Error: The file 'your_file.txt' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

