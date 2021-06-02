s=[]
import os
for root, dirs, files in os.walk("./sample", topdown=False):
    for name in files:
        #print(os.path.join(root, name))
        #对每个文档进行处理，。；？……分隔
        f=open(root+'/'+name,'r',encoding='utf-8')
        for lines in f:
