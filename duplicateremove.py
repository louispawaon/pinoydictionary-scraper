def remove_duplicate_words(filename):
    # Open the file
    with open(filename, 'r') as f:
        # Read all the text from the file
        text = f.read()

    # Split the text into words
    words = text.split()

    # Create a list to hold the unique words
    unique_words = []

    # Iterate over the words and add each one to the list if it is not already present
    for word in words:
        if word not in unique_words:
            unique_words.append(word)

    # Open the file for writing
    with open(filename, 'w') as f:
        # Write all the unique words to the file
        for word in unique_words:
            f.write('"'+word+'",'+ '\n')

# Test the function
remove_duplicate_words('tagalog_wordlist.txt')
