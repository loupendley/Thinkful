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

def modes_best_solution(data):
    frequency = {}
    mode_list = []

    # adds or creates a counter for each character
    for d in data:
        print("d = {}".format(d))
        if d in frequency:
            frequency[d] += 1
        else:
            frequency[d] = 1

    # adds modes from the dictionary to a list, and checks that there is a mode
    for f in frequency:
        if frequency[f] == max(frequency.values()) > min(frequency.values()):
            mode_list.append(f)

    return sorted(mode_list)

def modes(data):
    mode_json = {}
    if isinstance(data, list) and isinstance(data[0], str):
        data1 = data[0]
    else:
        data1 = data

    for letter in data1:
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
                if value >= max_value:
                    max_value = value

            for key, value in mode_json.items():
                if value == max_value:
                    mode.append(key)
        else:
            mode = []
    except:
        x = 1

    if len(mode) == len(data1) / 2 or len(mode) == len(data1):
        mode = []
    else:
        mode.sort()

    return mode

    # for i in len(mode_json):
    #     if mode_json.value() >= max:
    #         max =
    print('mode_json = {}'.format(mode_json))
    print("mode={}".format(mode))
print("modes with tomato is {}".format(modes("tomato")))
print("modes with redder is {}".format(modes(["redder"])))
print("modes with 1337 is {}".format(modes([1, 3, 3, 7])))
print("modes with 02346 is {}".format(modes([0, 2, 3, 4, 6])))

print("modes_best_solution with tomato is {}".format(modes_best_solution("tomato")))
print("modes_best_solution with redder is {}".format(modes_best_solution(["redder"])))
print("modes_best_solution with 1337 is {}".format(modes_best_solution([1, 3, 3, 7])))
print("modes_best_solution with 02346 is {}".format(modes_best_solution([0, 2, 3, 4, 6])))

# test.assert_equals(modes("tomato"), ["o", "t"])
# test.assert_equals(modes([1, 3, 3, 7]), [3])
    # test.assert_equals(modes(["redder"]), [])

# x=modes("what we have here is a failure to communicate")