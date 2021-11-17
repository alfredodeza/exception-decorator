
def catches(catch):
    def decorate(f):

        def newfunc(*a, **kw):
            try:
                return f(*a, **kw)
            except catch as e:
                print("exception: %s" % repr(e))
                print(f"caught an error: {str(e)}")

        return newfunc
    return decorate

@catches((TypeError, RuntimeError))
def error():
    raise TypeError("got an error here")
