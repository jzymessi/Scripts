def random_copyfile(srcPath, dstPath):
    for dir_info in os.walk(srcPath):
        dir_name, _, file_names = dir_info
        temp = []
        for file_name in file_names:
            temp.append(file_name)
        if len(temp) == 0:
            continue
        randomfile = random.choice(temp)

        I = Image.open(os.path.join(dir_name, randomfile))
        I.save(os.path.join(dstPath, temp[0]))


if __main__ == '__main__':
    srcPath = './/img'
    dstPath = './/all_img'

    random_copyfile(srcPath, dstPath)