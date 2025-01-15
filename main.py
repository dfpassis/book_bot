def count_characters(text):
    char_counts = {}
    for char in text:
        if char.isalpha():
            if char.lower() not in char_counts:
                char_counts[char.lower()] = 1
            else:
                char_counts[char.lower()] += 1
    return char_counts   

def main():
    book_path = "books/frankenstein.txt"
    with open(book_path) as f:
        text = f.read()
    my_dict = count_characters(text)
    sorted_dict = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)
    
    print("--- Character Counts ---")
    for char, count in sorted_dict:
        print(f"The '{char}' character appears {count} times.")

main()

