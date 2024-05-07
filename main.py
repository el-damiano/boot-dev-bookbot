#!/usr/bin/env python

def count_words(input: str) -> int:
    return len(input.split())

def count_letters(input: str) -> dict[str, int]:
    letter_to_count = {}
    lowered_string = input.lower()

    for s in lowered_string:
        if not s.isalpha():
            continue
        if s not in letter_to_count:
            letter_to_count[s] = 0

        letter_to_count[s] += 1
    
    return letter_to_count

def sort_letters(dict):
    return dict["count"]

def main():
    with open('books/frankenstein.txt') as f:
        print(f"--- Begin report of {f.name} ---")

        file_contents = f.read()
        print(f"{count_words(file_contents)} words found in the document\n")

        letters_list = []

        for letter, count in count_letters(file_contents).items():
            letters_list.append({"letter": letter, "count": count})

        letters_list.sort(reverse=True, key=sort_letters)

        for item in letters_list:
            print(f"The '{item["letter"]}' character was found {item["count"]} times")

        print('--- End report ---')


if __name__ == "__main__":
    main()
