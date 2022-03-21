import random

plain = [chr(i) for i in range(ord("a"), ord("z") + 1)]
cipher = [chr(i) for i in range(ord("a"), ord("z") + 1)]

random.shuffle(cipher)

print(f"Plain {plain}")
print(f"Cipher {cipher}")

msg = input("Enter Message: ")

encoded = ""
for i in msg:
    encoded += cipher[plain.index(i)]

print(f"Encoded Message: {encoded}")

decoded = ""
for i in encoded:
    decoded += plain[cipher.index(i)]

print(f"Decoded Message: {decoded}")
