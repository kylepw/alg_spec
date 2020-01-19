#!/usr/bin/env python3
"""File describes a set of jobs with positive and integral weights and
lengths. It has the format:

[number_of_jobs]

[job_1_weight] [job_1_length]

[job_2_weight] [job_2_length]

...

For example, the third line of the file is "74 59", indicating that the
second job has weight 74 and length 59.

You should NOT assume that edge weights or lengths are distinct.

Your task in this problem is to run the greedy algorithm that schedules
jobs in decreasing order of the difference (weight - length). Recall from
lecture that this algorithm is not always optimal. IMPORTANT: if two jobs
have equal difference (weight - length), you should schedule the job with
higher weight first. Beware: if you break ties in a different way, you are
likely to get the wrong answer. You should report the sum of weighted
completion times of the resulting schedule --- a positive integer --- in
the box below.
"""
import argparse

def extract_jobs(filename):
    """Extract total number of jobs, job weight, length.

        Args:
            filename: text file with job data

        Returns:
           (int, list of tuples) -> (total num of jobs, [(weight, length), ...])
    """

    total = 0
    jobs = []
    with open(filename) as f:
        total = int(f.readline())
        for job in f:
            jobs.append(tuple(int(i) for i in job.split()))

    return total, jobs

def sort_jobs(jobs, key, reverse=False):
    """Sort jobs in decreasing order of the ratio (weight - length).

        Args:
            jobs: list of (job weight, length)
            key: key to sort by
            reverse: sort in descending order (default is False)

    """
    jobs.sort(key=key, reverse=reverse)

def sum_weighted_completion_times(jobs):
    """Return sum of weighted completion times."""
    total = 0
    time_so_far = 0
    for j in jobs:
        time_so_far += j[1]
        total += j[0] * time_so_far

    return total

def get_parser(description):
    parser = argparse.ArgumentParser(
        description=description
    )
    parser.add_argument(
        'filename',
        metavar='jobs.txt',
        help='file with one job [weight] [length] per line such as "74 39"'
    )
    return parser

def main():
    parser = get_parser(description='Greedy algorithm that schedules jobs in decreasing order by (weight - length).')
    parsed = vars(parser.parse_args())

    _, jobs = extract_jobs(parsed['filename'])

    sort_by_diff = lambda j: (j[0] - j[1], j[0])
    sort_jobs(jobs, key=sort_by_diff, reverse=True)

    print(sum_weighted_completion_times(jobs))

if __name__ == '__main__':
    main()