import re

diphthongs = ["ao", "au", "eo", "eu", "io", "iu"]
hispanic_ortho = ["ue", "ui"]

def has_three_consecutive_vowels(text):
    pattern = r'[aeiou]{3}'
    if re.search(pattern, text, re.IGNORECASE):
        return True
    return False

def replace_first_three_consecutive_vowels(text):
    pattern = r'[aeiou]{3}'
    replaced_text = re.sub(pattern, '2', text, count=1, flags=re.IGNORECASE)
    return replaced_text
      
def preprocess_three_consecutive_vowels(token):
    if has_three_consecutive_vowels(token):
        formatted_token = replace_first_three_consecutive_vowels(token)
        return preprocess_three_consecutive_vowels(formatted_token)
    else:
        return token


def has_diphthongs(token):
    for diphthong in diphthongs:
        if diphthong in token:
            return True
    
    return False

def replace_diphthongs(token):
    for diphthong in diphthongs:
        if diphthong in token:
            return token.replace(diphthong, "1")

def preprocess_diphthongs(token):
    if has_diphthongs(token):
        formatted_token = replace_diphthongs(token)
        return preprocess_diphthongs(formatted_token)
    else:
        return token


def has_hispanic_ortho(token):
    for vowel in hispanic_ortho:
        if vowel in token:
            return True
    
    return False

def replace_hispanic_ortho(token):
    for vowel in hispanic_ortho:
        if vowel in token:
            return token.replace(vowel, "1")

def preprocess_hispanic_ortho(token):
    if has_hispanic_ortho(token):
        formatted_token = replace_hispanic_ortho(token)
        return preprocess_hispanic_ortho(formatted_token)
    else:
        return token

def preprocess_all(token):
    result = preprocess_three_consecutive_vowels(token)
    result = preprocess_diphthongs(result)
    result = preprocess_hispanic_ortho(result)
    return result
