#scan all photos in designated file
import os

#获取指定目录下的所有图片文件的文件名
def getFileName(path):
    file_list = os.listdir(path)
    #print file_list
    for i in file_list:
        if os.path.splitext(i)[1] == '.jpg' or os.path.splitext(i)[1] == '.JPG' or os.path.splitext(i)[1] == '.png' or os.path.splitext(i)[1] == '.PNG':
            #print(i)
            return i



if __name__ == '__main__':
    path = 'C:\\Users\zzh83\Desktop'
    getFileName(path)