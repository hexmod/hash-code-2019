from res.Picture import Picture
from res.Slide import Slide

FILENAME = "a_example"
# FILENAME = "b_lovely_landscapes"
# FILENAME = "c_memorable_moments"
# FILENAME = "d_pet_pictures"
# FILENAME = "e_shiny_selfies"

print('RUNNING HASH CODE 2019')
pictures = []

# Load the pictures into picture classes
data = open("data/"+FILENAME+".txt", "r")
count = -1
for line in data:
    if count != -1:
        pictures.append(Picture(line, count))
    count += 1
data.close()

# Group the verticals together
slides = []
lastVertical = None
for pic in pictures:
    if pic.isVertical():
        if lastVertical:
            slides.append(Slide(lastVertical, pic))
            lastVertical = None
        else:
            lastVertical = pic
    else:
        slides.append(Slide(pic))


# Sort slides
sortedSlides = slides

# Output results
resultFile = open("output/" + FILENAME + "-RESULT.txt", "w")
resultFile.write(str(len(slides)) + "\n")
for slide in slides:
    resultFile.write(slide.getPictures() + "\n")
resultFile.close()
