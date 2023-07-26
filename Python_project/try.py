import sys
from PIL import Image
import stagger
import io
mp3 = stagger.read_tag('Taur.mp3')
by_data = mp3[stagger.id3.APIC][0].data
im = io.BytesIO(by_data)
imageFile = Image.open(im)