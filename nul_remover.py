#removes NUL characters for a decoded DNA string
def nul_remover(file_in,file_out):
    with open(file_in, 'r') as f:
        contents = f.read()

    # Replace NUL characters with an empty string
        contents = contents.replace('\0' * 15, '')

    with open(file_out, 'w') as f:
        f.write(contents)