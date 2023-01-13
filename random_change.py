import random
import textwrap

#performs "percent_changes" nucleotides alterations at random positions, writes on a new file
def random_change(input_filename,output_filename,percent_changes):

    with open(input_filename, "r") as f:
        text = f.readlines()

    #remove all \n from the list
    text_clean = [i.strip() for i in text]

    cont = text_clean[1]
    char_per_line = len(cont)

    all_lines = "".join(text_clean)

    # Count the number of A, C, G, and T characters in the file
    num_valid_chars = sum(char in ['A', 'C', 'G', 'T'] for char in all_lines)

    # Calculate the number of character replacements to perform
    num_changes = int(num_valid_chars * percent_changes / 100)

    # Choose a list of random indices to modify
    indices = random.sample(range(len(all_lines)), num_changes)

    # Convert the string to a list of characters
    chars = list(all_lines)

    # Perform the character replacements
    for i in indices:
        char = chars[i]
        if char == 'A':
            replacements = ['C', 'G', 'T']
        elif char == 'C':
            replacements = ['A', 'G', 'T']
        elif char == 'G':
            replacements = ['A', 'C', 'T']
        elif char == 'T':
            replacements = ['A', 'C', 'G']
        else:
            print("invalid character")

        new_char = random.choice(replacements)
        chars[i] = new_char
        #print(f"Modified character at position {i}: {char} -> {new_char}")

    # Join the modified characters into a single string
    modified_text = "".join(chars)
    new_list = textwrap.wrap(modified_text,char_per_line)

    #add \n to all lines exept last one
    for i in range(len(new_list)-1):
        new_list[i] = new_list[i] + "\n"

    #write on output file
    with open(output_filename, "w") as f:
        for line in new_list:
            f.write(f"{line}")

    print(f"{num_changes} changes were made")
    print(f'random_change: total number of ACGT, {num_valid_chars}')
