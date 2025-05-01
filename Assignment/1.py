def calculate_word_energy(word):
    vowels = "aeiouAEIOU"
    vc = 0
    cc = 0
    
    for char in word:
        if char in vowels:
            vc += 1
        else:
            cc += 1
    word_length = len(word)

    if vc > cc:
        print("Your word is full of energy!")
    elif cc > vc:
        if word_length % 3 == 0:
            print("Your word has a strong and balanced form.")
        else:
            print("Your word is strong but not perfectly balanced.")
    else:
        print("Your word has equal energy and strength.")


calculate_word_energy("Ama")
calculate_word_energy("strength")
