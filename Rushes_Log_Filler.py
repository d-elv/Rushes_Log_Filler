import os, datetime, pyperclip

def getFolderSize(folder):
    total_size = os.path.getsize(folder)
    for item in os.listdir(folder):
        itempath = os.path.join(folder, item)
        if os.path.isfile(itempath):
            total_size += os.path.getsize(itempath)
        elif os.path.isdir(itempath):
            total_size += getFolderSize(itempath)
    return total_size

def getFileCount(folder):
    fileCount = 1
    for item in os.listdir(folder):
        itempath = os.path.join(folder, item)
        if os.path.isfile(itempath):
            fileCount += 1
    return fileCount

directoryToScan = input('Please drag the folder containing the rolls that require logging: ')

fileListinRoll = []
rollList = []
dirsList = []
rollSpecifier = ''
rollDirList = []
rootSplit = []
dirsSplit = []
firstFile = ''
lastFile = ''

rejectFiles = ['.DS_Store', 'Thumbs.db']
acceptedFiles = ['.mxf', '.mov', '.mp4', '.avi', '.vob', '.wav', '.aif', '.mp3', '.png', '.tif', '.jpg']

for root, path, file in os.walk(directoryToScan):
    rollDirList.append(root)
    for f in file:
        file_path = os.path.join(root + os.sep + f)
        name, ext = os.path.splitext(f)
        ext = ext.lower()
        if ext in acceptedFiles:
            fileListinRoll.append(f)
            fileListinRoll.sort()
            # Finds the first file and the last file
            firstFile = fileListinRoll[0]
            lastFile = fileListinRoll[-1]

# Finds the roll name
currentRoll = rollDirList[0]
currentRoll = currentRoll.split('/')
currentRoll = currentRoll[-1]

# Gives you the size of the roll
dirSize = getFolderSize(directoryToScan)
dirSize = dirSize / 1000000

fileCount = getFileCount(directoryToScan)

# Gives you the output of one roll, ready to paste into an excel doc
print(currentRoll + '\t' + str(dirSize) + '\t' + str(fileCount) + '\t' + firstFile + '\t' + lastFile )

# Test Commit

# for dirs in os.listdir(directoryToScan):
#     if dirs not in rejectFiles:
#         rollList.append(dirs)
#         rollSpecifier = str(dirs + '/')
#     for root, dir, files in os.walk(directoryToScan):
#         if dirs in root and rollSpecifier not in root:
#             rollDirList.append(root)
# for root, dirs, files in os.walk(rollDirList):
#     print(files)

    # rollNamepath = os.path.join(root, dirs)
    # print(dirs[0])
    # dirsSplit = str(dirs[0]).split()
    # print(dirsSplit)
    # print(rollNamepath)
    # if root == directoryToScan:


        # if root != directoryToScan:



# for root, path, file in os.walk(directoryToScan):
#     for f in file:
#         file_path = os.path.join(root + os.sep + f)
#         name, ext = os.path.splitext(f)
#         ext = ext.lower()
#         if ext in acceptedFiles:
#             fileListinRoll.append(f)
#             fileListinRoll.sort()
#             firstFile = fileListinRoll[0]
#             lastFile = fileListinRoll[-1]
#             rolls[dirs]['First File'] = firstFile
#             rolls[dirs]['Last File'] = lastFile