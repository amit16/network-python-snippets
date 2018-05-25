"====[ Make the 80th column stand out ]====================
highlight ColorColumn ctermbg=magenta
call matchadd('ColorColumn', '\%81v', 100)

"====[ Tab Settings ]====================
"set tabstop=4       " The width of a TAB is set to 4.
"                    " Still it is a \t. It is just that
"                    " Vim will interpret it to be having
"                    " a width of 4.
"
"set shiftwidth=4    " Indents will have a width of 4
"
"set softtabstop=4   " Sets the number of columns for a TAB
"
"set expandtab       " Expand TABs to spaces

" configure expanding of tabs for various file types
au BufRead,BufNewFile *.py set expandtab
au BufRead,BufNewFile *.c set noexpandtab
au BufRead,BufNewFile *.h set noexpandtab
au BufRead,BufNewFile Makefile* set noexpandtab

" ------------------------------------------------------------------------------ 
" configure editor with tabs and nice stuff...
" ------------------------------------------------------------------------------ 
set expandtab           " enter spaces when tab is pressed
set textwidth=120       " break lines when line length increases
set tabstop=4           " use 4 spaces to represent tab
set softtabstop=4
set shiftwidth=4        " number of spaces to use for auto indent
set autoindent          " copy indent from current line when starting a new line 
filetype indent on

" make backspaces more powerfull
set backspace=indent,eol,start

set ruler                           " show line and column number
syntax on               " syntax highlighting
set showcmd             " show (partial) command in status line

" Enter a new line
nmap <S-Enter> O<Esc>
nmap <CR> o<Esc>

" Search settings
set hlsearch
set incsearch

colo delek
set t_Co=256
