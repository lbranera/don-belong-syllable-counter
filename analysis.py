file = open("sample.txt")
text = [line.strip().split(" ") for line in file.readlines()]
file.close()

tokens = [token for line in text for token in line]
tokens = list(set(tokens))
sorted_tokens = sorted(tokens, key=lambda x: (len(x), x))

file = open("vocabulary.txt", "w")
for token in sorted_tokens:
    file.write(f"{token}\n")
file.close()