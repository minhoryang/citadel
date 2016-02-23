from os import mkdir
from os.path import isdir, isfile
from time import sleep
from sys import argv

from . import crawl

if not isdir("output"):
    mkdir("output")
if not isdir("output/%s" % (argv[1],)):
    mkdir("output/%s" % (argv[1],))

king = None
for line in open(argv[1]):
    line = line.strip()
    if '대' in line:
        king = line
        if not isdir("output/%s/%s/" % (argv[1], king)):
            mkdir("output/%s/%s/" % (argv[1], king))
    elif '#' in line:
        pass  # XXX: ignore
    elif 'end' in line:
        pass  # XXX: ignore
    elif len(line):
        for word in line.split():
            word = word.strip()
            if word[0] == '○':
                word = word[1:]
            if word:
                name = "output/%s/%s/%s" % (argv[1], king, word)
                print(name)
                if not isfile("%s.json" % (name,)):
                    result = crawl.search(word)
                    crawl.result2json(result, "%s.json" % (name,))
                #if not isfile("%s.txt" % (name,)):
                #    crawl.json2txt("%s.json" % (name,), "%s.txt" % (name,))
                sleep(2)
    else:
        pass
