import os

def listFile(childPath = ''):

    path = "/service/images" + "/" + childPath
    parentPath = "/" + childPath
    fileList = os.listdir(path)
    isDirList =[]
    isFilelist = []
    for checkFile in fileList:
        if os.path.isdir(path + "/" + checkFile):
            # print checkFile + " is dir"
            isDirList.insert(0 , checkFile)
        else :
            isFilelist.insert(0 , checkFile)
            # print checkFile + " is not dir"
    isDirList.sort()
    isFilelist.sort()
    # print(fileList)

    return isDirList , isFilelist, parentPath
    # return fileList

# listFile()
