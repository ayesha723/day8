def is_integer(w):
    try:
        int(w)
        return True
    except:
        return False
    
print(is_integer("123"))
print(is_integer("hello"))