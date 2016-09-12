from urllib import request
from urllib import parse

def uploadImage():
    print('method uploadImage')
    img=open('g:/crawlerTest/dress/1_1.jpg','rb')        # rb read binary
    imgdict={'upload_image':img.read()}
    imgData=parse.urlencode(imgdict)                        # returns a string in application/x-www-form-urlencoded format
    url='http://localhost:8000/searchSimilarImages/'
    req=request.Request(url,data=imgData.encode(encoding='utf_8', errors='strict'),method="post")     #str encoded to bytes
    try:
        resp=request.urlopen(req)
    except Exception as ex:
        print(ex)
    
    print(resp.read())
    '''except request.HTTPError as e:    #HTTPError必须排在URLError的前面
        print("The server couldn't fulfill the request")    #自动换行
        print("Error code:",e.code)
        print("Return content:",print(e),e.reason)
    except request.URLError as e:
        print("Failed to reach the server")
        print("The reason:",e.reason)
    else:    
        pass  #其他异常的处理
    '''
    
