#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import secrets
import string
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("the password length is not given!", file=sys.stderr)
        sys.exit()

    chars = string.ascii_letters + string.punctuation + string.digits
    length_pwd = int(sys.argv[1])

    result = []
    for _ in range(length_pwd):
        idx = secrets.SystemRandom().randrange(len(chars))
        result.append(chars[idx])

    print(f"secrets password: {''.join(result)}")
