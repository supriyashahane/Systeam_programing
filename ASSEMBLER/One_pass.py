import numpy as np
from sys import argv
script,filename,filename1,filename2=argv
arry = []
literal = []
adress = []
arry1 = []
arry2 = []
arry3 = []
size = []
sym = []
typ = []
DoU = []
size = []
value = []
count =0
sy = 0
line1 = []
print "*********************************************** SYMBOL TABLE ******************************************************************"
print ("sym_no""\t""line_No""\t""var_name""\t""var_type""\t""var_size""\t""var_value""\t""var_type")
with open (filename,'r')as input ,open ("output.txt","w")as output:
    line = input.readline()
    spc = "    "
    #output.write("line_No",spc,"var_name",spc,"var_size",spc,"var_value",spc,"var_type",'\n')
    d =len (line)
    while line != "":
        count = count + 1
        line1 = count
        for w in line:
            if ".data"in line or ".bss" in line or ".text" in line:
                #del(line)
                continue

        else:   
                #print("hello")
                #print line
                w = line.replace('\n',' ',1).split(' ')
                #print (w)
                #line =  input.readline()   
                c = len(w)
                #print c
                if True :
		    no = 0
                    arry =  w[0]
                    #print arry
                    arry1 = w[1]
                    #print w[1]
                    arry2 = "".join(w[2:])
                    if arry1 == "dd":
                        #print sy
                        sy = sy+1
                        sym = arry
                        typ = "int"
                        DoU = 'D'
                        size = len(arry2)*4
                        value = arry2
                        #print sy
                        print sy,'\t',line1,'\t''\t',sym,'\t''\t',typ,'\t''\t',size,'\t''\t',value,'\t''\t',DoU,'\t'
                        #output.write(str(no1))
                        output.write(str(sy))
                        output.write(spc)
                        output.write(str(line1))
                        output.write(spc)
                        output.write(sym)
                        output.write(spc)
                        output.write(typ)
                        output.write(spc)
                        output.write(str(size))
                        output.write(spc)
                        output.write(value)
                        output.write(spc)
                        output.write(DoU)
                        output.write('\n')
                    if arry1 == "dq":
                        sy = sy+1
                        sym = arry
                        typ = "float"
                        DoU = 'D'
                        size = len(arry2)*8
                        value = arry2
                        print sy,'\t',line1,'\t''\t',sym,'\t''\t',typ,'\t''\t',size,'\t''\t',value,'\t''\t',DoU,'\t'
			output.write(str(sy))
                        output.write(spc)
                        output.write(str(line1))
                        output.write(spc)
                        output.write(sym)
                        output.write(spc)
                        output.write(typ)
                        output.write(spc)
                        output.write(str(size))
                        output.write(spc)
                        output.write(value)
                        output.write(spc)
                        output.write(DoU)
                        output.write('\n')
                    if arry1 == "db":
                        sy = sy+1
                        sym = arry
                        typ = "byte"
                        DoU = 'D'
                        size = len(arry2)*1
                        value = arry2
                        print sy,'\t',line1,'\t''\t',sym,'\t''\t',typ,'\t''\t',size,'\t''\t',value,'\t''\t',DoU,'\t'
			output.write(str(sy))
                        output.write(spc)
                        output.write(str(line1))
                        output.write(spc)
                        output.write(sym)
                        output.write(spc)
                        output.write(typ)
                        output.write(spc)
                        output.write(str(size))
                        output.write(spc)
                        output.write(value)
                        output.write(spc)
                        output.write(DoU)

                        output.write('\n')
                    if arry1 == "dw":
                        sy = sy +1
                        sym = arry
                        typ = "word"
                        DoU = 'D'
                        size = len(arry2)*2
                        value = arry2
                        print sy,'\t',line1,'\t''\t',sym,'\t''\t',typ,'\t''\t',size,'\t''\t',value,'\t''\t',DoU,'\t'
			output.write(str(sy))
                        output.write(spc)
                        output.write(str(line1))
                        output.write(spc)
                        output.write(sym)
                        output.write(spc)
                        output.write(typ)
                        output.write(spc)
                        output.write(str(size))
                        output.write(spc)
                        output.write(value)
                        output.write(spc)
                        output.write(DoU)

                        output.write('\n')
                    if arry1 == "resb":
                        sy =sy+1
                        sym = arry
                        typ = "Reversed byte"
                        DoU = 'U'
                        size = len(arry2)*1
                        value = arry2
                        print sy,'\t',line1,'\t''\t',sym,'\t''\t',typ,'\t''\t',size,'\t''\t',value,'\t''\t',DoU,'\t'
                        output.write(str(sy))
                        output.write(spc)
                        output.write(str(line1))
                        output.write(spc)
                        output.write(sym)
                        output.write(spc)
                        output.write(typ)
                        output.write(spc)
                        output.write(str(size))
                        output.write(spc)
                        output.write(value)
                        output.write(spc)
                        output.write(DoU)

                        output.write('\n')
                    if arry1 == "resw":
                        sy = sy+1
                        sym = arry
                        typ = "Reversed word"
                        DoU = 'U'
                        size = len(arry2)*2
                        value = arry2
                        output.write(str(sy))
                        output.write(spc)
                        output.write(str(line1))
                        output.write(spc)
                        output.write(sym)
                        output.write(spc)
                        output.write(typ)
                        output.write(spc)
                        output.write(str(size))
                        output.write(spc)
                        output.write(value)
                        output.write(spc)
                        output.write(DoU)

                        output.write('\n')
                        print sy,'\t',line1,'\t''\t',sym,'\t''\t',typ,'\t''\t',size,'\t''\t',value,'\t''\t',DoU,'\t'
                    if arry1 == "resd":
                        sy = sy+1
                        sym = arry
                        typ = "Reversed int"
                        DoU = 'U'
                        size = len(arry2)*4
                        value = arry2
                        output.write(str(sy))
                        output.write(spc)
                        output.write(str(line1))
                        output.write(spc)
                        output.write(sym)
                        output.write(spc)
                        output.write(typ)
                        output.write(spc)
                        output.write(str(size))
                        output.write(spc)
                        output.write(value)
                        output.write(spc)
                        output.write(DoU)

                        output.write('\n')
                        print sy,'\t',line1,'\t''\t',sym,'\t''\t',typ,'\t''\t',size,'\t''\t',value,'\t''\t',DoU,'\t'
                    if arry1 == "resw":
                        sy = sy+1
                        sym = arry
                        typ = "Reversed word"
                        DoU = 'U'
                        size = len(arry2)*8
                        value = arry2
                        output.write(str(sy))
                        output.write(spc)
                        output.write(str(line1))
                        output.write(spc)
                        output.write(sym)
                        output.write(spc)
                        output.write(typ)
                        output.write(spc)
                        output.write(str(size))
                        output.write(spc)
                        output.write(value)
                        output.write(spc)
                        output.write(DoU)

                        output.write('\n')
                        print sy,'\t',line1,'\t''\t',sym,'\t''\t',typ,'\t''\t',size,'\t''\t',value,'\t''\t',DoU,'\t'
                    if ":" in line:
                        sy = sy+1
                        s = line.split(':')
                        sym = s[0]
                        typ = "label"
                        DoU = 'U'
                        size = '-'
                        value = '-'
                        print sy,'\t',line1,'\t''\t',sym,'\t''\t',typ,'\t''\t',size,'\t''\t',value,'\t''\t',DoU,'\t'
                        output.write(str(sy))
                        output.write(spc)
                        output.write(str(line1))
                        output.write(spc)
                        output.write(sym)
                        output.write(spc)
                        output.write(typ)
                        output.write(spc)
                        output.write(str(size))
                        output.write(spc)
                        output.write(value)
                        output.write(spc)
                        output.write(DoU)

                        output.write('\n')
                    
        #print literal,adress
        line = input.readline()
print "********************************************************************************************************************************"
print "*********************************************** LITERAL TABLE ******************************************************************"

arry = []
arry1 = []
arry2 = []
arry3 = []
arry4 = []
arry5 = []
arry6 = []
count = 0
sy = 0
ins = ['mov','add','sub','mul']
inss = ["jmp","inc","dec","je","jge","jne"]
reg = ["eax","edx","ecx","ebx","eci","edi","edi","esp","ebp","ax","bx","cx","dx","sp","bp","si","di","ah","al","bh","bl","ch","cl"]
print "lit_no  line_no    Literal    ASCII_val"

with open(filename,'r')as input,open(filename1,'r')as input1,open("Output.txt",'w')as output:
    linw = input1.read()

    output.write("literal_no  line_no    Literal    ASCII_val"'\n')
    spc = "        "
    w = linw.split()
    #print w
    #linw = input1.readline()
    line =input.readline()
    while line != "":
        s = line.replace(',',' ',1).split()
        #print s
        count = count+1
        d =len(s)
        #print s
        for i in range (d):
            if s[i] in ins:
                arry = line
                wt = arry.replace(',',' ',1).split()
                #print wt
                #print len(wt[2])
                if wt[2] in w :
                    arry1 =  wt[2]
                elif wt[2] in reg:
                    arry1 = wt[2]
                    #print wt[2]
                    #print arry1,
                    #print arry2
                    #print count,arry1,arry2
                elif "'" in arry:
                    sy = sy+1
                    #v =arry.replace(' ',"'",1).split("'")
                    arry2 =  wt[2]
                    arry4= [ord(x) for x in arry2]
                    h = len(arry4)
                    for l in range(h):
                        arry6 = hex (arry4[l])
                        arry3 = arry6
                    print sy,'\t',count,'\t','\t',arry2,'\t','\t',arry3
                    output.write(str(sy))
                    output.write(spc)
                    output.write(str(count))
                    output.write(spc)
                    output.write(str(arry2))
                    output.write(spc)
                    output.write(str(arry3))
                    output.write('\n')
                elif ":" in line:
                    sy = sy+1
                    v1=line.split(':')
                    print v1
                    if v1[0] in w:
                        arry1 =  v1[0]
                    else :
                        error = v1[0]
                        print "not defined = %s",error
                #elif len(wt[1])>=3 and len(wt[2])>=3:
                 #   arry5 = wt[2]
                elif type(int(wt[2])) == int:
                    sy = sy+1
                    arry2 =  wt[2]
                    arry3 = hex(ord(wt[2]))
                    print sy,'\t',count,'\t','\t',arry2,'\t','\t',arry3

                    output.write(str(sy))
                    output.write(spc)
                    output.write(str(count))
                    output.write(spc)
                    output.write(str(arry2))
                    output.write(spc)
                    output.write(str(arry3))

                    output.write('\n')
                else:
                    error = wt[2]
                    print "error ",arry5,"is not defined"
        line =input.readline()
print "**********************************************************************************************************************************"
print "*********************************************** INTERMEDIATE CODE ******************************************************************"
count = 0
lineno =1
arry =[]
arry1 =[]
arry2 = []
sy = 0
with open(filename,'r')as input,open(filename1,'r')as input1,open(filename2,'r')as input2:
    line2 = input2.read()
    line1 = input1.read()
    if True:
        k = line1.replace('\n','    ',1).split('    ')
        l = line2.replace('\n',' ',1).split(' ')
        #print k
        wid = len(k)
        #print l
        wid1 = len(l)
    line = input.readline()
    while line!= "":
        lineno = lineno + 1
        #line = input.readline()
        if True:
            w = line.replace(' ',',',1).replace('\n',',',1).split(',')
            arr = ["eax","ecx","edx","ebx","esp","ebp","esi","edi"]
            arr1 = "#reg32"
            arr161 = "#reg16"
            arr81 = "#reg8"
            lit1 = "#lit"
            sym1 = "#sym"
            arr16 = ['ax','cx','dx','bx','sp','bp','si','di']
            arr8 = ['al','bl','dl','bl','ah','ch','dh','bh']
            ins =["mov","add","sub","jmp","inc","dec","cmp"]
            ins1 = [5,2,3,4,5,6,7]
            opcod = ["#opcode01","#opcode02","#opcode03","#opcode03","#opcode04","#opcode05","#opcode06","opcode07"]
            c =len(arr)
            d =len(w)
            leni = len(ins)
            for i in range (d):
                if w[i] in ins: 
                    arry = w[i]
                    arry1 = w[i+1]
                    arry2 = w[i+2]
                    #print opcode
            if True:
                for k1 in range (leni):
                    if arry == ins[k1]:
                        arry = opcod[k1]
                        count = int(count) + int(ins1[k1])
                        #count = hex(ord(int(count)))
                for j in range (c):
                    if arry1 == arr[j] and arry2 in k:
                        sy = sy+1
                        if "#opcode01" in arry:
                            co = hex(count)[2:].zfill(8)
                            print sy,'\t',lineno,'\t',co,'\t',"mov",arry1,arry2,'\t',arry,"0#0",arr1,sym1
                        elif "#opcode02" in arry:
                            co = hex(count)[2:].zfill(8)
                            print sy,'\t',lineno,'\t',co,'\t',"add",arry1,arry2,'\t',arry,"0#0",arr1,sym1
                    elif arry1 ==arr[j] and arry2 in l:
                        sy = sy+1
                        if "#opcode01" in arry:
                            co = hex(count)[2:].zfill(8)
                            print sy,'\t',lineno,'\t',co,'\t',"mov",arry1,arry2,'\t',arry,"0#0",arr1,lit1

                        elif "#opcode02" in arry:
                            co = hex(count)[2:].zfill(8)
                            print sy,'\t',lineno,'\t',co,'\t',"add",arry1,arry2,'\t',arr1,"1#1",lit1
                    elif arry1 == arr[j] and arry2 in arr:
                        sy = sy+1
                        if "#opcode01" in arry:
                            co = hex(count)[2:].zfill(8)
                            print sy,'\t',lineno,'\t',co,'\t',"mov",arry1,arry2,'\t',arry,"000",arr1,arr1
                        elif "#opcode02" in arry:
                            co = hex(count)[2:].zfill(8)
                            print sy,'\t',lineno,'\t',co,'\t',"add",arry1,arry2,'\t',arry,"000",arr1,arr1
                    elif arry1 == arr[j] and arry2 in arr16:
                        sy = sy+1
                        if "#opcode01" in arry:
                            co = hex(count)[2:].zfill(8)
                            print sy,'\t',lineno,'\t',co,'\t',"mov",arry1,arry2,'\t',arry,"001",arr1,arr1
                        elif "#opcode02" in arry:
                            co = hex(count)[2:].zfill(8)
                            print sy,'\t',lineno,'\t',co,'\t',"add",arry1,arry2,'\t',arry,"001",arr1,arr161
                    elif arry1 == arr[j] and arry2 in arr8:
                        sy = sy+1
                        if "#opcode01" in arry:
                            co = hex(count)[2:].zfill(8)
                            print sy,'\t',lineno,'\t',co,'\t',"mov",arry1,arry2,'\t',arry,"010",arr1,arr1
                        elif "#opcode02" in arry:
                            co = hex(count)[2:].zfill(8)
                            print sy,'\t',lineno,'\t',co,'\t',"add",arry1,arry2,'\t',arry,"010",arr1,arr81
                    elif arry1 == arr16[j] and arry2 in arr16:
                        sy = sy+1
                        if "#opcode01" in arry:
                            co = hex(count)[2:].zfill(8)
                            print sy,'\t',lineno,'\t',co,'\t',"mov",arry1,arry2,'\t',arry,"011",arr1,arr1
                        elif "#opcode02" in arry:
                            co = hex(count)[2:].zfill(8)
                            print sy,'\t',lineno,'\t',co,'\t',"add",arry1,arry2,'\t',arry,"011",arr161,arr161
                    elif arry1 == arr16[j] and arry2 in arr8:
                        sy = sy+1
                        if "#opcode01" in arry:
                            co = hex(count)[2:].zfill(8)
                            print sy,'\t',lineno,'\t',co,'\t',"mov",arry1,arry2,'\t',arry,"100",arr161,arr81
                        elif "opcode02" in arry:
                            co = hex(count)[2:].zfill(8)
                            print sy,'\t',lineno,'\t',co,'\t',"add",arry1,arry2,'\t',arry,100,arr161,arr81
                    elif arry1 == arr8[j] and arry2 in arr8:
                        sy = sy+1
                        if "#opcode01" in arry:
                            co = hex(count)[2:].zfill(8)
                            print sy,'\t',lineno,'\t',co,'\t',"mov",arry1,arry2,'\t',arry,"101",arr81,arr81
                        elif "opcode02" in arry:
                            co = hex(count)[2:].zfill(8)
                            print sy,'\t',lineno,'\t',co,'\t',"add",arry1,arry2,'\t',arry,101,arr161,arr81
                    elif arry1 == arr[j] and type(int(arry2)) == int:
                        sy=sy+1
                        if "#opcode01" in arry:
                            co = hex(count)[2:].zfill(8)
                            print sy,'\t',lineno,'\t',co,'\t'"mov",arry1,arry2,'\t',arry,"110",arr1,"#immediate val"
                        elif "opcode02" in arry:
                            co = hex(count)[2:].zfill(8)
                            print sy,'\t',lineno,'\t',co,'\t'"add",arry1,arry2,'\t',arry,"110",arr1,"#immediate val"
                    elif arry1 == arr16[j] and type(int(arry2)) == int:
                        sy=sy+1
                        if "#opcode01" in arry:
                            co = hex(count)[2:].zfill(8)
                            print sy,'\t',lineno,'\t',co,'\t'"mov",arry1,arry2,'\t',arry,"110",arr1,"#immediate val"
                        elif "opcode02" in arry:
                            co = hex(count)[2:].zfill(8)
                            print sy,'\t',lineno,'\t',co,'\t'"add",arry1,arry2,'\t',arry,"110",arr1,"#immediate val"
                    elif arry1 == arr8[j] and type(int(arry2)) == int:
                        sy = sy+1
                        if "#opcode01" in arry:
                            co = hex(count)[2:].zfill(8)
                            print sy,'\t',lineno,'\t',co,'\t'"mov",arry1,arry2,'\t',arry,"110",arr1,"#immediate val"
                        elif "opcode02" in arry:
                            co = hex(count)[2:].zfill(8)
                            print sy,'\t',lineno,'\t',co,'\t'"add",arry1,arry2,'\t',arry,"110",arr1,"#immediate val"
        
        line = input.readline()

