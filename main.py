#需求：遍历整个文件夹的txt文档，读取第一个文档，按照。；？……处理整个文档
#统计文档有多少句子


#遍历整个文件夹的txt文档
#top[, topdown=True[, onerror=None[, followlinks=False]]]

s=[]
import os
for root, dirs, files in os.walk("./sample", topdown=False):
    for name in files:
        #print(os.path.join(root, name))
        #对每个文档进行处理，。；？……分隔
        f=open(root+'/'+name,'r',encoding='utf-8')
        for lines in f:
        #f的信息：
        # io.TextIOWrapper name='./sample/000001平安银行：2017年企业社会责任报告2018-03-15.txt'
        # mode='r' encoding='cp936'
        #else:
            #.replace(' ','')
            ls=lines.strip('\n').replace(' ','').replace('。','。\n').replace('?','?\n').replace('；','；\n').replace('\r\n','').split('/')
            for i in ls:
                s.append(i)
    f.close()
        #print(s)
f1=open(root+'/'+name,'w',encoding='utf-8')
for j in s:
    f1.write(j+'\n')
    f1.close()

        #统计文档有多少句子



