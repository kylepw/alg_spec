"""Kosaraju implementation."""
from ktopo import rts
import argparse
import os


def file_to_graph(path: str) -> dict:
    """Convert text file with two vertices per line to graph.

        Args:
            path: file path

        Returns:
            Dictionary of vertices/outgoing adjacent vertices

        Raises:
            IOError if file not found or invalid data.
    """
    graph = {}
    try:
        with open(path) as f:
            v = [v.strip().split()[:2] for v in f.readlines() if len(v) > 1]
            v = [(int(x), int(y)) if all([x.isdigit(), y.isdigit()]) else (x, y) for x, y in v]
            graph = {}
            for tail, head in v:
                if tail in graph:
                    graph[tail].append(head)
                else:
                    graph[tail] = [head]
    except IOError:
        raise IOError(f'{path} does not exist.')
    except ValueError:
        raise ValueError('Invalid file. Must contain two vertices per line.')

    return graph


def get_parser():
    parser = argparse.ArgumentParser(
        description='Count SSC (strongly connected components) of graph from file'
    )
    parser.add_argument('filename', metavar='file', help='file with two vertices per line')
    return parser

def main():
    parser = get_parser()
    args = vars(parser.parse_args())

    graph = file_to_graph(args['filename'])
    print(graph)
    #t_vals = rts(graph)
    #print(t_vals)

if __name__ == '__main__':
    main()