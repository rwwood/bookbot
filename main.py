def main():
    book_path = "books/frankenstein.txt"
    generate_report(book_path)
    

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    return len(text.split())

def count_letters(text):
    letter_dict = {}
    for s in text:
        letter = s.lower()
        if letter.isalpha():
            if letter in letter_dict:
                letter_dict[letter] += 1
            else:
                letter_dict[letter] = 1
    
    return letter_dict

def generate_report(path):
    print(f"--- Begin report of {path} ---")
    try:
        text = get_book_text(path)
        num_words = count_words(text)
        print(f"{num_words} words found in the document\n")

        letter_list = count_letters(text)
        sorted_letter_list = sorted(letter_list.items(), reverse=True, key=lambda x:x[1])
        converted_dict = dict(sorted_letter_list)

        for letter_total in converted_dict:
            print(f"The {letter_total} character was found {converted_dict[letter_total]} times")
    except Exception as e:
        print(e)

    print("\n--- End Report ---")


main()