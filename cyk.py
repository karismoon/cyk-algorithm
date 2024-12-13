from cyk_helpers import (
    find_original_state,
    find_substrings,
    cartesian_product
)

from library import example_cfg
string = "baaba"

processed_symbols = {}

for iteration_row in range(len(string)):
    for iteration_square in range(len(string) - iteration_row):
        square_substring_len = iteration_row + 1