import numpy as np

def main():
    sentence = input("Enter the desired sentence: ")

    if sentence[-1] == ' ':
        print("Sentence should not end with a space.")
        return

    sentence = sentence.strip()

    words = np.char.count(sentence, ' ') + 1

    print(f"Words: {words}")

if __name__ == "__main__":
    main()
