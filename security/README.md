# JavaScript NPM validateion - Security

Many JavaScript developers are using NPM (Node Package Manager); since NPM include public packages that can be uploaded by any user, it becomes a secrity risk.

This small application here will list all the packages inside 'package.json' file for the entire source tree. 
The application will list all the imported packages with the number of total downloads for each package. 
At that point, any package that has a relatively small number of downloads is suspected as a fake package.

The application can be used as a commit\push Git hook or as a post-checkout code validation step within a pipeline.

Usage: copy NPMvalidate.py and NPMUtilities.py to the root of the source tree. execute 'python NPMvalidate.py' 
the application is developed for pythin 3.*




List of example "fake" NPM packages:

babelcli: 42   -   
cross-env.js: 43   -   
crossenv: 679   -   
d3.js: 72   -   
fabric-js: 46   -   
ffmepg: 44   -   
gruntcli: 67   -   
http-proxy.js: 41   -   
jquery.js: 136   -   
mariadb: 92   -   
mongose: 196   -   
mssql-node: 46   -   
mssql.js: 48   -   
mysqljs: 77   -   
node-fabric: 87   -   
node-opencv: 94   -   
node-opensl: 40   -   
node-openssl: 29   -   
node-sqlite: 61   -   
node-tkinter: 39   -   
nodecaffe: 40   -   
nodefabric: 44   -   
nodeffmpeg: 39   -   
nodemailer-js: 40   -   
nodemailer.js: 39   -   
nodemssql: 44   -   
noderequest: 40   -   
nodesass: 66   -   
nodesqlite: 45   -   
opencv.js: 40   -   
openssl.js: 43   -   
proxy.js: 43   -   
shadowsock: 40   -   
smb: 40   -   
sqlite.js: 48   -   
sqliter: 45   -   
sqlserver: 50   -   
tkinter: 45   -   
