#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#open the file2.txt in read mode. causes error if no such file exists.
with open("file2.txt", "r") as fileptr:
    content = fileptr.readlines()
    print(content)