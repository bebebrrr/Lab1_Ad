#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# open the file2.txt in append mode. Create a new file
with open("file2.txt", "w") as fileptr:
    # appending the content to the file
    fileptr.write(
        "Python is the modern day language. It makes things so simple.\n"
        "It is the fastest growing programing language."
    )
