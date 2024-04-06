# Cleaning data dengan fungsi generator

import csv
from typing import IO, Iterator, List, Text, Union, Iterable
from typing import Tuple, cast
import math

def row_iter(souce: IO) -> Iterator[List[Text]]:
    return csv.reader(souce, delimiter="\t")

def head_split_fixed(row_iter: Iterator[List[Text]]) -> Iterator[List[Text]]:
    title = next(row_iter)
    assert(len(title) == 1
            and title[0] == "Anscombe's quartet")
    heading = next(row_iter)
    assert(len(heading) == 4
            and heading == ['I', 'II', 'III', 'IV'])
    columns = next(row_iter)
    assert(len(columns) == 8
            and columns == ['x', 'y', 'x', 'y', 'x', 'y', 'x', 'y'])
    return row_iter

Pair = Tuple[str, str]
def series(n: int, row_iter: Iterable[List[Text]]) -> Iterator[Pair]:
    for row in row_iter:
        yield cast(Pair ,tuple(row[n*2:n*2+2]))

def calculate_variance(data):
    n = len(data)
    mean = sum(data) / n
    deviations = [(x - mean) ** 2 for x in data]
    variance = sum(deviations) / n
    return variance

def calculate_std_dev(variance):
    return math.sqrt(variance)
        
def main():
    with open("Anscombe.txt") as source:
        data = head_split_fixed(row_iter(source))
        print(list(data))
    print("paired:")
    with open("Anscombe.txt") as source:
        data = tuple(head_split_fixed(row_iter(source)))
        sample_1 = tuple(series(0, data))
        sample_2 = tuple(series(1, data))
        sample_3 = tuple(series(2, data))
        sample_4 = tuple(series(3, data))
        print(sample_1)
        print(sample_2)
        print(sample_3)
        print(sample_4)
    # rata2 dari x di sample_1
    mean = (sum(float(pair[0]) for pair in sample_1)) / len(sample_1)
    print(mean)
    # rata2 dari x di sample_1 s/d 4
    for subset in sample_1, sample_2, sample_3, sample_4:
        mean = (sum(float(pair[0]) for pair in subset)) / len(subset)
    print(mean)
    # varians dan standar deviasi dari x di sample_1 s/d 4
    for subset in sample_1, sample_2, sample_3, sample_4:
        data = [float(pair[0]) for pair in subset]
        variance = calculate_variance(data)
        std_dev = calculate_std_dev(variance)
        print(f'Varians: {variance}, Standar Deviasi: {std_dev}')
        
        
if __name__ == "__main__":
    main()


    

    