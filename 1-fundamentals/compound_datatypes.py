fruits = ['apple', 'banana', 'cherry', 'date']

fruits.append('eldercurry')

print(fruits)

fruits.remove('banana')

print(fruits)

fruits.sort()

print(fruits)


student = {
  'name': 'John Doe',
  'age': 25,
  'major': 'Computer Science'
}


student['major'] = 'Electrical Engineering'
student['year'] = 'Senior'

print(student)
print(student.keys())
print(student.values())


books = [
  {
    'title':'title1',
    'author': 'author1',
    'year': 2001
  },
  {
    'title':'title2',
    'author': 'author2',
    'year': 2002
  },
  {
    'title':'title3',
    'author': 'author3',
    'year': 2003
  }
]

print(books[1]['title'])
print(books[2]['year'])

for book in books:
  print(f"title: {book['title']}, author: {book['author']}")


course = {
  'math': ['std1'],
  'history': ['std2', 'hstd2', 'hstd3'],
  'chemistry': ['std3']
}

course['math'].extend(['mstd1', 'mstd2', 'mstd3'])
del course['history'][2]
print(course['chemistry'])
course['physics'] = ['pstd1', 'pstd2', 'pstd3', 'pstd4',]

print(course)



