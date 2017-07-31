import os

file_size_stored = os.stat('test1.pdf').st_size
print(file_size_stored)