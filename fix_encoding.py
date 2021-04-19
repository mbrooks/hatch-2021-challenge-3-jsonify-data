#!/usr/bin/env python

sourceEncoding = "iso-8859-1"
targetEncoding = "utf-8"
source = open("data/DomoArigatoData.txt")
target = open("data/DomoArigatoData-utf8.txt", "w")

target.write(unicode(source.read(), sourceEncoding).encode(targetEncoding))
