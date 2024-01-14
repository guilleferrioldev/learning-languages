from dataclasses import dataclass, field, asdict

@dataclass(init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=False, match_args=True, kw_only=False, slots=False, weakref_slot=False)
class A(object):
    ...


"""
The parameters to dataclass() are:

1- init: If true (the default), a __init__() method will be generated.

2- repr: If true (the default), a __repr__() method will be generated. The generated repr string will have the class name and the name and repr of each field, in the order they are defined in the class. Fields that are marked as being excluded from the repr are not included. For example: InventoryItem(name='widget', unit_price=3.0, quantity_on_hand=10).

3- eq: If true (the default), an __eq__() method will be generated. This method compares the class as if it were a tuple of its fields, in order. Both instances in the comparison must be of the identical type.

4- order: If true (the default is False), __lt__(), __le__(), __gt__(), and __ge__() methods will be generated. These compare the class as if it were a tuple of its fields, in order. Both instances in the comparison must be of the identical type. If order is true and eq is false, a ValueError is raised.

5- unsafe_hash: If False (the default), a __hash__() method is generated according to how eq and frozen are set.
If eq and frozen are both true, by default dataclass() will generate a __hash__() method for you. If eq is true and frozen is false, __hash__() will be set to None, marking it unhashable (which it is, since it is mutable). If eq is false, __hash__() will be left untouched meaning the __hash__() method of the superclass will be used (if the superclass is object, this means it will fall back to id-based hashing).

6- frozen: If true (the default is False), assigning to fields will generate an exception. This emulates read-only frozen instances. If __setattr__() or __delattr__() is defined in the class, then TypeError is raised. See the discussion below.

7- match_args: If true (the default is True), the __match_args__ tuple will be created from the list of parameters to the generated __init__() method (even if __init__() is not generated, see above). If false, or if __match_args__ is already defined in the class, then __match_args__ will not be generated.

8- kw_only: If true (the default value is False), then all fields will be marked as keyword-only. If a field is marked as keyword-only, then the only effect is that the __init__() parameter generated from a keyword-only field must be specified with a keyword when __init__() is called. There is no effect on any other aspect of dataclasses. See the parameter glossary entry for details. Also see the KW_ONLY section.

9- slots: If true (the default is False), __slots__ attribute will be generated and new class will be returned instead of the original one. If __slots__ is already defined in the class, then TypeError is raised.

10- weakref_slot: If true (the default is False), add a slot named “__weakref__”, which is required to make an instance weakref-able. It is an error to specify weakref_slot=True without also specifying slots=True.

"""


@dataclass
class B(object):
    mylist: list[int] = field(default_factory=list)

"""
1- default: If provided, this will be the default value for this field. This is needed because the field() call itself replaces the normal position of the default value.

2- default_factory: If provided, it must be a zero-argument callable that will be called when a default value is needed for this field. Among other purposes, this can be used to specify fields with mutable default values, as discussed below. It is an error to specify both default and default_factory.

3- init: If true (the default), this field is included as a parameter to the generated __init__() method.

4- repr: If true (the default), this field is included in the string returned by the generated __repr__() method.

5- hash: This can be a bool or None. If true, this field is included in the generated __hash__() method. If None (the default), use the value of compare: this would normally be the expected behavior. A field should be considered in the hash if it’s used for comparisons. Setting this value to anything other than None is discouraged.
One possible reason to set hash=False but compare=True would be if a field is expensive to compute a hash value for, that field is needed for equality testing, and there are other fields that contribute to the type’s hash value. Even if a field is excluded from the hash, it will still be used for comparisons.

6- compare: If true (the default), this field is included in the generated equality and comparison methods (__eq__(), __gt__(), et al.).

7- metadata: This can be a mapping or None. None is treated as an empty dict. This value is wrapped in MappingProxyType() to make it read-only, and exposed on the Field object. It is not used at all by Data Classes, and is provided as a third-party extension mechanism. Multiple third-parties can each have their own key, to use as a namespace in the metadata.

8- kw_only: If true, this field will be marked as keyword-only. This is used when the generated __init__() method’s parameters are computed.

"""


@dataclass
class Rectangle(object):
    height: float
    width: float

@dataclass
class Square(Rectangle):
    side: float

    def __post_init__(self):
        super().__init__(self.side, self.side)

"""
 dataclasses.__post_init__()

When defined on the class, it will be called by the generated __init__(), normally as self.__post_init__(). However, if any InitVar fields are defined, they will also be passed to __post_init__() in the order they were defined in the class. If no __init__() method is generated, then __post_init__() will not automatically be called.
"""


