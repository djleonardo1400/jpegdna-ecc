#converts binary data to a dna string in a new file
def bin_to_dna(in_file, out_file):

    with open(in_file, "rb") as input_file:
        l = int.from_bytes(input_file.read(), byteorder='big')

    # Remove the '0b' prefix from the binary string
    binary_string = bin(l)[4:]
    out = []

    for i in range(0, len(binary_string), 2):
        # extract the two bits at the current index
        bits = binary_string[i:i+2]
        if bits == "00":
            out.append("A")
        elif bits == "01":
            out.append("C")
        elif bits == "10":
            out.append("G")
        elif bits == "11":
            out.append("T")

    final = "".join(out)
    with open(out_file, "w") as output_file:
        output_file.write(final)

#converts a dna string into a binary file
def dna_to_bin(in_file, out_file):

    with open(in_file, "r") as input_file:
        input_string = input_file.read()

    # initalise the binary sequence with "11" (3). this is useful to keep all characters with two bits
    # it is going to be removed after
    output_values = 3

    for ch in input_string:
        # map the character to a binary value and add it to the list
        if ch == "A":
            output_values = output_values<<2 | (0b00)
        elif ch == "C":
            output_values  = output_values<<2 | (0b01)
        elif ch == "G":
            output_values = output_values<<2 | (0b10)
            
        elif ch == "T":
            output_values  = output_values<<2 | (0b11)

    #calculates how many bytes are required to write the generated binary number
    byte_length = (output_values.bit_length() + 7) // 8

    with open(out_file, "wb") as output_file:
        output_file.write(output_values.to_bytes(byte_length, byteorder="big",signed=False))
