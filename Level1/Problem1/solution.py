def solution(s):
    # avoid calling len repeatedly since function calls are expensive
    len_str = len(s)
    # going from size 1 to length of the string
    for x in xrange(1, len_str+1):
        # only to consider lengths which divide string completely
        if len_str%x == 0:
            # store substring
            sub_str = s[:x]
            num_substr = len_str/x
            # if sub_str repeated num_substr times equals s then it is valid
            if sub_str*num_substr == s:
                # num_substr is max since we are going from length 1 to string length
                return num_substr