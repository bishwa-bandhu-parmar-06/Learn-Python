with open("file1.txt", "r") as f:
    content1 = f.read()

with open("file2.txt", "r") as f:
    content2 = f.read()

if(content1 == content2):
    print("Yes Thses files are identical")
else:
    print("No Thses files are Not identical")