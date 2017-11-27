import xlrd
import codecs
import os

def CreatTxt(num,value):
    if num < 1:
        return False
    else:
        f = codecs.open("%s.txt"%(num),"w",'utf-8')
        f.write(value)
        f.close()

data = xlrd.open_workbook('1.xlsx')
table = data.sheets()[0]
nrows = table.nrows
ncols = table.ncols
count = 0
path500 = "E:\\code_practice\\Atom\\hello\\%s"%(500)
path400 = "E:\\code_practice\\Atom\\hello\\%s"%(400)
if __name__ == '__main__':
    for i in range(nrows):
        for j in range(ncols):
            content = table.cell(i,j).value
            length = len(content)
            # 根据字数建立文件夹
            if length > 500 :
                isExists=os.path.exists(path500)
                if not isExists:
                    os.makedirs(path500)
                    pass
                count = count + 1
                os.chdir(r'%s'%path500)
                CreatTxt(count,content)
            elif length > 400:
                isExists=os.path.exists(path400)
                if not isExists:
                    os.makedirs(path400)
                    pass
                count = count + 1
                os.chdir(r'%s'%path400)
                CreatTxt(count,content)
