number_word_dict = {0: 'zero', 1: 'one', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten'}

a = int(input("Enter a number : "))
number_in_words = ' '
original=a
if a<10:
    a in number_word_dict.keys()
    number_in_words = number_word_dict[a]
    print(f'{a} = {number_in_words}')

elif a > 10:
    first = a//10
    remainder = a % 10
    if first in number_word_dict.keys():
        number_in_words = number_word_dict[first] + ' ' + 'Ten' + ' ' + number_word_dict[remainder]
    print(f'{a} = {number_in_words}')




