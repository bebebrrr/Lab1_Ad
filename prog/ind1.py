#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def read_sentences_from_file(file2):
    with open("file2.txt", 'r') as file:
        text = file.read()
        sentences = text.split('.')
        reversed_sentences = list(reversed(sentences))
        return reversed_sentences


def main():
    filename = 'file2.txt'  
    reversed_sentences = read_sentences_from_file(filename)

    for sentence in reversed_sentences:
        print(sentence + '.')


if __name__ == '__main__':
    main()