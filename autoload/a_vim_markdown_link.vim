let s:dir = expand('<sfile>:p:h')
let s:py_path = s:dir . '/' . 'a_vim_markdown_link.py'
"pyfileを指定する際にvimの変数は使えない？

function! a_vim_markdown_link#get() range
    for n in range(a:firstline, 5)
        echo "うおおおお"
    endfor


    "echo "aaa".a:firstline
    "echo "aaa".a:lastline
    " :py import vim
    " :py import sys
    " :py sys.argv[0] = <line1>
    " :py sys.argv[1] = <line2>
    " :py print sys.argv[0]
    "execute ':pyfile ' . s:py_path
endfunction

