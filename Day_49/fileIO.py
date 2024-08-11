# File IO in Python | Python Tutorial - Day #49

# https://www.youtube.com/watch?v=eDBPlcWYses&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg&index=49

#READING IN A FILE

# f=open('myfile1.txt','r')   #filename,mode(r,w,a) read,write,append

# text = f.read()
# print(text)
# f.close()

# f=open('myfile2.txt','w')  
# text = f.read()
# print(text)
# f.close()

# f=open('myfile1.txt','a')   #append mode
# text = f.read()
# print(text)
# f.close()

# read as binary
# f=open('myfile1.txt','rb')  
# text = f.read()
# print(text)
# f.close()

# read as text
# f=open('myfile1.txt','rt')  
# text = f.read()
# print(text)
# f.close()

#WRITING IN A FILE
# f=open('myfile2.txt','w')
# f.write('Hello,World!')
# f.close()

#appending

# f=open('myfile2.txt','a')
# f.write('Hello,World!')
# f.close()


#not using close

with open('myfile2.txt','a') as f:
    f.write("Hey this is after appending")