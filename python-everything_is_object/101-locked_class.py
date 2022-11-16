#!/usr/bin/python3
"""Defines a locked class. """


class LockedClass:
    """
Prevent the user from initiating new LockedClass attributes only
to attribute called 'first_name'
"""
    __slots__ = ["first_name"]
