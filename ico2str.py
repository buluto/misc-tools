#-------------------------------------------------------------------------------
# Name:        ICO2STR
# Purpose:     Convert an ICO file to a Base64 encoded string and vice versa
# Version:     1.0
#
# Author:      Bulut Ozturk < firstname dot lastname at gmail dot com >
#
# Created:     05/12/2014
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

import base64,os,sys

def main():

    # Argument check
    try:
        arg1 = sys.argv[1]
    except:
        print('No file given!')
        os.system('pause')
        sys.exit(0)

    # Extension check (Poor man's file type check)

    # Input is an ICO file
    if   arg1[-4:].lower() == '.ico':
        imgfile = open(arg1, "rb")
        strtext = base64.b64encode(imgfile.read())
        imgfile.close()

        strfile = open(arg1[:-4]+'.txt','wb')
        strfile.write(strtext)
        strfile.close()

    # Input is a TXT file
    elif arg1[-4:].lower() == '.txt':
        strfile = open(arg1, "rb")
        imgtext = base64.b64decode(strfile.read())
        strfile.close()

        imgfile = open(arg1[:-4]+'.ico','wb')
        imgfile.write(imgtext)
        imgfile.close()

    # Input is neither an ICO nor a TXT file
    else:
        print('Not an ICO or TXT file!')
        os.system('pause')
        sys.exit(0)

if __name__ == '__main__':
    main()
