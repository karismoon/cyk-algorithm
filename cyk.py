from cyk_helpers import (
    find_original_state,
    find_substrings,
    cartesian_product
)

from library import example_cfg
string = "baaba"

cfg = example_cfg
processed_symbols = cfg
print(find_substrings("a"))

for iteration_row in range(1, len(string)): 
    # For each possible substring length
    # Skip going over individual characters, already in the CFG
    print(f"\nrow {iteration_row}")
    for iteration_square in range(len(string) - iteration_row):
        # For each substring of the chosen length
        substring_len = iteration_row + 1
        substring = string[iteration_square:iteration_square + substring_len]
        print(f"\nsubstring: {substring}")
        
        # Find each possible split of the substring
        substring_splits = find_substrings(substring)
        initial_symbols = []

        for split in substring_splits:
            # For each split of the substring
            print(f"split: {split}")
            # Find the production rule for each split of the string
            rule1 = find_original_state(split[0], processed_symbols)
            rule2 = find_original_state(split[1], processed_symbols)
            
            print(f"split first part origin: {rule1}")
            print(f"split second part origin: {rule2}")

            products = cartesian_product(rule1, rule2)
            print(f"products: {products}")

            for product in products:
                # For each cartesian product
                initial_symbol = find_original_state(product, processed_symbols)
                if initial_symbol:
                    initial_symbols = initial_symbols + initial_symbol
                    initial_symbols = list(set(initial_symbols))
            print(f"initial symbols: {initial_symbols}")

        if substring not in processed_symbols and initial_symbols:
            processed_symbols[substring] = initial_symbols
            print(f"processed dict updated: {processed_symbols}")

if string in processed_symbols:
    print(f"\n\nFINAL ANSWER: {string} is in the given CFG, it can be obtained using these symbols: {processed_symbols[string]}")
else:
    print(f"\n\n{string} is not in the given CFG.")