# Function to count total words
def count_words(text):
    # .split() breaks the text into a list of words
    return len(text.split())

# Function to count vowels (a, e, i, o, u)
def count_vowels(text):
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)

# Function to count consonants (letters that are not vowels)
def count_consonants(text):
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char.isalpha() and char not in vowels)

# Function to flip the text backward
def reverse_text(text):
    return text[::-1]

# Function to check if it reads the same forward and backward
def is_palindrome(text):
    # Remove spaces and make lowercase to check correctly
    clean_text = text.replace(" ", "").lower()
    return clean_text == clean_text[::-1]

# Function to remove all vowels from the text
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return "".join(char for char in text if char not in vowels)

# Function to count how many times each word appears
def word_frequency(text):
    words = text.lower().split()
    freq = {}
    for word in words:
        # If word is in dictionary, add 1. If not, start at 1.
        freq[word] = freq.get(word, 0) + 1
    return freq

# Function to find the word with the most letters
def longest_word(text):
    words = text.split()
    if not words:
        return ""
    # max() finds the biggest word using len (length)
    return max(words, key=len)

# Main function to run the whole analysis
def analyze_text():
    user_input = input("Enter text: ")
    
    if not user_input.strip():
        print("Please enter some text!")
        return

    print("\n=== TEXT ANALYSIS ===")
    print(f"Words:          {count_words(user_input)}")
    print(f"Vowels:         {count_vowels(user_input)}")
    print(f"Consonants:     {count_consonants(user_input)}")
    print(f"Reversed:       {reverse_text(user_input)}")
    print(f"Palindrome:     {'Yes' if is_palindrome(user_input) else 'No'}")
    print(f"Without vowels: {remove_vowels(user_input)}")
    
    # Show longest word and its size
    big_word = longest_word(user_input)
    print(f"Longest word:   {big_word} ({len(big_word)} letters)")
    
    # Show how often words repeat
    freq_dict = word_frequency(user_input)
    freq_str = ", ".join([f"{k}: {v}" for k, v in freq_dict.items()])
    print(f"Word Frequency: {freq_str}")

if __name__ == "__main__":
    analyze_text()