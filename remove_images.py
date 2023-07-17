import os
# import shutil

# 定义文件夹1和文件夹2的路径
folder1_path = '/workspace/aoi_test/06-D5/NG/'
folder2_path = '/workspace/aoi_test/06-D5/OK/'

# 获取文件夹2中的文件列表
folder2_files = os.listdir(folder2_path)

# 遍历文件夹1中的文件
for file in os.listdir(folder1_path):
    file_path = os.path.join(folder1_path, file)

    # 检查文件是否存在于文件夹2中
    if file in folder2_files:
        # 如果文件存在于文件夹2中，删除文件
        os.remove(file_path)
        print(f'Removed {file_path}')


