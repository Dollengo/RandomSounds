import random
import string

# Function to generate a random string of a given length
def generate_random_string(length):
    # Define the characters that can be used to generate the string
    characters = string.ascii_letters + string.digits
    # Return a string of the given length with randomly chosen characters
    return ''.join(random.choice(characters) for _ in range(length))

def generate_and_shuffle_strings():
    # Generate a list of 10 random strings, each of length 10
    random_strings = [generate_random_string(2) for _ in range(2)]
    # Concatenate all the strings in the list twice to form a single string
    single_string = ''.join(random_strings + random_strings)
    # Randomly shuffle all the characters in the single string
    shuffled_string = ''.join(random.sample(single_string, len(single_string)))
    return shuffled_string

if __name__ == '__main__':
    # Print the shuffled string
    shuffled_string = generate_and_shuffle_strings()
    print(f"Shuffled string: {shuffled_string}")
