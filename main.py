from res.Picture import Picture
from res.Slide import Slide

# FILENAME = "a_example"
FILENAME = "b_lovely_landscapes"
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

print('EXTRACT VERTICALS')
# Extract verticals
slides = []
verticals = []
for pic in pictures:
    if pic.isVertical():
        verticals.append(pic)
    else:
        slides.append(Slide(pic))


# Sort verticals
print('SORT VERTICALS')
if len(verticals) > 0:
    while len(verticals) > 2:
        found = False
        unique = verticals[0].uniqueTags(verticals[1])
        for y in range(2, len(verticals) - 1):
            if verticals[0].uniqueTags(verticals[y]) > unique:
                slides.append(Slide(verticals[0], verticals[y]))
                verticals.pop(0)
                verticals.pop(y - 1)
                found = True
                break
        if not found:
            slides.append(Slide(verticals[0], verticals[1]))
            verticals.pop(0)
            verticals.pop(0)

    slides.append(Slide(verticals[0], verticals[1]))

# Sort slides
print('SORT SLIDES')
sortedSlides = [slides[0]]
slides.pop(0)
while len(slides) > 0:
    print(len(slides))
    found = False
    score = sortedSlides[-1].calculateScore(slides[0])
    for y in range(1, len(slides) - 1):
        if sortedSlides[-1].calculateScore(slides[y]) > score:
            sortedSlides.append(slides[y])
            slides.pop(y)
            found = True
            break
    if not found:
        sortedSlides.append(slides[0])
        slides.pop(0)


# Output results
print('OUTPUT RESULTS')
resultFile = open("output/" + FILENAME + "-RESULT.txt", "w")
resultFile.write(str(len(sortedSlides)) + "\n")
for slide in sortedSlides:
    resultFile.write(slide.getPictures() + "\n")
resultFile.close()

print('FINISHED RUNNING HASH CODE 2019')
