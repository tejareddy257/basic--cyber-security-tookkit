import hashlib

text = input("Enter Text: ")

hash_value = hashlib.sha256(text.encode()).hexdigest()

print("SHA256 Hash:", hash_value)
