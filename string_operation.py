course = "Python's course"
print(course)

course_begin = 'Python for "Beginners"'
print(course_begin)

course_learning = '''
Hi Naveen,

You are learning a python! 

Thanks,
:)
'''
print(course_learning)

course_index = "This_is_a_string"
print("first", course_index[0])
print("last", course_index[-1])
print(course_index[0:4])
print(course_index[:4])
print(course_index[4:])
print(course_index[:])  # clone a string

print(course_index[1:-1])

first = "Naveen Kumar"
second = "Lokesh"
print(first + ' [' + second + ']')
print(f'{first} [{second}]')  # formatted string

p_code = "Python CodE"
print("p_code length : ", len(p_code))
print(p_code, p_code.upper())
print(p_code, p_code.lower())
print("P @", p_code.find('P'))
print(p_code.replace('CodE', 'Dynamic Code'))
print("'Code' in p_code", 'Code' in p_code)
print(p_code.title())
