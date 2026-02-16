# Copyright (c) 2025 JiJiucha
# Licensed under the MIT License (see LICENSE file for details)

from urllib import parse

def makeurl(base,path=''):
    result=parse.urljoin(base,path)
    return result
