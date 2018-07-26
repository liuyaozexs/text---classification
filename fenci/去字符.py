import string


s = 'abcxyz123'
trans = str.maketrans('abc', 'ABC', '123456')
print(s.translate(trans))
