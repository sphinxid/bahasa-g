def encrypt_g(text):
    result = ""
    vowels = "aiueoAIUEO"
    words = text.split()
    
    for i, word in enumerate(words):
        if i > 0:
            result += " "
            
        for char in word:
            result += char
            if char in vowels:
                result += "g" + char.lower()
    
    return result

# Test cases
test_cases = [
    "lagi ngapain",
    "ini bahasa anak gaul 90-an",
    "aku cinta kamu",
    "gue sebel sama lo"
]

# Run test cases
for test in test_cases:
    encrypted = encrypt_g(test)
    print(f"Input  : {test}")
    print(f"Output : {encrypted}")
    print()
