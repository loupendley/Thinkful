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


# poem = 'Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex. Complex is better than complicated.'

# poem=format_poem('this is a story.  about a man named jed.  and that is all.')
# print('poem=\n{}'.format(format_poem(poem)))

# You have a bunch of red and blue marbles. To start the game you grab a handful of marbles of each color and put them into the bag,
# keeping track of how many of each color go in. You take turns reaching into the bag, guessing a color, and then pulling one marble out.
# You get a point if you guessed correctly. The trick is you only have three seconds to make your guess, so you have to think quickly.
#
# You've decided to write a function, guess_blue() to help automatically calculate whether you should guess "blue" or "red".
# The function should take four arguments:
#
# the number of blue marbles you put in the bag to start
# the number of red marbles you put in the bag to start
# the number of blue marbles pulled out so far, and
# the number of red marbles pulled out so far.
# guess_blue() should return the probability of drawing a blue marble, expressed as a float. For example, guess_blue(5, 5, 2, 3) should return 0.6.
# Test.assert_equals(guess_blue(5, 5, 2, 3), 0.6)
# Test.assert_equals(guess_blue(5, 7, 4, 3), 0.2)
# Test.assert_equals(guess_blue(12, 18, 4, 6), 0.4)
# def guess_blue(blue_start, red_start, blue_pulled, red_pulled):
#     # Your code here.
#     return float(blue_start - blue_pulled)/float( (blue_start - blue_pulled) + (red_start - red_pulled))
#
# print('blue_prob = {}'.format(guess_blue(5,5,2,3)))
# print('blue_prob = {}'.format(guess_blue(5,7,4,3)))
#
# print('blue_prob = {}'.format(guess_blue(12,18,4,6)))

# def box_capacity(length, width, height):
#     # Your code here.
#     box_size = float(16/12 * 16/12 * 16/12)
#     return int(float(length * width * height)/box_size)

# import math
#
# def box_capacity(length, width, height):
#     # Your code here.
#     length_inches = length * 12
#     width_inches = width * 12
#     height_inches = height * 12
#     warehouse_size = length_inches * width_inches * height_inches
#     box_size = int(16 * 16* 16)
#     return math.floor(warehouse_size / box_size)
#
#     # correct solution     return (length * 12 // 16) * (width * 12 // 16) * (height * 12 // 16)
# print('box1 = {}'.format(box_capacity(32,64,16)))
# print('box2 = {}'.format(box_capacity(20,20,20)))
# print('box3 = {}'.format(box_capacity(80,40,20)))


# Test.assert_equals(box_capacity(32, 64, 16), 13824)
# Test.assert_equals(box_capacity(20, 20, 20), 3375)
# Test.assert_equals(box_capacity(80, 40, 20), 27000)
import math

def test_roots(actual, expected):
    a, b = sorted(actual), sorted(expected)
    Test.expect(almost_equals(a[0], b[0]) and almost_equals(a[1], b[1]),
        "roots should be almost equal\nRecieved {}\nExpected {}".format(a, b))

# Test.describe("Basic tests")
# test_roots(quadratic_formula(2, 16, 1), [-7.937003937005906, -0.06299606299409444])
# test_roots(quadratic_formula(4, 21, 3), [-5.103028450199876, -0.14697154980012384])
# test_roots(quadratic_formula(6, 81, 3), [-13.462860791048776, -0.037139208951224134])
def quadratic_formula(a, b, c):

    root1 = (-b + math.sqrt(b**2 - (4 * (a*c))))/(2 * a)  # Put -b + something something here.

    root2 = (-b - math.sqrt(b**2 - (4*(a*c))))/(2 * a)  # Put -b - something something here.

    return [root1, root2]

print("value1 = {}".format(quadratic_formula(2, 16, 1)))