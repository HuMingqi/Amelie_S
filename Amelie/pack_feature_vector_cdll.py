import ctypes

#locate .dll file. using absolute path in django. relative path just in python intertive mode
#!!! feature_vector depend on opencv_world310d.dll , you can include it in system32

dll_path="G:/ResearchTraining/Amelie_Server/DLLS/feature_vector.dll"
#dll_path="D:/Clothes Search System/AmelieServer/DLLS/feature_vector.dll"

dll=ctypes.CDLL(dll_path)

#void get_feature_vector(double[24],string)
get_feature_vector=dll.get_feature_vector
get_feature_vector.argtypes=(ctypes.c_double*24,ctypes.c_char_p)

#using method
'''
hsv=(c_float*24)()
get_feature_vector(hsv,bytes(image_path,encoding='utf-8'))
'''