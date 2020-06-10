
def slidingWindowTemplate(s, t):
    #  init a collection or int value to save the result according to the question
    results = []
    if len(t) > len(s):
        return results

    # create a hash map to save the characters of the target substring
    # (key, value) = (Character, Frequency of the Characters)
    hashmap = {}
    for c in range(len(t)):
        hashmap[t[c]] = hashmap.get(t[c], 0) + 1

    # maintain a counter to check whether match th etaget string
    counter = len(hashmap)

    # Two Pointers: begin - left pointer of the window; end - right pinter of the window
    begin, end = 0, 0

    # the length of the substring which match the target string
    length = 0

    # loop at the beginning of the source string
    while end < len(s):
        c = s[end]  # get a character

        if c in hashmap:
            hashmap[c] = hashmap.get(c, 0) - 1 # plus or minus one
            if hashmap[c] == 0:  # modify the counter according to the requirements (different condition).
                counter += -1
        end += 1

        # increase begin pointer to make it invalid/valid again
        while counter == 0:  # *counter condition. different question may have different condition
            tempc = s[begin] # ***be careful here: choose the char at begin pointer, NOT the end pointer
            if tempc in hashmap:
                hashmap[tempc] = hashmap[tempc] + 1 # plus or minus one
                if hashmap[tempc] > 0: # modify the counter according to the requirements (different condition)
                    counter += 1
                # save / update (min/ max) the result if find a target
                # result collection or result int value
                begin += 1

        return results


