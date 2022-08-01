import hashlib

text = 'Python Bootcamp'

hash_object = hashlib.md5(text.encode())
hash_md5 = hash_object.hexdigest()

print(hash_md5)
