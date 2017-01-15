phones = {
    'Max': ['0501116454', '076876235612'],
    'Oleg': ['0676553465'],
    'Igor': ['0996654444', '0872386576', '076988877665544'],
    'Ira': ['0997674545'],
}

search_name = input('Enter name that you are finding: ')
if search_name in phones.keys():
    print('There are phones of user',
          search_name, ':', ', '.join(phones[search_name]))
else:
    print('Name not found')


search_number = input('Enter number that you are finding: ')
for person in phones:
    for tel in phones[person]:
        if search_number in tel:
            print(person, tel)




#Task with products
product_1 = {
    'title': 'Car',
    'price': 100,
    'photo': '1.jpg',
    'params': {
        'weight': 500,
        'color': 'red',
    },
}

product_2 = {
    'title': 'Bike',
    'price': 50,
    'photo': '2.jpg',
    'params': {
        'weight': 40,
        'color': 'black',
    },
}

products = [product_1, product_2]

for item in products:
    print('%s \n Price: %s USD \n Color: %s'
          % (item['title'], item['price'], item['params']['color']))



#Task with unique and non-unique words
text = """for a moment. The face was wind-browned,
cut by lines of weariness and cynical resignation;
the eyes were intelligent. Eddie Willers walked on, wondering
why he always felt it at this time of day, this sense of dread
 without reason. No, he thought, not dread, there's nothing
 to fear: just an immense, diffused apprehension,
 with no source or object. He had become accustomed to the feeling,
  but he could find no explanation for it;
  yet the bum had spoken as if he knew that Eddie felt it, as if
   he thought that one should feel it, and more: as if he knew the reason."""

words = text.lower().split(' ')
words.sort()
print(words)
unique_words = {}
non_unique = {}
for item in words:
    if words.count(item) == 1:
        unique_words[item] = 1
    else:
        non_unique[item] = words.count(item)
print(unique_words)
print(non_unique)
