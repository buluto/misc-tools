#-------------------------------------------------------------------------------
# Name:        Unicodify
# Purpose:     Fix Turkish text broken by ANSI encoding
# Version:     1.0
#
# Author:      Bulut Ozturk < firstname dot lastname at gmail dot com >
#
# Created:     08/09/2014
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
        print('No file given!')
        os.system('pause')
        sys.exit(0)

    # Try UTF-8 first, fall back to ANSI if that fails
    try:
        file = open(arg1,'r',encoding='utf-8')
        text = file.read()
    except:
        file = open(arg1,'r')
        text = file.read()

    file.close()
    # Lower & uppercase   |   thorn   |  y-acute  |    eth    |.
    mktr = str.maketrans('\u00de\u00dd\u00d0\u00fe\u00fd\u00f0',
                         '\u015e\u0130\u011e\u015f\u0131\u011f')
    trns = text.translate(mktr)
    file = open(arg1,'w',encoding='utf-8')
    file.write(trns)
    file.close()

if __name__ == '__main__':
    main()
