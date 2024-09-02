
def main():
    frankenstein = read_book("books/frankenstein.txt")
    print(frankenstein)
    print(f"{count_words(frankenstein)} words found in the document")
    count_letters = count_chars(frankenstein)
    print(count_letters)

    print_report(count_letters)

def read_book(book_path):
    with open(book_path) as f:
        file_contents = f.read()
        return file_contents
    
def count_words(text):
    return len(text.split())

def count_chars(text):
    lowered_text = text.lower()
    letters = 'abcdefghijklmnopqrstuvwxyz'

    dict={}

    for letter in lowered_text:
        if letter in letters:
            if letter not in dict:
                dict[letter] = 0
            dict[letter] += 1
    return dict

def print_report(d):
    report = sorted(d.items(),reverse=True, key=lambda x:x[1])
    for tup in report:
        letter,val = tup
        print(f"The '{letter}' character was found {val} times")

main()


