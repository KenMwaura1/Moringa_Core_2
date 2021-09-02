handle = open("test.txt", "r")

data = handle.read()
print(data)

# find number of times python occurs in the text file
counter = 0
for word in data.split():
    if word == "Python":
        counter += 1
print(f"\n Python occurs {counter} times ")
handle.close()
