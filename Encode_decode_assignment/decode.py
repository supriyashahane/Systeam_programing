from sys import argv
script,filename = argv
with open (filename,'r') as input,open ("input1.txt","w") as output:
    line = input.readline()
    while line!="":
        for ch in line:
           # print chr(ord(ch)+3)
            if ch == '$':
                char = ' '
            else:
                char= chr(ord(ch)-3)
            output.write(char)
        line=input.readline()
