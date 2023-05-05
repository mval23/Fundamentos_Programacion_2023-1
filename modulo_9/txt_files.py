# file basics
# file1 = open('src/haiku.txt', 'r')
#
# for line in file1:
#     print(line, end='')
#
# file1.close()
#

# file2 = open('src/hello.txt', 'w')
#
# print('Hello, \nworld!', end='', file=file2)
#
# file2.close()

# find amount of lines, words and characters
# file1 = open('src/haiku.txt', 'r')
# file3 = open('src/haiku_specs.txt', 'w')
# lines = 0
# words = 0
# characters = 0
#
# for line in file1:
#     lines += 1
#     words_line = line.split()
#     words += len(words_line)
#     for word in words_line:
#         characters += len(word)
#
# print("lines = {}\nwords = {}\ncharacters = {}".format(lines, words, characters),
#       end='', file=file3)
#
# file1.close()
# file3.close()
#
# find emails and domains
file4 = open('src/news.txt', 'r')
emails = []
domains = []

for line in file4:
    words = line.split()
    for word in words:
        if '@' in word:
            word = word.lower()
            word = word.strip(',')
            word = word.strip('<')
            word = word.strip('>')
            if word not in emails:
                emails.append(word)
                domain = word[word.find('@')+1:]
                if domain not in domains:
                    domains.append(domain)

print('Correos: ', len(emails))
print('Dominios: ', len(domains))
print(emails)
print(domains)
file4.close()
