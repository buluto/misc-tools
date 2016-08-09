# misc-tools
A bunch of miscellaneous tools written in Python. All require Python 3 and nothing else.

####ico2str
Convert an ICO file to a Base64 encoded string and vice versa. Useful when you want to embed an icon into the source code. A simple wrapper around the Base64 encode/decode functions.

How to use: Pass input file (.ico or .txt) as an argument to the script. A new file will be created in the same directory as the input file. "foo.ico" produces "foo.txt" and vice versa.

```bash
python ico2str.py foo.ico
```

####unicodify
Fix Turkish text broken by ANSI encoding. Useful for subtitle files. A simple wrapper around the translate function.

How to use: Pass input file (text file with any extension) as an argument to the script. The input file will be overwritten.

```bash
python unicodify.py foo.srt
```

####asciify
Convert text to ASCII block text with 7x7 characters.

How to use: Pass input text as an argument to the script OR its ```convert()``` function.

```bash
python asciify.py "foobar"
```

OR

```python
import asciify
asciify.convert("foobar")
```
