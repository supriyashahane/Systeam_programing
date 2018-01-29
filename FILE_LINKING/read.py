from sys import argv
script,filename,filnam = argv
arry = []
arry1 = []
count = 0
with open(filename,'r')as input,open(filnam,'r')as input1,open("output.txt",'w')as output:
    line = input.readline()
    while line != "":
        arry = line
        count = count + 1
        print count,line
        output.write(str(count))
        output.write(' ')
        output.write(str(line))

        line = input.readline()
    linw = input1.readline()
    while linw != "":
        arry1 = linw
        count = count + 1
        print count,linw

        output.write(str(count))
        output.write(' ')
        output.write(str(linw))
        linw = input1.readline()

