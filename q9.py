# Get the list of words from the user
user_list = input("Enter a list of words separated by spaces: ").split()

# Initialize an empty dictionary to store the word counts
word_counts = {}

# Iterate through the list of words
for word in user_list:
    # If the word is already in the dictionary, increment the count
    if word in word_counts:
        word_counts[word] += 1
    # If the word is not in the dictionary, add it with a count of 1
    else:
        word_counts[word] = 1

# Print the word counts
for word, count in word_counts.items():
    print(f"{word}: {count}")
