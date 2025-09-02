def NULL_not_found(val):
    if val is None:
        print(f"Nothing : {val} {type(val)}")
    elif isinstance(val, float) and val != val:
        print(f"Cheese : {val} {type(val)}")
    elif val == 0 and not (isinstance(val, bool)):
        print(f"Zero : {val} {type(val)}")
    elif val == "":
        print(f"Empty : {val} {type(val)}")
    elif not val:
        print(f"Fake : {val} {type(val)})")
    else:
        print("Type not found")
        return 1
    return 0
