#-------------------------------------------------------------------------------
# Name:        ASCIIfy
# Purpose:     Convert text to ASCII block text
# Version:     1.0
#
# Author:      Bulut Ozturk < firstname dot lastname at gmail dot com >
#
# Created:     10/09/2014
#-------------------------------------------------------------------------------
# This is free and unencumbered software released into the public domain.
#
# Anyone is free to copy, modify, publish, use, compile, sell, or distribute
# this software, either in source code form or as a compiled binary, for any
# purpose, commercial or non-commercial, and by any means.
#
# In jurisdictions that recognize copyright laws, the author or authors of
# this software dedicate any and all copyright interest in the software to the
# public domain. We make this dedication for the benefit of the public at large
# and to the detriment of our heirs and successors. We intend this dedication
# to be an overt act of relinquishment in perpetuity of all present and future
# rights to this software under copyright law.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
# 
# For more information, please refer to <http://unlicense.org>
#-------------------------------------------------------------------------------

import sys,os

def main():

    # Argument check
    try:
        arg1 = sys.argv[1]
    except:
        print('No input text given!')
        os.system('pause')
        sys.exit(0)

    print(convert(arg1))

def convert(rtxt):

    rpos = 0
    alst = [[] for i in range(len(rtxt))]

    for rchr in str(rtxt):
        if   rchr in 'Aa':
            achr = ' ##### \n' + \
                   '##   ##\n' + \
                   '##   ##\n' + \
                   '##   ##\n' + \
                   '#######\n' + \
                   '##   ##\n' + \
                   '##   ##\n'
        if   rchr in '\u00C4\u00E4':
            achr = '""   ""\n' + \
                   ' ##### \n' + \
                   '##   ##\n' + \
                   '##   ##\n' + \
                   '#######\n' + \
                   '##   ##\n' + \
                   '##   ##\n'
        elif rchr in 'Bb':
            achr = '###### \n' + \
                   '##   ##\n' + \
                   '##   ##\n' + \
                   '###### \n' + \
                   '##   ##\n' + \
                   '##   ##\n' + \
                   '###### \n'
        elif rchr in 'Cc':
            achr = ' ##### \n' + \
                   '##   ##\n' + \
                   '##     \n' + \
                   '##     \n' + \
                   '##     \n' + \
                   '##   ##\n' + \
                   ' ##### \n'
        elif rchr in '\u00C7\u00E7':
            achr = ' ##### \n' + \
                   '##   ##\n' + \
                   '##     \n' + \
                   '##     \n' + \
                   '##     \n' + \
                   '## $ ##\n' + \
                   ' ##### \n'
        elif rchr in 'Dd':
            achr = '###### \n' + \
                   '##   ##\n' + \
                   '##   ##\n' + \
                   '##   ##\n' + \
                   '##   ##\n' + \
                   '##   ##\n' + \
                   '###### \n'
        elif rchr in 'Ee':
            achr = '#######\n' + \
                   '##     \n' + \
                   '##     \n' + \
                   '#####  \n' + \
                   '##     \n' + \
                   '##     \n' + \
                   '#######\n'
        elif rchr in 'Ff':
            achr = '#######\n' + \
                   '##     \n' + \
                   '##     \n' + \
                   '#####  \n' + \
                   '##     \n' + \
                   '##     \n' + \
                   '##     \n'
        elif rchr in 'Gg':
            achr = ' ##### \n' + \
                   '##     \n' + \
                   '##     \n' + \
                   '##  ###\n' + \
                   '##   ##\n' + \
                   '##   ##\n' + \
                   ' ##### \n'
        elif rchr in '\u011E\u011F':
            achr = '  \\_/  \n' + \
                   ' ##### \n' + \
                   '##     \n' + \
                   '##     \n' + \
                   '##  ###\n' + \
                   '##   ##\n' + \
                   ' ##### \n'
        elif rchr in 'Hh':
            achr = '##   ##\n' + \
                   '##   ##\n' + \
                   '##   ##\n' + \
                   '#######\n' + \
                   '##   ##\n' + \
                   '##   ##\n' + \
                   '##   ##\n'
        elif rchr in 'Ii\u0131':
            achr = '  #### \n' + \
                   '   ##  \n' + \
                   '   ##  \n' + \
                   '   ##  \n' + \
                   '   ##  \n' + \
                   '   ##  \n' + \
                   '  #### \n'
        elif rchr in '\u0130':
            achr = '   ==  \n' + \
                   '  #### \n' + \
                   '   ##  \n' + \
                   '   ##  \n' + \
                   '   ##  \n' + \
                   '   ##  \n' + \
                   '  #### \n'
        elif rchr in 'Jj':
            achr = '    ###\n' + \
                   '     ##\n' + \
                   '     ##\n' + \
                   '     ##\n' + \
                   '     ##\n' + \
                   '##   ##\n' + \
                   ' ##### \n'
        elif rchr in 'Kk':
            achr = '##   ##\n' + \
                   '##  ## \n' + \
                   '## ##  \n' + \
                   '###### \n' + \
                   '##   ##\n' + \
                   '##   ##\n' + \
                   '##   ##\n'
        elif rchr in 'Ll':
            achr = '##     \n' + \
                   '##     \n' + \
                   '##     \n' + \
                   '##     \n' + \
                   '##     \n' + \
                   '##     \n' + \
                   '#######\n'
        elif rchr in 'Mm':
            achr = '##   ##\n' + \
                   '##   ##\n' + \
                   '### ###\n' + \
                   '## # ##\n' + \
                   '##   ##\n' + \
                   '##   ##\n' + \
                   '##   ##\n'
        elif rchr in 'Nn':
            achr = '##   ##\n' + \
                   '##   ##\n' + \
                   '###  ##\n' + \
                   '## # ##\n' + \
                   '##  ###\n' + \
                   '##   ##\n' + \
                   '##   ##\n'
        elif rchr in 'Oo':
            achr = '  #### \n' + \
                   ' ##  ##\n' + \
                   '##   ##\n' + \
                   '##   ##\n' + \
                   '##   ##\n' + \
                   '##  ## \n' + \
                   ' ####  \n'
        elif rchr in '\u00D6\u00F6':
            achr = ' ""  ""\n' + \
                   '  #### \n' + \
                   ' ##  ##\n' + \
                   '##   ##\n' + \
                   '##   ##\n' + \
                   '##  ## \n' + \
                   ' ####  \n'
        elif rchr in 'Pp':
            achr = '###### \n' + \
                   '##   ##\n' + \
                   '##   ##\n' + \
                   '###### \n' + \
                   '##     \n' + \
                   '##     \n' + \
                   '##     \n'
        elif rchr in 'Qq':
            achr = '  #### \n' + \
                   ' ##  ##\n' + \
                   '##   ##\n' + \
                   '##   ##\n' + \
                   '## # ##\n' + \
                   '##  ## \n' + \
                   ' #### #\n'
        elif rchr in 'Rr':
            achr = '###### \n' + \
                   '##   ##\n' + \
                   '##   ##\n' + \
                   '###### \n' + \
                   '##   ##\n' + \
                   '##   ##\n' + \
                   '##   ##\n'
        elif rchr in 'Ss':
            achr = ' ##### \n' + \
                   '##   ##\n' + \
                   '##     \n' + \
                   ' ##### \n' + \
                   '     ##\n' + \
                   '##   ##\n' + \
                   ' ##### \n'
        elif rchr in '\u00DF':
            achr = ' ####  \n' + \
                   '##  ## \n' + \
                   '##  ## \n' + \
                   '## ##  \n' + \
                   '##  ## \n' + \
                   '##   ##\n' + \
                   '## ### \n'
        elif rchr in '\u015E\u015F':
            achr = ' ##### \n' + \
                   '##   ##\n' + \
                   '##     \n' + \
                   ' ##### \n' + \
                   '     ##\n' + \
                   '## $ ##\n' + \
                   ' ##### \n'
        elif rchr in 'Tt':
            achr = '#######\n' + \
                   '  ##   \n' + \
                   '  ##   \n' + \
                   '  ##   \n' + \
                   '  ##   \n' + \
                   '  ##   \n' + \
                   '  ##   \n'
        elif rchr in 'Uu':
            achr = '##   ##\n' + \
                   '##   ##\n' + \
                   '##   ##\n' + \
                   '##   ##\n' + \
                   '##   ##\n' + \
                   '##   ##\n' + \
                   ' ##### \n'
        elif rchr in '\u00DC\u00FC':
            achr = '""   ""\n' + \
                   '##   ##\n' + \
                   '##   ##\n' + \
                   '##   ##\n' + \
                   '##   ##\n' + \
                   '##   ##\n' + \
                   ' ##### \n'
        elif rchr in 'Vv':
            achr = '##   ##\n' + \
                   '##   ##\n' + \
                   '##   ##\n' + \
                   '##   ##\n' + \
                   '##   ##\n' + \
                   ' ## ## \n' + \
                   '  ###  \n'
        elif rchr in 'Ww':
            achr = '##   ##\n' + \
                   '##   ##\n' + \
                   '##   ##\n' + \
                   '##   ##\n' + \
                   '## # ##\n' + \
                   '### ###\n' + \
                   '##   ##\n'
        elif rchr in 'Xx':
            achr = '##   ##\n' + \
                   '##   ##\n' + \
                   ' ## ## \n' + \
                   '  ###  \n' + \
                   ' ## ## \n' + \
                   '##   ##\n' + \
                   '##   ##\n'
        elif rchr in 'Yy':
            achr = '##   ##\n' + \
                   '##   ##\n' + \
                   '##   ##\n' + \
                   ' ## ## \n' + \
                   '  ##   \n' + \
                   '  ##   \n' + \
                   '  ##   \n'
        elif rchr in 'Zz':
            achr = '#######\n' + \
                   '     ##\n' + \
                   '    ## \n' + \
                   '   ##  \n' + \
                   '  ##   \n' + \
                   ' ##    \n' + \
                   '#######\n'
        elif rchr in '0':
            achr = ' ##### \n' + \
                   '##   ##\n' + \
                   '##  ###\n' + \
                   '## ####\n' + \
                   '#### ##\n' + \
                   '###  ##\n' + \
                   ' ##### \n'
        elif rchr in '1':
            achr = '    ## \n' + \
                   '  #### \n' + \
                   '    ## \n' + \
                   '    ## \n' + \
                   '    ## \n' + \
                   '    ## \n' + \
                   '    ## \n'
        elif rchr in '2':
            achr = ' ##### \n' + \
                   '##   ##\n' + \
                   '    ## \n' + \
                   '   ##  \n' + \
                   '  ##   \n' + \
                   ' ##    \n' + \
                   '#######\n'
        elif rchr in '3':
            achr = ' ##### \n' + \
                   '##   ##\n' + \
                   '     ##\n' + \
                   '  #### \n' + \
                   '     ##\n' + \
                   '##   ##\n' + \
                   ' ##### \n'
        elif rchr in '4':
            achr = '     ##\n' + \
                   '    ## \n' + \
                   '   ##  \n' + \
                   '  ##   \n' + \
                   ' ##  ##\n' + \
                   '#######\n' + \
                   '     ##\n'
        elif rchr in '5':
            achr = '#######\n' + \
                   '##     \n' + \
                   '##     \n' + \
                   '###### \n' + \
                   '     ##\n' + \
                   '     ##\n' + \
                   '###### \n'
        elif rchr in '6':
            achr = ' ##### \n' + \
                   '##     \n' + \
                   '##     \n' + \
                   '###### \n' + \
                   '##   ##\n' + \
                   '##   ##\n' + \
                   ' ##### \n'
        elif rchr in '7':
            achr = '#######\n' + \
                   '     ##\n' + \
                   '    ## \n' + \
                   '   ##  \n' + \
                   '  ##   \n' + \
                   ' ##    \n' + \
                   '##     \n'
        elif rchr in '8':
            achr = ' ##### \n' + \
                   '##   ##\n' + \
                   '##   ##\n' + \
                   ' ##### \n' + \
                   '##   ##\n' + \
                   '##   ##\n' + \
                   ' ##### \n'
        elif rchr in '9':
            achr = ' ##### \n' + \
                   '##   ##\n' + \
                   '##   ##\n' + \
                   ' ######\n' + \
                   '     ##\n' + \
                   '     ##\n' + \
                   ' ##### \n'
        elif rchr in ' ':
            achr = '       \n' + \
                   '       \n' + \
                   '       \n' + \
                   '       \n' + \
                   '       \n' + \
                   '       \n' + \
                   '       \n'
        elif rchr in '!':
            achr = '   ##  \n' + \
                   '   ##  \n' + \
                   '   ##  \n' + \
                   '   ##  \n' + \
                   '   ##  \n' + \
                   '   ##  \n' + \
                   '   ==  \n'
        elif rchr in '?':
            achr = ' ##### \n' + \
                   '##   ##\n' + \
                   '    ## \n' + \
                   '   ##  \n' + \
                   '  ##   \n' + \
                   '  ##   \n' + \
                   '  ==   \n'
        elif rchr in ':':
            achr = '       \n' + \
                   '       \n' + \
                   '   ##  \n' + \
                   '       \n' + \
                   '   ##  \n' + \
                   '       \n' + \
                   '       \n'
        elif rchr in ';':
            achr = '       \n' + \
                   '       \n' + \
                   '   ##  \n' + \
                   '       \n' + \
                   '   ##  \n' + \
                   '  ##   \n' + \
                   '       \n'
        elif rchr in '.':
            achr = '       \n' + \
                   '       \n' + \
                   '       \n' + \
                   '       \n' + \
                   '       \n' + \
                   '       \n' + \
                   '   ##  \n'
        elif rchr in ',':
            achr = '       \n' + \
                   '       \n' + \
                   '       \n' + \
                   '       \n' + \
                   '       \n' + \
                   '   ##  \n' + \
                   '  ##   \n'
        elif rchr in '/':
            achr = '      #\n' + \
                   '     ##\n' + \
                   '    ## \n' + \
                   '   ##  \n' + \
                   '  ##   \n' + \
                   ' ##    \n' + \
                   '##     \n'
        elif rchr in '-':
            achr = '       \n' + \
                   '       \n' + \
                   '       \n' + \
                   '#######\n' + \
                   '       \n' + \
                   '       \n' + \
                   '       \n'
        elif rchr in '=':
            achr = '       \n' + \
                   '       \n' + \
                   '#######\n' + \
                   '       \n' + \
                   '#######\n' + \
                   '       \n' + \
                   '       \n'
        elif rchr in '>':
            achr = '##     \n' + \
                   ' ##    \n' + \
                   '   ##  \n' + \
                   '     ##\n' + \
                   '   ##  \n' + \
                   ' ##    \n' + \
                   '##     \n'
        elif rchr in '<':
            achr = '     ##\n' + \
                   '    ## \n' + \
                   '  ##   \n' + \
                   '##     \n' + \
                   '  ##   \n' + \
                   '    ## \n' + \
                   '     ##\n'

        alst[rpos] = achr
        rpos += 1

    atxt = ''

    for l in range (0,7):
        i = 0
        while i < len(rtxt):
            n = 0
            for c in alst[i]:
                if   c != '\n' and n == l:
                    atxt += c
                elif c == '\n' and n == l:
                    break
                elif c == '\n' and n != l:
                    n += 1
            i += 1
            atxt += '  '
        atxt += '\n'

    return atxt

if __name__ == '__main__':
    main()
