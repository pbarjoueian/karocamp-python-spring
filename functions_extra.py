def foo(name: str, *args, **kwargs):
    print(args)
    print(kwargs)
    print(name)


foo("Ahmad", *("one", "two"), **{"x": "hello", "y": "Hi"})
