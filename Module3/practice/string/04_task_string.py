# Дана строка текста, слова разделены пробелами, знаки препинания отсутствуют.
# Определить в предоставленном сообщении количество слов длиной больше, чем 5.

text = "Lorem ipsum dolor sit amet consectetur adipiscing elit Integer porttitor bibendum nisi ut convallis ante"
# Примечание: для генериации текста можете воспользоваться сайтом: https://ru.lipsum.com/

# TODO: your code here

text = "Lorem ipsum dolor sit amet consectetur adipiscing elit Integer porttitor bibendum nisi ut convallis ante"

new_text = text.split(" ")

words_per_line = len(new_text)
#print(words_per_line)
i = 0
summ_word = 0
while i < words_per_line:
    word_count = len(new_text[i])
    #print(word_count)
    if word_count > 5:
        summ_word = summ_word + 1
        #print(word_count)
    i += 1
print(summ_word)
