# -*- coding: utf-8 -*-

import os,json,zipfile

class Path(object):
    '''
    遍历指定类型文件
    '''
    root=u'D:'
    attrs=['mp4','avi','mkv','wmv','mov']

    @classmethod
    def videos(cls,):
        w=os.walk(cls.root)
        for root,folder,filenames in w:
            for filename in filenames:
                if filename.rsplit('.',1)[-1] in cls.attrs:
                    filepath=u'%s/%s'%(root,filename)
                    filepath=filepath.replace('\\','/')
                    print filepath
                    yield filepath


def move(filepath):
    '''
    重命名方式剪切文件
    '''
    filename=filepath.rsplit('/',1)[1]
    newpath=Path.root + u'/' + filename
    print newpath
    os.rename(filepath,newpath)


def myzip(filepath):
    '''
    压缩文件
    '''

    folder,fullname=filepath.rsplit('/',1)
    filename,extent=fullname.rsplit('.',1)
    zippath=u'%s/%s/%s.zip'%(folder,filename,filename)
    print u'ready zip %s to %s'%(filepath,zippath)
    z = zipfile.ZipFile(zippath, 'w',allowZip64=True) 
    z.write(filepath,fullname)
    z.close()






