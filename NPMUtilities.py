import logging
import  url

logging.basicConfig(format='%(levelname)s:%(message)s', filename='NPMutilities.log',level=logging.DEBUG)

def GetPackageNumOfDownloads(packageName):
    try:
        with urllib.request.urlopen('https://api.npmjs.org/downloads/range/1900-01-10:2300-01-10/' + packageName + ' ?/') as response:
           html = response.read()
    except:
        logging.debug('url is not resolved')
        logging.info('url is not resolved' + 'https://api.npmjs.org/downloads/range/1900-01-10:2300-01-10/' + packageName + ' ?/')
        return
    ConvertToString=str(html , 'utf-8')
    ResponseArr = ConvertToString.split(',')

    TotalDownloadsArr  = []
    for item in ResponseArr :
        if item.startswith("""{"downloads":"""):
            TotalDownloadsArr.append(int(item.replace('{"downloads":', '')))

    Intformat = ("{:,}".format(sum(TotalDownloadsArr)))

    return Intformat
