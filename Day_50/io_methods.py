# read(), readlines() and other methods | Python Tutorial - Day #50

# https://www.youtube.com/watch?v=l1FsnQxET9U&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg&index=50


# f=open('myfile.txt','r')
# while True:
#     line = f.readline()
#     print(line)
#     if not line:
#         print(line,type(line))
#         break
    
# f=open('myfile.txt','r')
# while True:
#     line = f.readline()
#     if not line:
#         break
#     print(line)


# f=open('myfile2.txt','r')
# i=0
# while True:
#     i=i+1
#     line = f.readline()
#     m1=int(line.split(",")[0])
#     m2=int(line.split(",")[1])
#     m3=int(line.split(",")[2])
#     print(f"Marks of stud {i} in math is:{m1}")
#     print(f"Marks of stud {i} in eng is:{m2}")
#     print(f"Marks of stud {i} in sci is:{m3}")
    
#     print(line)

f=open('myfile3.txt','w')
lines=['line 1\n','line 2\n','line 3\n']
f.writelines(lines)
f.close()
