# You probably know that the "mode" of a set of data is the data point that appears most frequently.
# Looking at the characters that make up the string "sarsaparilla" we can see that the letter "a" appears
# four times, more than any other letter, so the mode of "sarsaparilla" is "a".
#
# But do you know what happens when two or more data points occur the most? For example, what is the mode
# of the letters in "tomato"? Both "t" and "o" seem to be tied for appearing most frequently.
#
# Turns out that a set of data can, in fact, have multiple modes, so "tomato" has two modes: "t" and "o".
# It's important to note, though, that if all data appears the same number of times there is no mode. ' \
#   'So "cat", "redder", and [1, 2, 3, 4, 5] do not have a mode.
#
# Your job is to write a function modes() that will accept one argument data that is a sequence like a
# string or a list of numbers and return a sorted list containing the mode(s) of the input sequence.
# If data does not contain a mode you should return an empty list.

# >>> modes("tomato")
# ["o", "t"]
# >>> modes([1, 3, 3, 7])
# [3]
# >>> modes(["redder"])
# []

def modes(data):
    # Your code here.
    mode_json = {}
    for letter in str(data):
        # print('letter = {}'.format(letter))
        try:
            if mode_json[letter]:
                mode_json[letter] += 1
        except:
            mode_json[letter] = 1

    max_value = -1
    mode = []
    try:
        if mode_json[letter]:

            for key, value in mode_json.items():
                # print("x1234 here is a value {}".format(value))
                if value >= max_value:
                    # print("mx found {}".format(value))
                    max_value = value

            for key, value in mode_json.items():
                # print("key={}, value={}".format(key, value))
                if value == max_value:
                    # print('we are appending {} to the mode list'.format(key))
                    mode.append(key)
    except:
        x = 1

    if len(mode) == len(data) / 2:
        mode = []

    return mode

    # for i in len(mode_json):
    #     if mode_json.value() >= max:
    #         max =
    print('mode_json = {}'.format(mode_json))
    print("mode={}".format(mode))
print("modes with tomato is {}".format(modes("tomato")))
print("modes with redder is {}".format(modes("redder")))
# test.assert_equals(modes("tomato"), ["o", "t"])
# test.assert_equals(modes([1, 3, 3, 7]), [3])
    # test.assert_equals(modes(["redder"]), [])

# x=modes("what we have here is a failure to communicate")