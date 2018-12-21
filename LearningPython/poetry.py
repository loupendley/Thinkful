def reformat_poem(poem):
    return ".\n".join(poem.split(". "))
    # What  I did in my study here was to not use
    #       the actual poem from the Codewars details, mistake #1.
    #       If you don't have that correct, noting else will work,
    #       Lou.
    #
    #
    # poem = poem[:-1]
    # poem_new = ''
    # for poemline in poem.split('.'):
    #     if len(poemline) > 1:
    #         poemline = str(poemline.strip())
    #         poem_new = poem_new + poemline + '.\n'
    # return poem_new


poem = "Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex. Complex is better than complicated."
# print('poem={}, and\nnew poem={}'.format(poem, reformat_poem(poem)))
print("poem_new = {}".format(reformat_poem(poem)))
