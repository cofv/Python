word = input("Lägg ord i låda ") 

length_word = len(word)

mellanrum = 2

box = ""
box += "#" * (length_word + (mellanrum*2) + (1*2)) + "\n"
box += "#" + " " * (length_word + (mellanrum*2)) + "#" + "\n"
box += "#" + " " * mellanrum + word + " " * mellanrum + "#" + "\n"
box += "#" + " " * (length_word + (mellanrum*2)) + "#" + "\n"
box += "#" * (length_word + (mellanrum*2) + (1*2)) + "\n"

"""
##########
#        #
#  test  #
#        #
##########

length:word + (mellanrum*2) + (1*2)
"""
print(box)