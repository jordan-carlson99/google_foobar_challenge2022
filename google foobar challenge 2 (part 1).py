def solution(s):
    list_length = len(s)
    s = list(s)
    right_loc = []
    left_loc = []
    y = 0

    # Find location of < and > put location on a list for comparing
    for i in range(list_length):
        try:
            right = s[i:i+1].index('>')
            right_loc.append((right + i))
        except ValueError:
            pass
        try:
            left = s[i:i+1].index('<')
            left_loc.append((left + i))
        except ValueError:
            pass

    left_loc_l = len(left_loc)
    right_loc_l = len(right_loc)

    # Compare every value in left_loc against every value in right_loc, compare to see if they will 'pass' each other
    for t in range(left_loc_l):
        for x in range(right_loc_l):
            if left_loc[t] > right_loc[x]:
                y += 2
            elif left_loc[t] < right_loc[x]:
                pass
            else:
                break

    return y





        # > = 3,5,8,12  < = 6,9
print(solution('<<>><'))
