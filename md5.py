import hashlib
m = hashlib.md5()
text = 'hello world'
m.update(text.encode('utf-8'))
file = open("results.txt","w")
file.write(m.hexdigest())
file.close()