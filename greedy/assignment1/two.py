#!/usr/bin/env python3
"""Your task now is to run the greedy algorithm that schedules jobs
(optimally) in decreasing order of the ratio (weight/length). In this
algorithm, it does not matter how you break ties. You should report the
sum of weighted completion times of the resulting schedule --- a positive
integer.
"""
import argparse
from one import get_parser, extract_jobs, sort_jobs, sum_weighted_completion_times

def main():
    parser = get_parser(description='Run greedy algorithm that schedules jobs in decreasing order of the ratio (weight/length).')
    parsed = vars(parser.parse_args())
    print(parsed['filename'])

    _, jobs = extract_jobs(parsed['filename'])

    sort_by_diff = lambda j: (j[0] / j[1])
    sort_jobs(jobs, key=sort_by_diff, reverse=True)

    print(sum_weighted_completion_times(jobs))

if __name__ == '__main__':
    main()
