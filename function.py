# python functions
# basic function using python
# using global variables

x = "awesome"


def myfunc():
    print("Python is " + x)


myfunc()

y = "KAKKAD"


def myFunc():
    print("OMKAR " + y)


myFunc()


def myfunc():
    global z
    z = "fantastic"


myfunc()

print("Python is " + z)


a = "awesome"


def myfunc():
    global a
    a = "great"


myfunc()

print("Python is " + a)


