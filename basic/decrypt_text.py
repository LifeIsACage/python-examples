from hashlib import sha1, sha224, sha256, sha384, sha512, md5

print("Select you decrypt method (1.SHA1, 2.SHA224, 3.SHA256, 4.SHA384, 5.SHA512, 6.MD5)")

selected = int(input())

decrypt_text = input("Insert text you want to decrypt: ")

if selected == 1:
    print(sha1(decrypt_text.encode()).hexdigest())
elif selected == 2:
    print(sha224(decrypt_text.encode()).hexdigest())
elif selected == 3:
    print(sha256(decrypt_text.encode()).hexdigest())
elif selected == 4:
    print(sha384(decrypt_text.encode()).hexdigest())
elif selected == 5:
    print(sha512(decrypt_text.encode()).hexdigest())
elif selected == 6:
    print(md5(decrypt_text.encode()).hexdigest())
else:
    print(sha1(decrypt_text.encode()).hexdigest())