with open("log.txt", "r") as f:
    content = f.read()

if("python" in content):
    print("yes Python is Present")
else: 
    print("No Python is Not Present")