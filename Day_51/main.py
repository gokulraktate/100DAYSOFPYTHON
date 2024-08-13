# seek(), tell() and other functions | Python Tutorial - Day #51

# https://www.youtube.com/watch?v=PByYX-2l5Us&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg&index=51



# with open('myfile.txt','r') as f:
#     print(type(f))

#     f.seek(10)  #move to the 10th byte in the file


#     print(f.tell())  #gives index from where it is seek
#     data=f.read(5)  #read the next 5 bytes
#     print(data)


with open('sample.txt','r') as f:
    f.write('Hello World!')
    f.truncate(5)

with open('sample.txt','r')as f:
    print(f.read())