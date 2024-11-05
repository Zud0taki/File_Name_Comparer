import glob as glob
import shutil
import os
import time
import getopt
import sys


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# method to collect arguments from user
def collect_args(argv):
    input1: str = ''
    input2: str = ''
    output: str = ''
    try:
        opts, args = getopt.getopt(argv, "hi:c:o:", ["in1=", "in2=", "out="])
    except getopt.GetoptError:
        print("StartCollection.py -i <inputpath> -c <outputpath>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print("StartCollection.py -i <inputpath> -c <outputpath>")
            sys.exit()
        elif opt in ("-i", "-in1"):
            input1 = arg
        elif opt in ("-c", "in2"):
            input2 = arg
        elif opt in ("-o", "out"):
            output = arg
    print(f"{bcolors.OKBLUE}INFO | path to input is:{bcolors.ENDC}")
    print(input1)
    print(f"{bcolors.OKBLUE}INFO | path to output is:{bcolors.ENDC}")
    print(input2)
    print(f"{bcolors.OKBLUE}INFO | path to output is:{bcolors.ENDC}")
    print(output)
    return input1, input2, output


def common_members(in_1, in_2):
    result = []
    pos = []
    for i in range(len(in_1)):
        for l in range(len(in_2)):
            if in_1[i] == in_2[l]:
                result.append(i)
                if len(in_1) > len(in_2):
                    pos.append(i)
                elif len(in_1) < len(in_2):
                    pos.append(l)
    # result = [i for i in in_1 if i in in_2]
    return result, pos


if __name__ == "__main__":
    tac = time.time()
    input_path_1, input_path_2, output = collect_args(sys.argv[1:])

    # initialize inputs
    input_1 = []
    input_2 = []

    for dirpath, dirnames, filenames in os.walk(input_path_1):
        for filename in [f for f in filenames if f.endswith(".macs")]:
            input_1.append(os.path.join(dirpath, filename))
    for dirpath, dirnames, filenames in os.walk(input_path_2):
        for filename in [f for f in filenames if f.endswith(".tif")]:
            input_2.append(os.path.join(dirpath, filename))
    stop = 0
    decider = ""
    if len(input_1) > len(input_2):
        input_copy = list(input_1)
        decider = "in1"
    elif len(input_1) < len(input_2):
        input_copy = list(input_2)
        decider = "in2"
    if len(input_1) == len(input_2):
        input_copy = list(input_1)
        decider = "even"
    # cut the names down to actual filenames for comparison
    for element in range(len(input_1)):
        input_1[element] = input_1[element].split("\\")
        picker = len(input_1[element]) - 1
        input_1[element] = input_1[element][picker]
        input_1[element] = input_1[element].split(".")
        input_1[element] = input_1[element][0]

    for element in range(len(input_2)):
        input_2[element] = input_2[element].split("\\")
        picker = len(input_2[element]) - 1
        input_2[element] = input_2[element][picker]
        input_2[element] = input_2[element].split(".")
        input_2[element] = input_2[element][0]

    # call the function common_members()
    result, pos = common_members(input_1, input_2)

    # copy the common files to final directory
    for f in range(len(result)):
        # print(input_copy[pos[f]])
        print(f"{bcolors.WARNING}PROCESS | " + str(f + 1) + "/" + str((len(result))) + " copying the following file:  " + str(input_copy[pos[f]]) + f"{bcolors.ENDC}")
        shutil.copy(input_copy[pos[f]], output)
    tic = time.time()
    print(f"{bcolors.OKGREEN}FINISHED | found the following number of overlap: " + str(len(result)) + f"{bcolors.ENDC}")
    print(f"{bcolors.OKGREEN}FINISHED | time needed for processing: " + str("%.3f" % (tic-tac)) + "s" + f"{bcolors.ENDC}")
