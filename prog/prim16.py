#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == "__main__":
    for idx, arg in enumerate(sys.argv):
        print(f"argument #{idx} is {arg}")
    print("no. of arguments passed is ", len(sys.argv))
