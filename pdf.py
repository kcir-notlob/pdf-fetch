#import urllib as u  #rick it appears that urllib does not support http 301 (file moved) and other redirections
#so swapped it for urllib2

import sys as sys
import urllib2, httplib


def getdoc(doc):
    print "hello"
    return

def readpage(url):
    urls={}
    if len(url)==0:
        print "expected url"
        return
    #f=urlopen(url[0])
    request = urllib2.Request(url[0])
    opener = urllib2.build_opener()
    f = opener.open(request)

    key='href="'

    d=f.read()

    print "found %s bytes" % len(d)



    l=d.lower()
    ix=0;
    while ix!=-1:

        ix=l.find(key,ix)
        if ix==-1:
            break
                
        iy=l.find('"',ix + 6)

        if iy==-1:
            print "could not locate end of url"
            break;

        childUrl=""


        for num in range(ix + 6,iy):
            childUrl=childUrl + l[num]

        if childUrl.find(".pdf")!=-1:    
          #print childUrl 
          urls[len(urls)]=childUrl

        ix=iy    


    print "finished" 
    return urls

def geturls(urls):
    for i in urls:
        url=urls[i]
        ix=url.rfind("/")
        if ix!=-1:
           ix=ix+1
           name=url[ix:]
        else:
            name=""

        print "url:[" + url + "]"
        print "name:[" + name  + "]"

        request = urllib2.Request(url)
        opener = urllib2.build_opener()

        try:
            f = opener.open(request)

            with open(name, "wb") as local_file:
                local_file.write(f.read())

        except:
            print "error trying to download file"


def main(arg):
    url=arg
    urls=readpage(url)
    geturls(urls)

if __name__ == "__main__":
  main(sys.argv[1:])
