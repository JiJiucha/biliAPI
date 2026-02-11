from urllib import parse

def makeurl(base,path=''):
    result=parse.urljoin(base,path)
    return result
