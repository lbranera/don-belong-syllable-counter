import os
import pandas as pd
import matplotlib.pyplot as plt

from getter import get_doc
from preprocessor import preprocess

def is_vowel(letter):
    if letter.upper() in ["A", "E", "I", "O", "U"]:
        return True

    return False

def ilokano_syllable_count(token, old_ortho=False):
    if (not old_ortho):
        count = 0
        for character in token:
            if is_vowel(character):
                count += 1
        
        return count
    else:
        preprocessed_token = preprocess(token)
        count = 0
        for character in preprocessed_token:
            if is_vowel(character) or (character == "1"):
                count += 1
            elif character == "2":
                count += 2

        return count

def execute(filename):
    doc = get_doc(filename)

    headers = [
        "line_index",
        "line_syllable_count",
        "word_count",
        "average_syllable",
        "max_syllable_count",
        "min_syllable_count",
    ]

    df = pd.DataFrame(columns=headers)

    for line_index, line in enumerate(doc):
        word_count = len(line)

        count_list = []
        for token in line:
            if filename == "leona.txt":
                count = ilokano_syllable_count(token, old_ortho=True)
            else:
                count = ilokano_syllable_count(token)
            
            count_list.append(count)

        line_syllable_count = sum(count_list)
        average_syllable = line_syllable_count / len(count_list)

        max_syllable_count = max(count_list)
        min_syllable_count = min(count_list)

        new_data = pd.DataFrame({
            "line_index": [ line_index + 1 ],
            "line_syllable_count": [ line_syllable_count ],
            "word_count": [ word_count ],
            "average_syllable": [ average_syllable ],
            "max_syllable_count": [ max_syllable_count ],
            "min_syllable_count": [ min_syllable_count ],
        })

        df = pd.concat([df, new_data], ignore_index=True)
    
    df.to_csv(f"./results/{filename}.csv", index=False)

    value_counts = df['line_syllable_count'].value_counts()
    value_counts_sorted = value_counts.sort_index()

    bars = plt.bar(value_counts_sorted.index, value_counts_sorted.values)

    plt.xlabel('Line Syllable Count Values')
    plt.ylabel('Number of Lines')
    plt.title('Histogram of Line Syllable Count')

    plt.xticks(range(min(value_counts_sorted.index), max(value_counts_sorted.index) + 1))

    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, height, f'{int(height)}', 
                ha='center', va='bottom', fontsize=10, color='black')

    plt.tight_layout()
    plt.savefig(f"./results/{filename}.png")
    plt.close()
    #plt.show()

folder_path = './input'
filenames = os.listdir(folder_path)

for filename in filenames:
    print("Processing", filename)
    execute(filename)
