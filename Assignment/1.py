def calculate_word_energy(word):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0
    
    for char in word:
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1
    word_length = len(word)

    if vowel_count > consonant_count:
        print("Your word is full of energy!")
    elif consonant_count > vowel_count:
        if word_length % 3 == 0:
            print("Your word has a strong and balanced form.")
        else:
            print("Your word is strong but not perfectly balanced.")
    else:
        print("Your word has equal energy and strength.")


calculate_word_energy("Ama")
calculate_word_energy("strength")
