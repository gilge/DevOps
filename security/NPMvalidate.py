import NPMUtilities
import os
import fnmatch

# search package.json for packages

PackegesArr = []
projectroot = '.' # replace with parameter ARGV

###
### search jason files to scan
###
def GetpackgeJsonFileslist(rootdir):
    FilesArr = []
    for dirpath, dirnames, files in os.walk(rootdir):
        for name in files:
            if fnmatch.fnmatch(name,'package.json'):
                FilesArr.append(os.path.join(dirpath, name))
    return FilesArr

###
### extract the packages name from jason file, the files are listed by "GetpackgeJsonFileslist" def
def ReadpackagesFromFile(FileName):
    with open(FileName) as f:
        lines = f.readlines()
        startRead = False
        localPackageArr = []
        for line in lines:
            if startRead == True:
                lineFormat = line.split(':')
                localPackageArr.append(lineFormat[0].strip().replace('"',''))
            if line.strip().startswith(""""devDependencies":""") or line.strip().startswith(""""Dependencies":"""):
                startRead = True
            if startRead == True and line.strip() == '},':
                startRead = False
        del localPackageArr[-1]
        return(localPackageArr)

####
## build a list of packages, making sure that a package is no appear twice
####
for file in GetpackgeJsonFileslist(projectroot):
        for package in ReadpackagesFromFile(file):
            if package not in PackegesArr:
                PackegesArr.append(package)

for packageName in PackegesArr:
    print ("Package Name: %s : %s " % (packageName,  NPMUtilities.GetPackageNumOfDownloads(packageName) ))
