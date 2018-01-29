def find_dd():

    from sys import argv
    script,filename=argv
    arry = []
    arry1 = []
    arry2 = []
    app = []
    count = 0
    count1 = 1
    symbol = []
    value = []
    with open(filename,'r')as input:
        line = input.readline()
        while line != "":
            w=line.replace('\n',' ',10).split(' ')
            #print w
            d = len(w)
            line = input.readline()
            if ".data" in line:
                continue
            if True:
                arry = w[0]
                #print arry,
                ar1 = w[1]
                #print arry1,
                arry2 = "".join(w[2:])
                #print arry2
                le = len(arry2)
                for i in range (d):
                    if "dd" in w[i] and ',' != arry2:
                        count =int(count)
                        arry1 = w[i+1]
                        #print arry
                        try:
                            if type(int(arry1)) == int:
                                #print arry1
                                arr = hex(int(arry1))[2:]#.ljust(7,'0')
                                #arr1 =  arr.zfill(8)
                                #print arr
                                d = len(arr)
                                #print d
                                if d >= 2:
                                    count = hex(count)[2:]
                                    count =str(count).zfill(8)
                                    arr1 = arr.ljust(8,'0')
                                    arr1 = arr1.zfill(8)
                                    #print arr1
                                    count1 = count1+1 
                                    print count1,count,arr1 ,'\t','\t',arry,ar1,arry2
                                    value.append(count)
                                    count = int(count,16)
                                    count = count+4
                                    symbol.append(arry)
                                    #print symbol
                                if d == 1:
                                    count = hex(count)[2:]
                                    count =str(count).zfill(8)
                                    arr1 = arr.ljust(7,'0')
                                    arr1 = arr1.zfill(8)
                                    count1=count1+1
                                    print count1,count,arr1,'\t','\t',arry,ar1,arry2
                                    value.append(count)
                                    count = int(count,16)
                                    count =count+4
                                    symbol.append(arry)
                                    #print symbol
                            #print arry
                        except ValueError:
                                pass

                        if "," in line:
                            #print line
                            #print len(arry2)
                            #w1 = line.replace(' ',',',10).replace('\n',',',1).split(',')
                            w1 = line.split()
                        
                            #print w1
                            d1 =  len(w1)
                            #print d1
                            for j in range (d1):
                                if "," in w1[j]:
                                    arry1 = w1[j]
                                    #print arry1
                                    w2 = arry1.replace(' ',',',10).replace('\n',',',1).split(',')
                                    d2 = len(w2)
                                    #print d2
                                    count = int(count)
                            for h in range (d2):
                                    arry1 = w2[0]
                            #print arry1
                                
                            try:
                                if type(int(arry1)) == int:
                                    arr = hex(int(arry1))[2:]
                                    d = len(arr)
                                    if d >= 2:
                                        count = hex(count)[2:]
                                        count = str(count).zfill(8)
                                        arr1 = arr.ljust(8,'0')
                                        arr1 = arr.zfill(8)
                                        if w2[1]==10:
                                            app = w2[1]
                                            app = hex(int(app))[2:]
                                            app1 = app.ljust(7,'0')
                                            app1 = app1.zfill(8)
                                            app2 =  arr1 + app1
                                        if w2[2] == '0':
                                            app = w2[2]
                                            app = hex(int(app))[2:]
                                            app1 = app.ljust(7,'0')
                                            app1 = app.zfill(8)
                                            app3 = app2 + app1
                                            count1 = count1+1
                                            print count1,count,arr1,'\t',w1[0],w1[1],w1[2]
                                            value.append(count)
                                            #print w2[0]
                                            count = int(count,16)
                                            symbol.append(w1[0])
                                            print symbol

                                    if d == 1:
                                        count = hex(count)[2:]
                                        count =str(count).zfill(8)
                                        arr1 = arr.ljust(7,'0')
                                        arr1 = arr1.zfill(8)
                                        #print type(w2[1])
                                        if w2[1]== '10':
                                            app = w2[1]
                                            app = hex(int(app))[2:]
                                            app1 = app.ljust(7,'0')
                                            app1 = app1.zfill(8)
                                            app2 =  arr1 + app1
                                            count1 = count1+1
                                            print count1,count,app2,'\t',w1[0],w1[1],w1[2]
                                            value.append(count)
                                            count = int(count,16)
                                            #print w1[0]
                                            symbol.append(w1[0])
                                            #print symbol
                                        if w2[2] == '0':
                                            app = w2[2]
                                            app = hex(int(app))[2:]
                                            #app1 = app.ljust(7,'0')
                                            app1 = app.zfill(8)
                                            #app3 = app2 + app1
                                            count =count +3
                                            count = hex(count)[2:]
                                            count = str(count).zfill(8)
                                            count1= count1+1
                                            print  count1,count,app1
                                            count = int(count,16)
                                            count = count +3
                            except ValueError:
                                pass
                            return count1,symbol,value


def find_bss(count1):

    from sys import argv
    script,filename=argv
    arry = []
    arry1 = []
    arry2 = []
    app = []
    count = 0
    symbol1 = []
    value1 =[]
    with open(filename,'r')as input:
        line = input.readline()
        #print line
        while line != "":
            w=line.replace('\n',' ',10).split(' ')
            #print w
            d = len(w)
            line = input.readline()
            if ".bss" in line:
                continue
            if True:
                arry = w[0]
                #print arry,
                ar1 = w[1]
                #print arry1,
                arry2 = "".join(w[2:])
                #print arry2
                le = len(arry2)
                for i in range (d):
                    if "resd" in w[i]:
                        count =int(count)
                        arry1 = w[i+1]
                        #print arry1
                        try:
                            #print arry1
                            if arry1 == '1':
                                #print "hello"
                                count = hex(count)[2:]
                                count = count.zfill(8)
                                res = "<res 00000004>"
                                count1 = count1+1
                                print count1,count,res,'\t',w[i-1],w[i],w[i+1]
                                symbol1.append(w[i-1])
                                value1.append(count)
                                count = int(count,16)
                                count = count + 4

                        except ValueError:
                            pass
                    if "resb" in w[i]:
                        count = int(count) +3
                        arry1 = w[i+1]
                        try:
                            if arry1 == '1':
                                count = hex(count)[2:]
                                count = count.zfill(8)
                                res = "<res 00000001>"
                                count1 = count1+1
                                print count1,count,res,'\t',w[i-1],w[i],w[i+1]
                                symbol1.append(w[i-1])
                                value1.append(count)
                                count = int(count,16)
                                count = count+1
                        except ValueError:
                            pass

                    if "resw" in w[i]:
                        count = int(count) +3
                        arry1 = w[i+1]
                        try:
                            if arry1 == '1':
                                count = hex(count)[2:]
                                count = count.zfill(8)
                                res = "<res 00000002>"
                                count1 = count1+1
                                print count1,count,res,'\t',w[i-1],w[i],w[i+1]
                                symbol1.append(w[i-1])
                                value1.append(count)
                                count = int(count,16)
                                count = count+1
                        except ValueError:
                            pass
                        return count1,symbol1,value1

from sys import argv
script,filename=argv
arry0 = []
arry1 = []
arry2 = []
app = []
count = 0
count1 = 1
reg32 = ["eax","ecx","edx","ebx","edi","esi","esp","ebp"]
reg321 = ["B8","B9","BA","BB","BC","BD","BE","BF"]
with open(filename,'r')as input:
    line = input.readline()
    while line != "":
        w=line.replace('\n',' ',10).replace(',',' ',10).split(' ')
        #print w
        d = len(w)
        line = input.readline()
        if ".data" in w:
            print count1,"                              section .data"
            arrr,symbol,value = find_dd()
            #print arrr
            count1 = arrr
            count1 =  count1+1
        if ".bss" in w:
            #print count1
            print count1,"                              section .bss"

            arr2,symbol1,value1 = find_bss(count1)
            #print arr2
            count1 = arr2
            count1 = count1+1
            code = 35264
        if ".text" in w:
            print count1,"                              section .text"
        if "global" in w:
            count1 = count1+1
            print count1,"                              global main"
        if "extern" in w:
            count1= count1+1
            print count1,"                              extern printf"
        if "main:" in w:
            count1= count1+1
            print count1,"                              main:"
        if "mov" in w:
            #count1 = count1+1
            #arr3 = find_mov(count1)
            arry0 = w[0]
            arry1 = w[1]
            arry2 = "".join(w[2])
            d = len(reg32)
            #print "B",8+1
            if arry1 in reg32:
                index1 = reg32.index(arry1)+1
            if arry2 in reg32:
                index2 = reg32.index(arry2)+1
                count = int(count)
                ######reg eax#####
                if index1 == 1 and index2 == 1:
                    count1 = count1+1
                    count = hex(count)[2:]
                    count = count.zfill(8)
                    code = hex(code)[2:]
                    print count1,count,code,'\t','\t',arry0,arry1,arry2
                    code = int(code,16)
                    count = int(count,16)
                    code = code+8
                    count = count + 2
                if index1 == 1 and index2 != 1:
                    count1 = count1+1
                    count = hex(count)[2:]
                    count = count.zfill(8)
                    code = code + 8
                    code = hex(code)[2:]
                    print count1,count,code,'\t','\t',arry0,arry1,arry2
                    code = int(code,16)
                    count = int(count,16)
                    code = code-16
                    count = count + 2
                    #print count,w[0]
                ####Acess symbol table###
                    length = len(symbol)
            if  arry1 in reg32 and arry2 in symbol:
                count1 = count1+1
                count = hex(count)[2:]
                count = count.zfill(8)    
                index1 = reg32.index(arry1)
                index2 = symbol.index(arry2)
                print count1,count,reg321[index1]+'['+value[index2]+']','\t',arry0,arry1,arry2
                count = int(count,16)
                count = count + 5



