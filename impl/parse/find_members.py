#
# function to return members of dict and print non members (all lowercase)
#

def find_members(input_names, names_dict):
    # setup output lists
    members = []
    nonmembers = []

    # now iter over placing in each list
    for el in input_names:
        el_lower = el.lower()
        if el_lower in names_dict:
            members.append(el_lower)
        else:
            nonmembers.append(el_lower)

    # return the members
    return members
