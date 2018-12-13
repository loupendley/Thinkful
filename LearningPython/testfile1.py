# def format_poem(poem):
#     # Your code goes here.
#     new_poem = ''
#     counter = 1
#     length = len(poem.split('.'))
#     for poem_lines2 in poem[:-1].split('.'):
#         poem_line_temp = str(poem_lines2.strip())
#         if counter <= length:
#             poem_line_temp = poem_line_temp + '.\n'
#         new_poem = new_poem + poem_line_temp
#         counter += 1
#     return new_poem

def format_poem(poem):
  return ".\n".join(poem.split(". "))

def celsius_to_romer(temp):
    # Your code here.
    # [°Rø] = [°C] × ​21⁄40 + 7.5
    return temp * 21.0 / 40.0 + 7.5

# stuff

# def area_code(text):
#     # Your code goes here
#     for text_piece in text.split(' '):
#         text_piece = text_piece.strip()
#         print('text_piece={} and 1 = {}, and 2 = {}'.format(text_piece, text_piece[:1], text_piece[:1]))
#         if text_piece[:1] == '(' and text_piece[-1:] == ')':
#             print('text_piece = {}'.format(text_piece))
#             return text_piece[1:4]


# big_string = 'pleases call me lou, my number is (760) 555-1212'
# print('here is the area code \'{}\''.format(area_code(big_string)))

# Test.assert_equals(format_poem('Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex. Complex is better than complicated.'), 'Beautiful is better than ugly.\nExplicit is better than implicit.\nSimple is better than complex.\nComplex is better than complicated.')
# Test.assert_equals(format_poem("Flat is better than nested. Sparse is better than dense. Readability counts. Special cases aren't special enough to break the rules."), "Flat is better than nested.\nSparse is better than dense.\nReadability counts.\nSpecial cases aren't special enough to break the rules.")
# Test.assert_equals(format_poem("Although practicality beats purity. Errors should never pass silently. Unless explicitly silenced. In the face of ambiguity, refuse the temptation to guess."), "Although practicality beats purity.\nErrors should never pass silently.\nUnless explicitly silenced.\nIn the face of ambiguity, refuse the temptation to guess.")


poem = 'Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex. Complex is better than complicated.'

# poem=format_poem('this is a story.  about a man named jed.  and that is all.')
print('poem=\n{}'.format(format_poem(poem)))


