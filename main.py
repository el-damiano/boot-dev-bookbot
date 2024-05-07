#!/usr/bin/env python

def count_words(input: str) -> int:
    return len(input.split())

def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
        print(f"total word count: {count_words(file_contents)}")

if __name__ == "__main__":
    main()
