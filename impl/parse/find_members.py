#
# function to return members of dict and print non members (all lowercase)
#

def findMembers(input_names, names):
    if input_names == "" or input_names == []:
        raise RuntimeError("no inputs to determine membership")

    # setup output lists
    members = []
    nonmembers = []

    # now iter over placing in each list
    for el in input_names:
        el_lower = el.lower()
        if el_lower in names:
            members.append(el_lower)
        else:
            nonmembers.append(el_lower)

    # return the members
    return members
