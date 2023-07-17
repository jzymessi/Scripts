import os
import shutil

def read_images_from_folder(folder_path):
    image_list = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg"): # 只读取jpg和png文件
            image_list.append(filename)
    return image_list

def delete_files_in_folder(folder_path):
    # 获取文件夹中的所有文件名
    file_list = os.listdir(folder_path)
    
    # 遍历文件列表并删除文件
    for file_name in file_list:
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):
            os.remove(file_path)
            
folder_NG_path_list = ["/workspace/aoi_test/05-C6/NG/","/workspace/aoi_test/06-D5/NG/","/workspace/aoi_test/11-red/NG/","/workspace/aoi_test/pad1/NG/","/workspace/aoi_test/pad3/NG/"]
folder_OK_path_list= ["/workspace/aoi_test/05-C6/OK/","/workspace/aoi_test/06-D5/OK/","/workspace/aoi_test/11-red/OK/","/workspace/aoi_test/pad1/OK/","/workspace/aoi_test/pad3/OK/"]
folder_out_NG_path_pist = ["/workspace/aoi_test/05-C6_out/","/workspace/aoi_test/06-D5_out/","/workspace/aoi_test/11-red_out/","/workspace/aoi_test/pad1_out/","/workspace/aoi_test/pad3_out/"]
folder_save_path_list = ["/workspace/aoi_test/05-C6_save/","/workspace/aoi_test/06-D5_save/","/workspace/aoi_test/11-red_save/","/workspace/aoi_test/pad1_save/","/workspace/aoi_test/pad3_save/"]
for folder_NG_path,folder_OK_path,folder_out_NG_path,folder_save_path in zip(folder_NG_path_list,folder_OK_path_list,folder_out_NG_path_pist,folder_save_path_list):
    print('***********',folder_NG_path," ",folder_OK_path," ",folder_out_NG_path,'***********')
    folder_NG_images = read_images_from_folder(folder_NG_path)
    len_NG = len(folder_NG_images)
    print("NG数量",len_NG)

    folder_OK_images = read_images_from_folder(folder_OK_path)
    len_OK = len(folder_OK_images)
    print("OK数量",len_OK)

    folder_out_NG_images = read_images_from_folder(folder_out_NG_path)
    len_out_NG = len(folder_out_NG_images)
    print("out_NG数量",len_out_NG)

    set1 = set(folder_NG_images)
    set2 = set(folder_out_NG_images)

    wujian_files = set2.difference(set1)
    wujian = len(wujian_files)
    print("误检数量",wujian)
    print(wujian_files)
    delete_files_in_folder(os.path.join(folder_save_path,"wujian"))
    for file in wujian_files:
        file_source_path = os.path.join(folder_out_NG_path,file)
        file_save_path = os.path.join(folder_save_path,"wujian",file)
        shutil.copy(file_source_path,file_save_path)
        

    loujian_files = set1.difference(set2)
    loujian = len(loujian_files)
    print("漏检数量",loujian)
    print(loujian_files)
    delete_files_in_folder(os.path.join(folder_save_path,"loujian"))
    for file in loujian_files:
        file_source_path = os.path.join(folder_NG_path,file)
        file_save_path = os.path.join(folder_save_path,"loujian",file)
        shutil.copy(file_source_path,file_save_path)



