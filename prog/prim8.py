#!/usr/bin/env python3
# -*- coding: utf-8 -*-

with open("file2.txt", "r") as fileptr:
    print("the filepointer is at byte:", fileptr.tell())

    fileptr.seek(10)

    print("after reading, the fillpointer is at:", fileptr.tell())
