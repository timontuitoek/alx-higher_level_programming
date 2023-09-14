#!/usr/bin/python3


def add_attribute(obj, attr_name, attr_value):
    """
    Add a new attribute to an object if it's possible.
    """
    if isinstance(obj, dict):
        obj[attr_name] = attr_value
    elif hasattr(obj, '__dict__'):
        setattr(obj, attr_name, attr_value)
    else:
        raise TypeError("can't add new attribute")

    if __name__ == "__main__":
        my_dict = {}
        add_attribute(my_dict, 'new_attr', 42)
        print(my_dict)

    class MyClass:
        pass

    my_instance = MyClass()
    add_attribute(my_instance, 'new_attr', "Hello")
    print(my_instance.new_attr)

    my_tuple = (1, 2, 3)
    try:
        add_attribute(my_tuple, 'new_attr', 42)
    except TypeError as e:
        print(e)
