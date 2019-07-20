"""Python script that runs McCabe on all files."""

import ast
import sys
import mccabe

from utils import collect_all_sources


def process(py_source, max_complexity):
    """Method to run McCabe complexity analizer for a file."""
    code = py_source.text()
    tree = compile(code, py_source, "exec", ast.PyCF_ONLY_AST)
    visitor = mccabe.PathGraphingAstVisitor()
    visitor.preorder(tree, visitor)
    for graph in visitor.graphs.values():
        if graph.complexity() > max_complexity:
            text = "{}:{}:{} {} {}"
            return text.format(py_source, graph.lineno, graph.column, graph.entity,
                               graph.complexity())
        return None


def main():
    """Main function for McCabe script. Runs McCabe for all files"""
    max_complexity = int(sys.argv[1])
    okay = True
    for py_source in collect_all_sources():
        error = process(py_source, max_complexity)
        if error:
            okay = False
            print(error)
    if not okay:
        sys.exit(1)


if __name__ == "__main__":
    main()
