import ctypes

#locate .dll file
dll_path="../DLLS/feature_vector.dll"
dll=ctypes.CDLL(dll_path)

#void get_feature_vector(double[24],string)
get_feature_vector=dll.get_feature_vector
get_feature_vector.argtypes=(ctypes.c_double*24,ctypes.c_char_p)

#using method
'''
hsv=(c_float*24)()
get_feature_vector(hsv,bytes(image_path,encoding='utf-8'))
'''