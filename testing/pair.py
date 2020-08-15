from PIL import Image
import imagehash
basehash = imagehash.phash(Image.open('/Users/rishabtandon3/Desktop/testing/swasika meme.jpg'))
otherhash = imagehash.phash(Image.open('/Users/rishabtandon3/Desktop/testing/swatistaka.jpg'))
print(otherhash)
print(basehash == otherhash)
print(basehash - otherhash)
