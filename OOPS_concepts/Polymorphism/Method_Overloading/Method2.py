#USING *ARGS
# Function to take multiple arguments
def add(datatype, *args):
 
    # if datatype is int
    if datatype == 'int':
        answer = 0
 
    # if datatype is str
    if datatype == 'str':
        answer = ''

    # Traverse through the arguments
    for x in args:
 
        # This will do addition if the arguments are int. Or concatenation if the arguments are str
        answer = answer + x
 
    print(answer)
 
 
# Integer
add('int', 5, 6)
 
# String
add('str', 'Hi ', 'Aastha')