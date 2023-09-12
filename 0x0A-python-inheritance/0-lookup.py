#!/usr/bin/python3
"""Defineing an object attribute lookup function."""


def lookup(obje):
    """Returning a list of object's available attributes."""
    return (dir(obje))
