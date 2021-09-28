import hashlib
input=input('Enter for Hash: - ')
print('[+]MD5=',hashlib.md5(input.encode()).hexdigest())
print('[+]sha1',hashlib.sha1(input.encode()).hexdigest())
print('[+]sha224=',hashlib.sha224(input.encode()).hexdigest())
print('[+]sha254=',hashlib.sha256(input.encode()).hexdigest())
print('[+]sha384=',hashlib.sha384(input.encode()).hexdigest())
print('[+]sha512=',hashlib.sha512(input.encode()).hexdigest())
print('[+]sha256=',hashlib.sha256(input.encode()).hexdigest())