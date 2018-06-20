def copy_attrs(src, dst, attrs):
    for attr in attrs:
        if hasattr(src, attr):
            setattr(dst, attr, getattr(src, attr))
