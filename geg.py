import glob
import os

folder_1 = r"E:\Weihnachtsmarkt\findings"

input_1 = []
old_names = []
new_names = []

# read images from path
in_1_folder = folder_1 + "/*"
for in_1 in glob.glob(in_1_folder):
    input_1.append(in_1)
    old_names.append(in_1)

for element in range(len(input_1)):
    input_1[element] = input_1[element].split(".bmp")
    input_1[element] = input_1[element][0]
    input_1[element] = input_1[element].split("\\")
    input_1[element] = input_1[element][3]
    input_1[element] = input_1[element].split("_")
    new_name = r"E:/Weihnachtsmarkt/findings/" + str(input_1[element][0])+"_"+str(input_1[element][1])+"_"+str(input_1[element][2])+".bmp"
    new_names.append(new_name)
bla = 0
'E:\\Weihnachtsmarkt\\findings\\00033_000243945_1500_detection_result_2.bmp'



for i in range(len(old_names)):
    old_name = old_names[i]
    new_name = new_names[i]
    os.rename(old_name, new_name)


