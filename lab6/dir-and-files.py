# ex1
import os

path = "."  # You can change to any path

print("Directories:")
print([d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))])

print("Files:")
print([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])

print("All:")
print(os.listdir(path))



# ex2
import os
path = input()

print("Existence: ", os.access(path, os.F_OK))
print("readability: ", os.access(path,  os.R_OK))
print("writability: ", os.access(path, os.W_OK))
print("Executability: ", os.access(path, os.X_OK))


# ex3
import os

s = input()
exists = os.path.exists(s)
print(exists)

if exists:
    print("File name: ")
    print(os.path.basename(s))
    print("Directory portion: ")
    print(os.path.dirname(s))


# ex4
import os

path = input()

if not os.path.exists(path):
    print("File not find")
with open(path, "r") as a:
    print("Count lines: ", len(a.readlines()))


# ex5
anylist = map(int, input().split())

path_to_file = input('Where to write?: ')

with open(path_to_file, 'w') as a:
    for i in anylist:
        a.write("%s\n" % i)


# ex6
import string
for i in string.ascii_uppercase:
   with open(i + ".txt", "w") as a:
       a.writelines(i)


# ex7
path1 = input()
path2 = input()

with open(path1) as i:
    with open(path2, "w") as j:
        for k in i:
            j.write(k) 


# ex8
import os

path = input()

if os.access(path, os.F_OK) and os.access(path, os.R_OK) and os.access(path, os.W_OK):
    os.remove(path)
else:
    print("File not remove")