import glob as glob
import shutil

def common_members(in_1, in_2):
    result = [i for i in in_1 if i in in_2]
    return result


folder_1 = r"E:\_Julian_Master_ML_Learning\3cm-4cm\original_image"
folder_2 = r"E:\_Julian_Master_ML_Learning\3cm-4cm\json"

input_1 = []
input_2 = []

# read images from path
in_1_folder = folder_1 + "/*"
for in_1 in glob.glob(in_1_folder):
    input_1.append(in_1)

# read json files from path
in_2_folder = folder_2 + "/*"
for in_2 in glob.glob(in_2_folder):
    input_2.append(in_2)

input_1 = input_1[:-1]

for element in range(len(input_1)):
    input_1[element] = input_1[element].split(".tif")
    input_1[element] = input_1[element][0]
    input_1[element] = input_1[element].split("\\")
    input_1[element] = input_1[element][4]
bla = 0
for element in range(len(input_2)):
    input_2[element] = input_2[element].split(".json")
    input_2[element] = input_2[element][0]
    input_2[element] = input_2[element].split("\\")
    input_2[element] = input_2[element][4]
    # input_2[element] = input_2[element].split("_")
    # input_2[element] = str(input_2[element][0])+"_"+str(input_2[element][1])+"_"+str(input_2[element][2])
bla = 0
result = common_members(input_1, input_2)

for f in range(len(result)):
    result[f] = r"E:\_Julian_Master_ML_Learning\3cm-4cm\original_image/" + result[f] + ".tif"
    print(result[f])
    bla = 0
    shutil.copy(str(result[f]), r"E:\_Julian_Master_ML_Learning\3cm-4cm\anno_image")
bla = 0

