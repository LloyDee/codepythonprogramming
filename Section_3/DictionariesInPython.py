my_dict = {'key1': 'value1', 'key2': 'value2'}
print(my_dict)
print(my_dict['key2'])

prices = {"Apple": 3.00, "Orange": 2.50, "Banana": 2.756232}
print("{0:2.2f}".format(prices["Orange"]))
print('{0:1.2f}'.format(prices['Banana']))

dictionary_of_list = {'Group 1': ['Lloyd', 'Blonde', 'Tiger'], 'Group 2': ['Edith', 'Ginger', 'Panther']}

dictionary_of_list['Group 1'].append('Jayson')
print(dictionary_of_list['Group 1'])
print(dictionary_of_list['Group 2'])

dictionary_in_dictionary = {'Lloyd': {'Age': 29, 'Gender': 'Male'}, 'Edith': {'Age': 30, 'Gender': 'Female'}}
dictionary_in_dictionary['Lloyd']['Age'] = 100
print(dictionary_in_dictionary['Lloyd']['Gender'])
print(dictionary_in_dictionary['Edith']['Age'])
print(dictionary_in_dictionary.values())
print(dictionary_in_dictionary.items())
print(dictionary_in_dictionary['Lloyd'])

d = {'key1': "My Name is Lloyd"}
print(d['key1'].split())
print(d['key1'][::-1])
x = d['key1'].split()[3].upper()
print('Printing just {0}'.format(x))
print(d['key1'][11:])
