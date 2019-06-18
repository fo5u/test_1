def test(*args):
    return  sum(args)

print test(1,2,3,4,55)

def test(**kwargs):
    return sum(kwargs)

