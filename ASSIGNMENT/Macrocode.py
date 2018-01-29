from sys import argv
script,filename = argv
count = 2
lenth = []
ins = []
valstr = []
value1 = []
with open(filename,'r') as input,open("OutPUT.asm",'w') as output:
    line = input.readline()
    #print line
    while line != "":
        for w in line:
            if ".data" in line or ".bss" in line or ".text" in line:
                continue
        else:
            #print line
            w = line.replace(' ',',',50).replace('\n',',',50).split(',')
            #print line
            d = len(w)
            if True:
                arry = w[0]
                arry1 = w[1]
                arry2 = "".join(w[2:])

                if arry == "%macro":
                    macroname = arry1
                    macrosize = arry2
                if count < 9:
                    ins.append(arry+' '+arry1+' '+arry2)
                array =  ins[1:][:-1]
                #print array (macrocod)
                    #print ins,res,val
                if arry =="%endmacro":
                    #arry2 = i
                    #print count
                    print "%line",str(count)+str('+')+str(1),filename
                    pass
                    #if ".data" in w[i+1]:
                if arry1 == ".data":
                    print '['+"section .data"+']'
                    output.write("[section .data]")
                    output.write('\n')
                    count1 = count
                    
                    #continue
                if arry1 == ".bss":
                    print '['+"section .bss"+']'
                if arry1 == ".text":
                    arry = '['+"section .text"+']'
                    arry1 = ""
                if arry == "global":
                    arry = '['+arry+' '+arry1+']'
                    arry1 = ""
                if arry == macroname:
                    lenth.append(arry1)
                    lenth.append(arry2)
                    length = len(lenth)
                    value1.append(arry1)
                    value1.append(arry2)
                    if int(length) == int(macrosize):
                        print "%line",str(count-1)+str('+')+str(1),filename
                        for s in array:
                            #print s
                            arry ="%line"
                            arry1 = str(count)+str('+')+str(1)
                            arry2 = filename
                            d =s.split()
                            aroy = d[0]
                            aroy1 = d[1]
                            aroy2 = "".join(d[2:])
                            #print arry2
                            if "%" in aroy2:
                                wid = len(d)
                                valuu = aroy2
                                #print wid
                                if "%" in valuu:
                                    valuu =  valuu[1:]
                                aroy2 = lenth[int(valuu)-1]
                            print aroy,aroy1,aroy2
                            output.write(aroy)
                            output.write(' ')
                            output.write(aroy1)
                            output.write(' ')
                            output.write(aroy2)
                            output.write('\n')

                if count > 9:
                    print arry,arry1,arry2
                    output.write(arry)
                    output.write(' ')
                    output.write(arry1)
                    output.write(' ')
                    output.write(arry2)
                    output.write('\n')


        line = input.readline()
        count = count + 1


"""if "section .data" in w[i]:
        print '[',line.strip('\n'),']'
    pass
    print line
line = input.readline()
"""     
