from text import samples




# handle a massive file using generator
def __filereader_gen(file):
    with open(file) as f:
        for line in f:
            yield line


def fileprocessor(file, function):
    filegen = __filereader_gen()
    filegen2 = (process(x) for x in g)



