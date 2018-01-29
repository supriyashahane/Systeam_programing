from sys import argv
script,filename = argv
with open (filename,'r') as input,open ("output1.txt","w") as output:
    line = input.readline()
    print line
    while line!="":
        words = line.split()
        print words
        for abc in words:
            print abc
        for ch in line:
            print ch
           # print chr(ord(ch)+3)
           # if ch == ' ':
            #    char = '$'
           # else:
            #    char= chr(ord(ch)+3)
             #   print char,
           # output.write(char)
        line=input.readline()
