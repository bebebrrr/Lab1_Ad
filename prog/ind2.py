#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def analyze_file(filename):
    wcounts = {}

    with open(filename, "r") as file:
        for line in file:
            words = line.split()
            for word in words:
                word = word.lower()
                if word:
                    if word in wcounts:
                        wcounts[word] += 1
                    else:
                        wcounts[word] = 1

    wmost = max(wcounts, key=wcounts.get)
    f = wcounts[wmost]

    return wmost, f


def main():
    filename = input("Введите имя файла для обработки: ")
    wmost, f = analyze_file(filename)

    print(f"Слово '{wmost}' встречается чаще всего - {f} раз(а).")


if __name__ == "__main__":
    main()
