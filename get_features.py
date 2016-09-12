import Amelie.feature_vector

objects=[
#     ("D:/Clothes Search System/PL/dress/dress_feature.txt","D:/Clothes Search System/PL/dress/dress_src/"),
#     ("D:/Clothes Search System/PL/up_clothes/up_clothes_feature.txt","D:/Clothes Search System/PL/up_clothes/up_clothes_src/"),
#     ("D:/Clothes Search System/PL/down_clothes/down_clothes_feature.txt","D:/Clothes Search System/PL/down_clothes/down_clothes_src/")
    ("C:/Users/mingq/Desktop/Temp/clothes_test/sample_feature.txt","C:/Users/mingq/Desktop/Temp/clothes_test/src_gf/")
    ]

for feature_path,images in objects :
    Amelie.feature_vector.calculate_and_save_feature_vectors(feature_path,images)   #src/ need / else output \\
