#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    with open("text.txt", "w", encoding = "utf-8") as fileptr:
        print(
            "UTF-8 is a variable-width charecter encoding used for electronic communication.",
            file = fileptr
        )
        print(
            "UTF-8 is capable of encoding all 1,112,064 valid charecter code points.",
            file = fileptr
        )
        print(
            "in unicode using one to four one-byte (8-bit) code units. ",
            file = fileptr
        )