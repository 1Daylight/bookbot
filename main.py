def main(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        print(f"--- Begin report of {file_path} ---")
        print(f"{word_count} words found in the document")
        print("")
        letter_count = count_letters(file_contents)
        letter_sort = []
        for letter in letter_count:
            if letter.isalpha():
                count = letter_count[letter]
                letter_sort.append({"letter": letter, "count": count})
        letter_sort.sort(reverse=True, key=sort_on)
        for letter_count in letter_sort:
            letter = letter_count["letter"]
            count = letter_count["count"]
            print(f"The {letter} character was found {count} times")
        print("--- End report ---")

def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    letters = {}
    for letter in text.lower():
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1
    return letters

def sort_on(dict):
    return dict["count"]

main("books/frankenstein.txt")
