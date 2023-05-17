import glob as glob
import shutil


def common_members(in_1, in_2):
    result = [i for i in in_1 if i in in_2]
    return result


# add folders where you want the files compared
folder_1 = r"E:\_Julian_Master_ML_Learning\3cm-4cm\original_image"
folder_2 = r"E:\_Julian_Master_ML_Learning\3cm-4cm\json"

# initialize inputs
input_1 = []
input_2 = []

# read images from path
in_1_folder = folder_1 + "/*.tif"  # TODO: build possibility to have different file extensions
for in_1 in glob.glob(in_1_folder):
    input_1.append(in_1)

# read json files from path
in_2_folder = folder_2 + "/*.json"  # TODO: build possibility to have different file extensions
for in_2 in glob.glob(in_2_folder):
    input_2.append(in_2)

# debug_point = 0

# depending on the folder enable/disbale this option - it deletes the first member of the input
input_1 = input_1[:-1]

# cut the names down to actual filenames for comparison
for element in range(len(input_1)):
    input_1[element] = input_1[element].split(".tif")
    input_1[element] = input_1[element][0]
    input_1[element] = input_1[element].split("\\")
    input_1[element] = input_1[element][4]
# debug_point = 0
for element in range(len(input_2)):
    input_2[element] = input_2[element].split(".json")
    input_2[element] = input_2[element][0]
    input_2[element] = input_2[element].split("\\")
    input_2[element] = input_2[element][4]
    # input_2[element] = input_2[element].split("_")
    # input_2[element] = str(input_2[element][0])+"_"+str(input_2[element][1])+"_"+str(input_2[element][2])
# debug_point = 0

# call the function common_members()
result = common_members(input_1, input_2)

# copy the common files to final directory
for f in range(len(result)):
    result[f] = r"E:\_Julian_Master_ML_Learning\3cm-4cm\original_image/" + result[f] + ".tif"
    print(result[f])
    bla = 0
    shutil.copy(str(result[f]), r"E:\_Julian_Master_ML_Learning\3cm-4cm\anno_image")
bla = 0
