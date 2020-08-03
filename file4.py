# combo tools v 4
# python3
import os
import hashlib
os.system('cls' or 'clear')
class color :
    GREEN = '\033[48m'
    RED = '\033[91m'

print(color.RED+'''
www.SinaAbdi.com

  _      _____  _____ _______   _______ ____   ____  _       _____ 
 | |    |_   _|/ ____|__   __| |__   __/ __ \ / __ \| |     / ____|
 | |      | | | (___    | |       | | | |  | | |  | | |    | (___  
 | |      | |  \___ \   | |       | | | |  | | |  | | |     \___ \ 
 | |____ _| |_ ____) |  | |       | | | |__| | |__| | |____ ____) |
 |______|_____|_____/   |_|       |_|  \____/ \____/|______|_____/ 
                                                                   
                                                                   

Dev: Mr Sina
Version : 4.0
''')
im = '''
            Pleas Enter Mode :
            
    [0] Show Line  Count
    [1] Line Spliter
    [2] remov duplicate line
    [3] save duplicate
    [4] combo crack offline
    [6] encode password on combo
    [5] combo crack online
    [5] Dev info
    [9] Exit
    
              : '''
mode = int(input(im))
if mode != 9:
    while mode != 9:
        n = 0
        d = 0
        if mode == 0:
            f = input('Pleas Enter Your File Neme : ')
            fi = open(f , 'r',encoding='latin1',errors='ignore')
            for line in fi:
                n += 1
                d += 1
                if d == 1000000:
                    d = 0
                    print('\t\t--->',n,'|line prossed')
            print('\t\t %s Lins is : '% n)
            n = 0
            d = 0
        if mode == 1:
            f = input('Pleas Enter Your File Neme : ')
            fi = open(f , 'r',encoding='latin1',errors='ignore')
            fo = open('res_'+f,'a',encoding='UTF-8',errors='ignore')
            spc = input("Split by ? ' : ; , . @ and ....' ")
            rf = int(input("""
            
            [0] for left
            [1] for right
            [2] for right 2 (exampel : email:pass:phone | 2 for save phone )
            [3] for right 3 (exampel :  user:email:pass:phone | 3 for save phone)
            [4] for right 4 (exampel :  user:email:pass:phone | 4 for save email:pass:phone)
            [5] for left 2 (exampel : email:pass:phone | 5 for save email:pass )
            [6] for lrft 3 (exampel :  user:email:pass:phone | 6 for save user:email:pass )
            
                                    : """))
            fo.write('\n')
            for line in fi:
                n += 1
                d += 1
                err = 0
                if rf == 0:
                    fo.write(line.split(spc)[rf]+'\n')
                elif rf == 1:
                    try:
                        fo.write(line.split(spc)[rf])
                    except IndexError:
                        err += 1
                        #print("error")
                elif rf == 4:
                    l = line.split(spc)
                    try:
                        fo.write(l[1]+spc+l[2]+spc+l[3])
                    except IndexError:
                        err += 1
                elif rf == 5:
                    l = line.split(spc)
                    try:
                        fo.write(l[0]+spc+l[1]+'\n')
                    except IndexError:
                        err += 1
                elif rf == 6:
                    l = line.split(spc)
                    try:
                        fo.write(l[0]+spc+l[1]+spc+l[2])
                    except IndexError:
                        err += 1
                else:
                    try:
                        fo.write(line.split(spc)[rf])
                    except IndexError:
                        err += 1
                if d == 1000000:
                    print('\t\t %s line splited...' % '{:,}'.format(n))
                    d = 0
                    fo.flush()
            fo.close()
            print('\n\t FINISHED all lines  %s  | ERRORS : %s ' % ('{:,}'.format(n),err))
            n = 0
            d = 0
        if mode == 2:
            f = input('Pleas Enter Your File Neme : ')
            fi = open(f , 'r',encoding='latin1',errors='ignore')
            fo = open('res__'+f,'a',encoding='UTF-8',errors='ignore')
            dop = 0
            sv = 0
            dic = dict()
            for line in fi:
                n += 1
                d += 1
                if line.strip() in dic:
                    dic[line.strip()] += 1
                    dop += 1
                else:
                    dic[line.strip()] = 1
                if d == 1000000:
                    d = 0
                    print('Prossing :.... %s  line ' % '{:,}'.format(n))
            print('\n\t\t prossed %s lines' % n)
            fo.write('\n')
            for save in dic:
                #print(save)
                fo.write(save+'\n')
                sv += 1
            print('\t all Dupplicated lines : %s  | all lines : %s | saved : %s '% ('{:,}'.format(dop),'{:,}'.format(n),'{:,}'.format(sv)))
            sv = 0
            ask = input(" ar you save dupplicated by number ? Y or N ").upper()
            if ask == 'Y':
                fo = open('res____' + f, 'a', encoding='UTF-8', errors='ignore')
                cn = int(input('Enter conter of save : '))
                cn -= 1
                for save in list(dic.keys()):
                    if dic[save] < cn:
                        fo.write(save + '\n')
                        sv += 1
                print('\t\t\t %s saved'% '{:,}'.format(sv))
            fo.close()
        if mode == 3:
                dic = dict()
                n = 0
                d = 0
                sv = 0
                f = input('Pleas Enter Your File Neme : ')
                fi = open(f, 'r', encoding='latin1', errors='ignore')
                fo = open('res__-' + f, 'a', encoding='UTF-8', errors='ignore')
                cn = int(input('Enter conter of save : '))
                for line in fi:
                    n += 1
                    d += 1
                    if line in dic:
                        dic[line] += 1
                        sv += 1
                    else:
                        dic[line] = 1
                    if d == 1000000:
                        print(n,' line prossed ..')
                        d = 0
                print('prossing finished %s lines and %s line duplicate '% (n,sv))
                sv2 = 0
                d = 0
                fo.write('\n')
                for save in list(dic.keys()):
                    d += 1
                    if cn < dic[save]:
                        fo.write(save)
                        sv2 += 1
                    if d == len(dic)/100:
                        print(d+d ,'line prossed')
                        d = 0
                print('all lines : %s | duplicated : %s | \t saved : % i ' % (n,sv,sv2) )
                fo.close()
        if mode == 4:
            typtxt = '''
            Pleas insert hash type:
            md5
            sha1
            sha256
            and more ....
                             
                        :'''
            f = input('Pleas Enter Your WordList : ')
            fi = open(f, 'r', encoding='latin1', errors='ignore')
            typ = input(typtxt)
            hashfile = input('Pleas Enter Your Hashed combo  file name   : ')
            fh = open(hashfile,'r',encoding='UTF-8',errors='ignore')
            spc = input(' Separator character? : ')
            fo = open('cracked_'+hashfile+'.txt', 'a', encoding='UTF-8', errors='ignore')
            n = 0
            d = 0
            dd = 0
            dic = dict()
            for line in fi:
                create = getattr(hashlib, typ)((line.strip()).encode()).hexdigest()
                #print(create)
                dic[create] = line.strip()
            print(len(dic),' password addet to dictionery ')
            fo.write('\n')
            for find in fh:
                if spc in find:
                    sp = find.split(spc)[1].strip()
                    if sp in dic:
                        n += 1
                        print('%s Hash craced !' % n )
                        fo.write(find.split(spc)[0]+spc+dic[sp]+'\n')
                    else:
                        d += 1
                        dd += 1
                        if dd == 1000:
                            print(d, 'Hash Not find')
                            dd = 0
            print('\t\t FINISH %s Hash Cracked\t %s  Hash Not find ' % (n,d))
            fo.close()
            ask = input('Do you want to crack the new combo list?  y OR n   :' )
            while ask != 'n':
                hashfile = input('Pleas Enter Your Hashed combo  file name   : ')
                fh = open(hashfile, 'r', encoding='UTF-8', errors='ignore')
                spc = input(' Separator character? : ')
                fo = open('cracked_' + hashfile + '.txt', 'a', encoding='UTF-8', errors='ignore')
                n = 0
                d = 0
                fo.write('\n'+hashfile+'new file \n')
                for find in fh:
                    if spc in find:
                        sp = find.split(spc)[1].strip()
                        if sp in dic:
                            n += 1
                            print('%s Hash craced !' % n)
                            fo.write(find.split(spc)[0] + spc + dic[sp] + '\n')
                        else:
                            d += 1
                            #print(d, 'Hash Not find')
                print('\t\t FINISH %s Hash Cracked\t %s  Hash Not find ' % (n, d))
                ask = input('Do you want to crack the new combo list?  y OR n   :')
                fo.close()
                dic = dict()
        mode = int(input(im))
else:
    print("closed")
