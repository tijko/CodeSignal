def reverse_parenthesis(string):
    substrings = []
    built = ''
    count = 0
    for s in string:
        if s != '(' and s!= ')':
            if count:
                substrings[-1] += s
            else:
                built += s
        elif s == '(':
            count += 1
            substrings.append('')
        elif s == ')':
            count -= 1
            substring = substrings.pop(-1)[::-1]
            if count:
                substrings[-1] += substring
            else:
                built += substring
    return built

if __name__ == '__main__':
    t = 'foo(bar(baz))blim'
    print(reverse_parenthesis(t))
