# Compare two files character by character and prints the differences
def compare_files(file1, file2):

    differences = 0
    line_number = 1

    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        # Read both files line by line
        for line1, line2 in zip(f1, f2):
            # Compare each character in the lines
            for i, (char1, char2) in enumerate(zip(line1, line2)):
                if char1 != char2:
                    #print(f'Difference found at line {line_number}, position {i}: {char1} (file1) vs {char2} (file2)')
                    differences += 1
            line_number += 1
            nchar = i
    print(f'Total differences found: {differences}')
    print(f'The error percentage is: {differences/nchar*100}%')
    print(f'compare: total number of ACGT, {nchar}')
