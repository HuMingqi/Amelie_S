from PIL import Image
import glob

def saveSize(filepath,imageDir):     #imageDir ͼƬͨ����ʽ
    imgDirLi=glob.glob(imageDir)     #�б�˳��һ����windows����,���ַ����ֵ�������,imageDir��һ��ģʽ��/*.jgp
    dic={}        
    for imgpath in imgDirLi:
        #print(imgpath)
        img=Image.open(imgpath)    
        imgName=imgpath.split('\\')[-1]         #python Ĭ�ϵ�·���ָ��� \   
        sli=[]
        sli.append(img.size[0])                 #img.size ���ص� tuple ����Ϊlist,json.loads���ֱ���±�����
        sli.append(img.size[1])
        dic[imgName]=sli             #�ֵ����򵫲���������޷�ȷ�������򣬵�����ȷ����λ��
        #sli.clear()                 #����Ҳ���ˣ�����        
        
    sizestr="{"
    for key,value in dic.items():
        sizestr+='"%s":%s,'%(key,value)
    sizestr=sizestr[:-1]                    #ȥĩβ���ţ�����json���ز���
    sizestr+="}"
    imgSize=open(filepath,'w')
    imgSize.write(sizestr)
    imgSize.close()
    return 'ok'