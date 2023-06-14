def clean_word(word):
    punctuation = [',', '.', ';', ':', '?']
    cleaned_word = word.lower()
    for char in punctuation:
        cleaned_word = cleaned_word.replace(char, '')
    return cleaned_word

def count_words(lines):
    word_count = {}
    for line in lines:
        words = line.split()
        unique_words = set()  # Track unique words in each line
        for word in words:
            cleaned_word = clean_word(word)
            if len(cleaned_word) > 4:
                unique_words.add(cleaned_word)
        for word in unique_words:
            word_count[word] = word_count.get(word, 0) + 1
    return word_count


with open('discurso.txt', 'r') as file:
    speech_lines = file.readlines()

word_count = count_words(speech_lines)

sorted_words = sorted(word_count.items())

for word, count in sorted_words:
    print(f'{word} {count}')