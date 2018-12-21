# You're putting together contact information for all the users of your website to ship them a small gift. You queried
# your database and got back a list of users, where each user is another list with up to two items:
#       a string representing the user's name and their shipping zip code. Example data might look like:
#
# [["Grae Drake", 98110], ["Bethany Kok"], ["Alex Nussbacher", 94101], ["Darrell Silver", 11201]]
# Notice that one of the users above has a name but doesn't have a zip code.
#
# Write a function user_contacts() that takes a two-dimensional list like the one above and returns
# a dictionary with an item for
# each user where the key is the user's name and the value is the user's zip code.
# If your data doesn't include a zip code then the value should be None.
#
# For example, using the input above, user_contacts() would return this dictionary:
#
# {
#     "Grae Drake": 98110,
#     "Bethany Kok": None,
#     "Alex Nussbacher": 94101,
#     "Darrell Silver": 11201,
# }

def user_contacts(data):
    # Your code here.
    data_json = {}
    contact_list: object
    for contact_list in data:
        if len(contact_list) == 2:
            data_json[contact_list[0]] = contact_list[1]
        else:
            data_json[contact_list[0]] = None

    return data_json




data = [["Grae Drake", 98110], ["Bethany Kok"], ["Alex Nussbacher", 94101], ["Darrell Silver", 11201]]
data1 = user_contacts(data)
print('data1 = {}'.format(data1))
# expected_result = {'Grae Drake': 98110, 'Darrell Silver': 11201, 'Alex Nussbacher': 94101, 'Bethany Kok': None}
# test.assert_equals(user_contacts(data), expected_result)