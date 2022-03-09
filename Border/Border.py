def solution(picture):
    picture = ['*' * (len(picture[0]) + 2)] + picture
    picture.append('*' * (len(picture[-1]) + 2))
    for i,v in enumerate(picture[1:-1], 1):
        picture[i] = '*' + picture[i] + '*'
    return picture

if __name__ == '__main__':
    t = ['abc', 'ded']
    out = solution(t)
    for i in out:
        print(i)
