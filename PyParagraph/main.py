import os
import re



text_file_1 = os.path.join("raw_data","paragraph_1.txt")
text_file_2 = os.path.join("raw_data","paragraph_2.txt")
text_file_3 = os.path.join("raw_data","paragraph_3.txt")


paragraph = open(text_file_2,"r")
#print(paragraph.readline())
#paragraph = "Adam Wayne, the conqueror, with his face flung back and his mane like a lion's, stood with his great sword point upwards, the red raiment of his office flapping around him like the red wings of an archangel. And the King saw, he knew not how, something new and overwhelming. The great green trees and the great red robes swung together in the wind. The preposterous masquerade, born of his own mockery, towered over him and embraced the world. This was the normal, this was sanity, this was nature, and he himself, with his rationality, and his detachment and his black frock-coat, he was the exception and the accident a blot of black upon a world of crimson and gold."


re.split("(?<=[.!?]) +", paragraph)

print(paragraph)