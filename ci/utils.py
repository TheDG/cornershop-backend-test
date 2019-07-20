"""Auxiliary method to get list of files you want to run your linters on"""

import path


def collect_sources(ignore_func):
    """Get list of files ignoring those by ignore_function"""
    top_path = path.Path(".")
    for py_path in top_path.walkfiles("*.py"):
        py_path = py_path.normpath()  # get rid of the leading '.'
        if not ignore_func(py_path):
            yield py_path


def collect_all_sources():
    """Get list of all files starting from top directory"""
    top_path = path.Path(".")
    for py_path in top_path.walkfiles("*.py"):
        py_path = py_path.normpath()  # get rid of the leading '.'
        yield py_path
