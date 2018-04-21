import os

def listFile(childPath = ''):

    path = "/Users/gengzhibo/Desktop" + "/" + childPath
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


    # print(fileList)

    return isDirList , isFilelist, parentPath
    # return fileList

# listFile()