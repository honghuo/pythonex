import zipfile,os,shutil
import datetime
filename = r"attach_file/"+ datetime.datetime.now().date().isoformat()
filelist = []
if os.path.isdir(filename):
    pass
else:
    os.mkdir(filename)
shutil.copy(r"E:\codings\ancunbase\testcase\add_product.csv",filename)
shutil.copy(r"E:\codings\ancunbase\report\2016-09-18-17_32_38.html",filename)
shutil.copy(r"E:\codings\ancunbase\log\2016-09-18.txt",filename)
f = zipfile.ZipFile('attach_file/'+datetime.datetime.now().date().isoformat()+'.rar','w',zipfile.ZIP_DEFLATED)
for root,dirs,files in os.walk(filename):
    print "root:"+root
    print dirs,files
    for name in files:
        filelist.append(os.path.join(root,name))
for tar in filelist:
    arcname = tar[len(filename):]
    print "arcname:"
    print arcname
    f.write(tar,arcname)
f.close()
