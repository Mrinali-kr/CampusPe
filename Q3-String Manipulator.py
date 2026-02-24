# Analyzes a sentence and prints various string properties

def main():
    sentence = input("Enter a sentence: ")

    words = sentence.split()

    print("Original:", sentence)
    print("Characters (with spaces):", len(sentence))
    print("Characters (without spaces):", len(sentence.replace(" ", "")))
    print("Words:", len(words))
    print("UPPERCASE:", sentence.upper())
    print("lowercase:", sentence.lower())
    print("Title Case:", sentence.title())

    if words:
        print("First word:", words[0])
        print("Last word:", words[-1])

    print("Reversed:", sentence[::-1])

if __name__ == "__main__":
    main()