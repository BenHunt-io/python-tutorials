

### Numbers ########################
# Number types include {int,float,Decimal,Fraction,j/J}

### +,-,*,/ all work the same
fiveSquared = 5 ** 2
print(fiveSquared)

### Strings #######################
print(r"C:\raw\string");
print("""\
    1st Line
    2nd Line\
""")
print(3*"string multiples ");
# No character types, just string of size 1
print("negative"[-1]);
# slicing [,)   can omit [2:] -> [2,end), [:4] -> 3rd character
# Handles out of range gracefully
print("slicing"[2:7])
# Immutable, can't assign index
# Built in function len(s)
# Strings are sequences, support for lots of string methods,
# string literals with embedded expressions (format),
print("Ben is age:{0} and is very {1}".format(25,"cool"));

### Lists ##########################
# sequence type like string
squares = [1,4,9,16,25]
squaresShallowCopy = squares[2:]
# can add using .append(), concatenate using +, assignment to slices
# clear list
squares[:]
print("Squares: {0}".format(+len(squares)));