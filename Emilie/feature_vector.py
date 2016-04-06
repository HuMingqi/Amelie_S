#from PIL import Image
#from PIL import ImageFile
#from numpy import *
#import colorsys
#import pygal
#from pygal.style import LightStyle
import datetime
import os
import json
import ctypes
from pack_feature_vector_cdll import *

def feature_vector_of_image(image_path):
    hsv_vector=(ctypes.c_double*24)()
    #call dll func
    get_feature_vector(hsv_vector,bytes(image_path,encoding='utf-8'))
    return list(hsv_vector)

def get_imlist(path):
    """ Returns a list of filenames for all jpg images in a directory. """
    return [os.path.join(path,f) for f in os.listdir(path) if f.endswith('.jpg')]

def save_data(filename, key_list, value_list):
    dic = dict(list(zip(key_list, value_list)))
    target = open(filename, 'w')
    target.write(json.dumps(dic))
    target.close()

def calculate_and_save_feature_vectors(filename, image_set_folder):         #计算特征库，并保存到filename（路径) use / in folder path
    image_paths = get_imlist(image_set_folder)
    image_feature_vectors = []
    #store hsv from cdll
    hsv_vector=(ctypes.c_double*24)()

    start_time = datetime.datetime.now()    
    for image_path in image_paths:
        #call dll
        get_feature_vector(hsv_vector,bytes(image_path,encoding='utf-8'))
        image_feature_vectors.append(list(hsv_vector))      #listize array        
        print(image_path)
    end_time = datetime.datetime.now()
    use_time = end_time - start_time
    print(str(use_time.seconds+use_time.microseconds/1000000.0))   

    save_data(filename, image_paths, image_feature_vectors)
    #return image_feature_vectors


'''
def feature_vector_of_image(image_path):

    # if img and img.meta_type == 'Image':
    #     pilImg = PIL.Image.open(StringIO(str(img.data)) )
    # elif imgData:
    #     pilImg = PIL.Image.open(StringIO(imgData) 
    start=datetime.datetime.now()

    try:
        img = Image.open(image_path)
    except Exception as exception:
        print(exception)
        return []
    except IOError as error:
        print(error)
        return []
    # img = Image.open('D:\\98_1.jpg')
    # !!! maybe, index out range
    # hl, sl, vl = [0]*18, [0]*3, [0]*3
    hl, sl, vl = [0]*19, [0]*4, [0]*4
    try:
        # img.load()
        # maybe RGBA, but we only need RGB, avoid too many value unpack exception        
        img_split_list = img.split()

        end=datetime.datetime.now()
        print("split time:"+str((end-start).seconds)) #0s

        r_object, g_object, b_object = img_split_list[0], img_split_list[1], img_split_list[2]
    # except Exception, e:
    #     print e
    #     return []
    except IOError:
        # print error
        return []
        
    for r, g, b in zip(r_object.getdata(), g_object.getdata(), b_object.getdata()):
        h, s, v = colorsys.rgb_to_hsv(r/255.0, g/255.0, b/255.0)    #there,hsv is percentage
        h = h*360
        hi, si, vi = int(h/20), int(s*3), int(v*3)
        hl[hi], sl[si], vl[vi] = hl[hi] + 1, sl[si] + 1, vl[vi] + 1

    end1=datetime.datetime.now()
    print("for1 time:"+str((end1-start).seconds)) #29s!!!

    # normalize
    width, height = img.size[0], img.size[1]
    pixel_num = float(width * height)
    for i in range(0,19):
        hl[i] = hl[i]/pixel_num
    for i in range(0,4):
        sl[i], vl[i] = sl[i]/pixel_num, vl[i]/pixel_num

    hsvl = hl + sl + vl

    end2=datetime.datetime.now()
    print("for2 time:"+str((end2-start).seconds)) #29s

    return hsvl
    # print hsvl
    # bar_chart = pygal.Bar(style=LightStyle)
    # bar_chart.title = ' '
    # bar_chart.x_labels = map(str, range(0, 26))
    # bar_chart.add(' ', hsvl)
    # bar_chart.render_in_browser()
    # im = array(Image.open('D:\\test.jpg'))
    # width, height = im.shape[0], im.shape[1]
    # print width, height
    # for i in xrange(0,width):
    #   for j in xrange(0,height):
    #       hsv_tuple = colorsys.rgb
'''    


