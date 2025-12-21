def one_edit_apart(str1: str, str2: str) -> bool:
    if len(str1) < len(str2):
        str1, str2 = str2, str1

    edits = 0
    p1, p2 = 0, 0
    while p1 < len(str1) and p2 < len(str2):

        if str1[p1] == str2[p2]:
            p1 += 1
            p2 += 1
            continue

        edits += 1
        if p2 + 1 < len(str2) and str1[p1] == str2[p2 + 1]:
            p1 += 1
            p2 += 2
        elif p1 +1 < len(str1) and str1[p1 + 1] == str2[p2]:
            p1 += 2
            p2 += 1
        else:
            p1 += 1
            p2 += 1

    return edits <= 1


def main():
    print(one_edit_apart("cat", "dog") == False)
    print(one_edit_apart("cat", "cats") == True)
    print(one_edit_apart("cat", "cut") == True)
    print(one_edit_apart("cat", "cast") == True)
    print(one_edit_apart("cat", "at") == True)
    print(one_edit_apart("cat", "act") == False)


if __name__ == '__main__':
    main()
