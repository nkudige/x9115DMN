#Exercise 3.1

"""
repeat_lyrics()

def print_lyrics():
    print "I'm a lumberjack, and I'm okay."
    print "I sleep all night and I work all day."

def repeat_lyrics():
    print_lyrics()
    print_lyrics()

"""

#Error message received: NameError: name 'repeat_lyrics' is not defined

#Exercise 3.2

def repeat_lyrics():
    print_lyrics()
    print_lyrics()
    
def print_lyrics():
    print "I'm a lumberjack, and I'm okay."
    print "I sleep all night and I work all day."

repeat_lyrics()

#Program runs

#Exercise 3.3

def right_justify(string_value):
    lengthstr = len(string_value)
    whitespaces = 70-lengthstr
    print " "*whitespaces+string_value

right_justify("allen")


#Exercise 3.4

def do_twice(f, value):
    f(value)
    f(value)

def print_twice(value):
    print value
    
def do_four(f, value):
    do_twice(f, value)
    do_twice(f, value)

do_twice(print_twice, "spam")

do_four(print_twice, "spam")

#Exercise 3.5

def print_square(arg):
    for i in range(0, 2*arg):
        print_border(arg)
        do_four(print_rows, arg)
    print_border(arg)
    
def print_border(arg):
    for i in range(0, 2*arg):
        print "+",
        print "----",
    print "+"
    
def print_rows(arg):
    for i in range(0, 2*arg-1):
        print "|     ",
    print "|      |"
        
print_square(2)
