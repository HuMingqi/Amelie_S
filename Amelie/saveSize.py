from PIL import Image
import glob

def saveSize(filepath,imageDir):     #imageDir 图片通配表达式
    imgDirLi=glob.glob(imageDir)     #列表顺序不一定按windows那样,按字符串字典序重排,imageDir是一个模式，/*.jgp
    dic={}        
    for imgpath in imgDirLi:
        #print(imgpath)
        img=Image.open(imgpath)    
        imgName=imgpath.split('\\')[-1]         #python 默认的路径分隔符 \   
        sli=[]
        sli.append(img.size[0])                 #img.size 返回的 tuple ，改为list,json.loads后可直接下标引用
        sli.append(img.size[1])
        dic[imgName]=sli             #字典无序但不随机，你无法确定键的序，但键在确定的位置
        #sli.clear()                 #对象也清了！！！        
        
    sizestr="{"
    for key,value in dic.items():
        sizestr+='"%s":%s,'%(key,value)
    sizestr=sizestr[:-1]                    #去末尾逗号，否则json加载不了
    sizestr+="}"
    imgSize=open(filepath,'w')
    imgSize.write(sizestr)
    imgSize.close()
    return 'ok'