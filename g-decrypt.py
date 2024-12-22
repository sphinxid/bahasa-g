def decrypt_g(text):
    result = ""
    vowels = "aiueoAIUEO"
    words = text.split()
    
    for i, word in enumerate(words):
        if i > 0:
            result += " "
            
        i = 0
        while i < len(word):
            result += word[i]
            if i + 2 < len(word) and word[i] in vowels and word[i+1] == 'g' and word[i+2] == word[i].lower():
                i += 3
            else:
                i += 1
    
    return result

# Test cases with both encrypted and decrypted versions
test_cases = [
    "lagagigi ngagapagaigin",
    "iginigi bagahagasaga aganagak gagaugul 90-agan",
    "agakugu cigintagaga kagamugu",
    "guguege segebegel sagamaga logo"
]

# Run test cases
for test in test_cases:
    decrypted = decrypt_g(test)
    print(f"Input  : {test}")
    print(f"Output : {decrypted}")
    print()
