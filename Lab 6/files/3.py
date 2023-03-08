# Write a Python program to test whether a given path exists or not. If the path exist find the filename and directory portion of the given path.
import os

p = input("write the path to the file:\n")

if os.path.exists(p):
    filename = os.path.basename(p)
    dirname = os.path.dirname(p)
    print(f"Filename of the path :{filename}" )
    print(f"directory portion of the given path {dirname}")
    
else:
    print("path does not exists")
