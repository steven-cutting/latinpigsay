
# handle a massive file using generator
def filereader_gen(file):
    with open(file) as f:
        for line in f:
            yield line
