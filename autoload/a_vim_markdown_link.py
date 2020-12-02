# encoding:utf-8

#import vim
import urllib
from bs4 import BeautifulSoup
import re
import sys

#line = 'aaa[](https://ambergonslibrary.com/)'
#line = 'aaa[aaa](https://ambergonslibrary.com/)'

#line = vim.current.line
line = '[](https://ambergonslibrary.com/)[](https://ambergonslibrary.com/wordpress/vim/1867/)[](https://ambergonslibrary.com/wordpress/vim/1708/)'
r = r'(\[(?P<title>.*?)\](?P<url>\(http.+?\)))'


def check_url(line,r):

    p = re.compile(r)
    m = p.search(line)
    print m.groups()
    print p.search(line).groups()
    if m == None:
        #matchしなかった場合
        print('NO URL')
        #sys.stderr.write('NO URL')
        break
    elif m.group('title') != "" :
        print("already set title")
        break

    elif m.group('title') == "" :
        #titleが挿入されていない場合のみ
        #set_url()


def set_url():
    url = m.group('url').replace('(','').replace(')','')
      
    html = urllib.urlopen(url)
    soup = BeautifulSoup(html,"html.parser")
    text = soup.title.string
    title_text = text.encode('utf-8')

#    vim.current.line = re.sub(r'\[\]','[' + title_text + ']',line)
    print('match')
    print(re.sub(r'\[\]','[' + title_text + ']',line ,count=1))

check_url(line,r)




##test
#[](https://ambergonslibrary.com/)
#[](https://ambergonslibrary.com/wordpress/vim/1867/)
#[](https://ambergonslibrary.com/wordpress/vim/1708/)

#[](https://ambergonslibrary.com/)[](https://ambergonslibrary.com/wordpress/vim/1867/)[](https://ambergonslibrary.com/wordpress/vim/1708/)


