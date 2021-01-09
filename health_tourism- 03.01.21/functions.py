def full_name_fix(s):
    # full name input situation
    full = []
    fname = s.split(' ')[0]
    lname = s.split(' ')[1]
    first_letter = fname[0].upper()
    full.append(first_letter + fname[1:])
    first_letter = lname[0].upper()
    full.append(first_letter + lname[1:])
    return full


def name_fix(s):
    # input of first or last name only
    fname = s.split(' ')[0]
    first_letter = fname[0].upper()      # first letter of the first name
    return first_letter + fname[1:]