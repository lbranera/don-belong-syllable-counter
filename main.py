from getter import syllables
from getter import get_doc

def is_vowel(letter):
    if letter.upper() in ["A", "E", "I", "O", "U"]:
        return True

    return False

def ilokano_syllable_count(string):
    count = 0
    for character in string:
        if is_vowel(character):
            count += 1
    
    return count

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

filename = "biag"
doc = get_doc(f"{filename}.txt")

file = open(f"./results/{filename}_results.csv", "w")

headers = [
    "line",
    "line_syllable_count",
    "word_count",
    "average_syllable",
    "max_syllable_count",
    "min_syllable_count\n",
]

file.write(",".join(headers))

for index, line in enumerate(doc):
    line_string = " ".join(line)
    total_syb_count = ilokano_syllable_count(line_string)

    word_count = len(line)

    count_list = []
    for token in line:
        count_list.append(ilokano_syllable_count(token))

    average_syb = sum(count_list) / len(count_list)

    max_syb_count = max(count_list)
    min_syb_count = min(count_list)

    file.write(f"{index+1},{total_syb_count},{word_count},{average_syb},{max_syb_count},{min_syb_count}\n")

file.close()