import re

def has_three_consecutive_vowels(text):
    pattern = r'[aeiou]{3}'
    if re.search(pattern, text, re.IGNORECASE):
        return True
    return False

def replace_first_three_consecutive_vowels(text):
    pattern = r'[aeiou]{3}'
    replaced_text = re.sub(pattern, '2', text, count=1, flags=re.IGNORECASE)
    return replaced_text

def has_diphthongs(token):
    diphthongs = ["ao", "au", "eo", "eu", "io", "iu", "ou", "uo"]

    for diphthong in diphthongs:
        if diphthong in token:
            return True
    
    return False

def replace_diphthongs(token):
    diphthongs = ["ao", "au", "eo", "eu", "io", "iu", "ou", "uo"]

    for diphthong in diphthongs:
        if diphthong in token:
            return token.replace(diphthong, "1")

def preprocess1(token):
    if has_three_consecutive_vowels(token):
        formatted_token = replace_first_three_consecutive_vowels(token)
        return preprocess1(formatted_token)
    else:
        return token

def preprocess2(token):
    if has_diphthongs(token):
        formatted_token = replace_diphthongs(token)
        return preprocess2(formatted_token)
    else:
        return token

def preprocess(token):
    result = preprocess1(token)
    final_result = preprocess2(result)
    return final_result
