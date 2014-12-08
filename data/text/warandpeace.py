import requests as re
import piglatin as pl

bookgot = re.get("http://www.gutenberg.org/files/2600/2600.txt")
thebook = bookgot.text
pigbook = pl.translate(thebook)


with open("warandpeace.txt", "w") as f:
    f.write(thebook)

with open("pig_warandpeace.txt", "w") as f:
    f.write(pigbook)
