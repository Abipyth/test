import sys
sys.path.append("C:/users/abinaya/appdata/roaming/python/python311/site-packages")
from spellchecker import SpellChecker
import textdistance

def perform_token_healing(text):
    spell = SpellChecker()
    corrected_tokens = []
    tokens = text.split()
    for token in tokens:
        corrected_token = spell.correction(token)
        if corrected_token != token:
            corrected_tokens.append(corrected_token)
        else:
            suggested_tokens = list(spell.candidates(token)) 
            if suggested_tokens:
                similarity_scores = [textdistance.jaro_winkler.normalized_similarity(token, suggestion) for suggestion in suggested_tokens]
                best_suggestion = suggested_tokens[similarity_scores.index(max(similarity_scores))]
                corrected_tokens.append(best_suggestion)
            else:
                corrected_tokens.append(token)
    corrected_text = ' '.join(corrected_tokens)
    return corrected_text

# Take input from the user
input_text = input("Enter the text for token healing: ")

# Perform token healing
output_text = perform_token_healing(input_text)

print("\nOutput Text:")
print(output_text)


