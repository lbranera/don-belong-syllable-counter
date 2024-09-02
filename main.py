from getter import syllables
from getter import get_sample

def is_vowel(letter):
    if letter.upper() in ["A", "E", "I", "O", "U"]:
        return True

    return False

def ilokano_syllabifier(token):
    token_size = len(token)

    if token_size <= 2:
        return [token]
    elif token_size == 3:
        if is_vowel(token[0]) and (not is_vowel(token[1])) and is_vowel(token[2]):
            return [ token[0], token[1]+token[2]]
        elif (not is_vowel(token[0])) and is_vowel(token[1]) and (not is_vowel(token[2])):
            return [token]
        elif (not is_vowel(token[0])) and is_vowel(token[1]) and is_vowel(token[2]):
            return [token[0]+token[1], token[2]]
    else:
        target_token = token
        result = []
        while target_token != "":
            #print(target_token)
            for syb in syllables:
                if (len(syb) <= len(target_token)):
                    sub_token = target_token[: len(syb)]
                    if (syb.upper() == sub_token.upper()):
                        target_token = target_token[len(syb): ]
                        result.append(sub_token)
                        break

        return result

test_dataset = get_sample(n = 20)
print(test_dataset)

print("")

for token in test_dataset:
    print(token, ilokano_syllabifier(token))