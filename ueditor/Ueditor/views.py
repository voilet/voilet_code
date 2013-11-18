#coding:utf-8
'''
Created on 2012-8-29
@author: Administrator
'''
from mysite import settings
from django.core.context_processors import csrf
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_exempt
from PIL import Image
import base64
import os
import time
import urllib2
import uuid

def testueditor(request):   
    context={}
    context.update(csrf(request))   
    return render_to_response('op_add.html',context,context_instance=RequestContext(request))


def __myuploadfile(fileObj, source_pictitle, source_filename,fileorpic='pic'):
    """ 一个公用的上传文件的处理 """
    myresponse=""
    if fileObj:
        filename = fileObj.name.decode('utf-8', 'ignore')
        fileExt = filename.split('.')[1]
        file_name = str(uuid.uuid1())
        subfolder = time.strftime("%Y%m")
        if not os.path.exists(settings.MEDIA_ROOT[0] + subfolder):
            os.makedirs(settings.MEDIA_ROOT[0] + subfolder)
        path = str(subfolder + '/' + file_name + '.' + fileExt)
        
        if fileExt.lower() in ('jpg', 'jpeg', 'bmp', 'gif', 'png',"rar" ,"doc" ,"docx","zip","pdf","txt","swf","wmv"):
        
            phisypath = settings.MEDIA_ROOT[0] + path
            destination = open(phisypath, 'wb+')
            for chunk in fileObj.chunks():
                destination.write(chunk)            
            destination.close()
            
            if fileorpic=='pic':
                if fileExt.lower() in ('jpg', 'jpeg', 'bmp', 'gif', 'png'):
                    im = Image.open(phisypath)
                    im.thumbnail((720, 720))
                    im.save(phisypath)
                    
            real_url = '/static/upload/' + subfolder + '/' + file_name + '.' + fileExt
            myresponse = "{'original':'%s','url':'%s','title':'%s','state':'%s'}" % (source_filename, real_url, source_pictitle, 'SUCCESS')
    return myresponse


@csrf_exempt
def ueditor_ImgUp(request): 
    """ 上传图片 """   
    fileObj = request.FILES.get('upfile', None)   
    source_pictitle = request.POST.get('pictitle','')
    source_filename = request.POST.get('fileName','')  
    response = HttpResponse()  
    myresponse = __myuploadfile(fileObj, source_pictitle, source_filename,'pic')
    response.write(myresponse)
    return response
   
    
@csrf_exempt
def ueditor_FileUp(request): 
    """ 上传文件 """   
    fileObj = request.FILES.get('upfile', None)   
    source_pictitle = request.POST.get('pictitle','')
    source_filename = request.POST.get('fileName','')    
    response = HttpResponse()  
    myresponse = __myuploadfile(fileObj, source_pictitle, source_filename,'file')
    response.write(myresponse)
    return response

@csrf_exempt 
def ueditor_ScrawUp(request):
    """ 涂鸦文件,处理 """
    print request
    param = request.POST.get("action",'')
    fileType = [".gif" , ".png" , ".jpg" , ".jpeg" , ".bmp"];
    
    if  param=='tmpImg':
        fileObj = request.FILES.get('upfile', None)   
        source_pictitle = request.POST.get('pictitle','')
        source_filename = request.POST.get('fileName','')  
        response = HttpResponse()  
        myresponse = __myuploadfile(fileObj, source_pictitle, source_filename,'pic')
        myresponsedict=dict(myresponse)
        url=myresponsedict.get('url','')
        response.write("<script>parent.ue_callback('%s','%s')</script>" %(url,'SUCCESS'))
        return response
    else:
        #========================base64上传的文件======================= 
        base64Data = request.POST.get('content','')
        subfolder = time.strftime("%Y%m")
        if not os.path.exists(settings.MEDIA_ROOT[0] + subfolder):
            os.makedirs(settings.MEDIA_ROOT[0] + subfolder)
        file_name = str(uuid.uuid1())
        path = str(subfolder + '/' + file_name + '.' + 'png')
        phisypath = settings.MEDIA_ROOT[0] + path        
        f=open(phisypath,'wb+')
        f.write(base64.decodestring(base64Data))
        f.close()
        response=HttpResponse()
        response.write("{'url':'%s',state:'%s'}" % ('/static/upload/' + subfolder + '/' + file_name + '.' + 'png','SUCCESS'));
        return response
        

@csrf_exempt 
def ueditor_getRemoteImage(request):
    print request
    """ 把远程的图抓到本地,爬图 """
    file_name = str(uuid.uuid1())
    subfolder = time.strftime("%Y%m")    
    if not os.path.exists(settings.MEDIA_ROOT[0] + subfolder):
        os.makedirs(settings.MEDIA_ROOT[0] + subfolder)    
    #====get request params=================================
    urls = str(request.POST.get("upfile"));
    urllist=urls.split("ue_separate_ue")
    outlist=[]
    #====request params end=================================    
    fileType = [".gif" , ".png" , ".jpg" , ".jpeg" , ".bmp"];    
    for url in urllist:
        fileExt=""
        for suffix in fileType:
            if url.endswith(suffix):
                fileExt=suffix
                break;
        if fileExt=='':
            continue
        else:
            path = str(subfolder + '/' + file_name + '.' + fileExt)
            phisypath = settings.MEDIA_ROOT[0] + path
            piccontent= urllib2.urlopen(url).read()
            picfile=open(phisypath,'wb')
            picfile.write(piccontent)
            picfile.close()
            outlist.append('/static/upload/' + subfolder + '/' + file_name + '.' + fileExt)
    outlist="ue_separate_ue".join(outlist)
    
    response=HttpResponse()
    myresponse="{'url':'%s','tip':'%s','srcUrl':'%s'}" % (outlist,'成功',urls)
    response.write(myresponse);
    return response

def listdir(path,filelist):
    """ 递归 得到所有图片文件信息 """
    phisypath = settings.MEDIA_ROOT[0]
    if os.path.isfile(path):
        return '[]' 
    allFiles=os.listdir(path)
    retlist=[]
    for cfile in allFiles:
        fileinfo={}
        filepath=(path+os.path.sep+cfile).replace("\\","/").replace('//','/')        
        
        if os.path.isdir(filepath):
            listdir(filepath,filelist)
        else:
            if cfile.endswith('.gif') or cfile.endswith('.png') or cfile.endswith('.jpg') or cfile.endswith('.bmp'):
                filelist.append(filepath.replace(phisypath,'/static/upload/').replace("//","/"))

@csrf_exempt
def ueditor_imageManager(request):
    """ 图片在线管理  """
    filelist=[]
    phisypath = settings.MEDIA_ROOT[0]
    listdir(phisypath,filelist)
    imgStr="ue_separate_ue".join(filelist)
    response=HttpResponse()
    response.write(imgStr)     
    return response

@csrf_exempt
def ueditor_getMovie(request):
    """ 获取视频数据的地址 """
    content ="";   
    searchkey = request.POST.get("searchKey");
    videotype = request.POST.get("videoType");
    try:        
        url = "http://api.tudou.com/v3/gw?method=item.search&appKey=myKey&format=json&kw="+ searchkey+"&pageNo=1&pageSize=20&channelId="+videotype+"&inDays=7&media=v&sort=s";
        content=urllib2.urlopen(url).read()
    except Exception,e:
        pass
    response=HttpResponse()  
    response.write(content);
    return response
