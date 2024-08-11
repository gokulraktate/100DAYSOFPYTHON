# Local vs Global Variables in Python| Python Tutorial - Day #48

# https://www.youtube.com/watch?v=RaG6GgcDt54&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg&index=48


# x=4
# print(x)

# def hello():
#     x=5
#     print(f"The local x is:{x}")
#     print("Hello Harry")
# print(f"The global x is:{x}")
# hello()
# print(f"The global x is:{x}")


x=10  #global

def fun():
    global x
    x=5  #global
    y=3 #local

    print(y)
fun()
print(x)
# print(y)