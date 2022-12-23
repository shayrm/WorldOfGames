import os

file_name = "test.txt"

with open(file_name, "rb") as file:
    try:
        file.seek(-2, os.SEEK_END)
        while file.read(1) != b'\n':
            file.seek(-2, os.SEEK_CUR)
    except OSError:
        file.seek(0)
    last_line = file.readline().decode()

print(f"this is the last line {last_line}")