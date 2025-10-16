with open("log.txt", "r") as f:
    lines = f.readlines()

lineno = 1
for line in lines:
    if("python" in line):
        print(f"yes Python is Present Line No. : {lineno}")
        break
    lineno += 1
else: 
    print("No Python is Not Present")