f = open("poem.txt")
content = f.read()
if('twinkle' in content):
    print("The Word is twinkle is present in the content ")
else:
    print("The Word twinkle is not present in the content")

f.close()