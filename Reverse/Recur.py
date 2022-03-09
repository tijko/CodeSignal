def recur(base, cnt, new, subs):
    if base == '':
        return new
    if base[0] == '(':
        subs.append('')
        cnt += 1
    elif base[0] == ')':
        cnt -= 1
        rev = subs.pop(-1)[::-1]
        if cnt != 0:
            subs[-1] += rev
        else:
            new += rev
    else:
        if cnt:
            subs[-1] += base[0]
        else:
            new += base[0]
    return recur(base[1:], cnt, new, subs)

def solution(string):
    return recur(string, 0, '', [])

if __name__ == '__main__':
    t = 'foo(bar(baz))blim'
    print(solution(t))
