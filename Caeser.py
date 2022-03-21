text = "abcdz"  # input("Enter text: ")
text = text.lower()
shift = 1  # int(input("Enter shift value: "))

encoded = ""
for i in text:
    if ord("a") <= ord(i) <= ord("z"):
        normalize = ord(i) - ord("a")
        encrypted = (normalize + shift) % 26
        encoded += chr(encrypted + ord("a"))

print(f"Encoded text: {encoded}")

decoded = ""
for i in encoded:
    if ord("a") <= ord(i) <= ord("z"):
        normalize = ord(i) - ord("a")
        decrypted = (normalize - shift) % 26
        decoded += chr(decrypted + ord("a"))

print(f"Decoded text: {decoded}")
