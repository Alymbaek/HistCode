# q1 = ['alma','almurut','ananas','banan','klubnika']
#
# for q3 in q1:
#     print(q3)
#     print(f'indexsi: {q1.index(q3)}')


# ПРАКТИКА 13-ИЮЛЬ САМ ПРИДУМАЛ

# q1 = ['alma','almurut','ananas','banan','klubnika']
# q2 = ['alma','almuwrut','ananaqs','banan','klubnika']
# q1 = set(q1)
# q2 = set(q2)
# q3 = q1.union(q2)
#
# for q1 in q3:
#     print(q1)



# q1 = ['alma','almurut','ananas','banan','klubnika']
# q2 = input('jaz: ')
# if q2 in q1:
#     print(q1.index(q2))
#     print(q1)
# else:
#     print('Error')








#3
# pet = {
#      'w1': {'emne': 'echteke','aytchy':'aitbaim kozu','atyn kim':'jashoo kooz'},
#
#      'w2': {'ou': 'echteke', 'aytsan': 'aitbaim kozu', 'kanday': 'jashoo kooz'}
# }
# pet['w1']['emne'] = 'atandyn chokusu'
# print(pet['w1']['emne'])
# print(len(pet['w1']['emne']))





numbers1 = [0, 5,5,6,7,2,2,2,5,5,5,0,0,0, 2]
while True:
  nem = int(input('san jaz: '))
  if nem in numbers1:
    print(f'aga bolgon okshosh sandar: {numbers1.count(nem)}')
    print(f'indexsi: {numbers1.index(nem)}')
    numbers1.remove(nem)
    print(numbers1)
  n = int(input('jaz: '))
  if n in numbers1:


    print(f'aga bolgon okshosh sandar: {numbers1.count(n)}')
    print(f'indexsi: {numbers1.index(n)}')
    numbers1.remove(n)
    print(numbers1)
  else:
      print('Error')












































