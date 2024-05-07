#!/usr/bin/env python

def count_words(input: str) -> int:
    return len(input.split())

def count_letters(input: str) -> dict[str, int]:
    letter_to_count = {}
    lowered_string = input.lower()

    for s in lowered_string:
        if s not in letter_to_count:
            letter_to_count[s] = 0

        letter_to_count[s] += 1
    
    return letter_to_count

def main():
    with open('books/frankenstein.txt') as f:
        print(f"--- Begin report of {f.name} ---")

        file_contents = f.read()
        print(f"{count_words(file_contents)} words found in the document")
        print(f"total letter count: {count_letters(file_contents)}")

        print('--- End report ---')


if __name__ == "__main__":
    main()
