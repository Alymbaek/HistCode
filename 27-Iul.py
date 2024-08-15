def dico(**kwargs):
    for key,value in kwargs.items():
        print(f'{key}: {value}')

dico(name= 'Alymbek',age= 16,job= 'Proframmist',yu='Kyrgyzstan',gorod= 'Osh',ulissa= 'Abdykadyrova', dom= 204)








# def sum_of_squares(numbers):
#   sum = 0
#   for number in numbers:
#     sum += number ** 2
#   return sum
#
# numbers = [1, 2, 2]
# result = sum_of_squares(numbers)
# print(result)










# def is_pangram(text):
#
#   text = text.lower()
#   text = ''.join(c for c in text if c.isalpha())
#
#   return len(set(text)) == 26
#
# print(is_pangram("The quick brown fox jumps over the lazy dog"))  # True
# print(is_pangram("This is not a pangram."))  # False
# print(is_pangram("The five boxing wizards jump quickly."))  # True
































