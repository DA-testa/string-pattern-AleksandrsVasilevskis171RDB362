# python3
d = 10
def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    choice = input()
    check = None
    first_line = " "
    second_line = " "
    
    for i in choice:
        if i == "I":
            check = False
           
            


                
        elif i =="F":
            check = True


            

            
    
    # after input type choice
    # read two lines
    if check == False:
        first_line= input()
        second_line = input()  
    elif check == True:
        f = open("tests/06",mode = "r")
        first_line=f.readline()
        second_line = f.readline()


    #print(first_line)
    #print(second_line)          
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function
    q = len(first_line)+len(second_line)
    return (first_line.rstrip(), second_line.rstrip(),q)

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text, q):
    arr = []
    m = len(pattern)
    n = len(text)
    p = 0
    t = 0
    h = 1
    i = 0
    j = 0

    for i in range(m-1):
        h = (h*d) % q

    # Calculate hash value for pattern and text
    for i in range(m):
        p = (d*p + ord(pattern[i])) % q
        t = (d*t + ord(text[i])) % q

    # Find the match
    for i in range(n-m+1):
        if p == t:
            for j in range(m):
                if text[i+j] != pattern[j]:
                    break

            j += 1
            if j == m:
                arr.append(i)
                #print("Pattern is found at position: " + str(i+1))

        if i < n-m:
            t = (d*(t-ord(text[i])*h) + ord(text[i+m])) % q

            if t < 0:
                t = t+q
    

    # and return an iterable variable
    return arr


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
