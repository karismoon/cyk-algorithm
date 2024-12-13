def find_original_state(symbol, processed):
    """
    Find the state that gives the given symbol.

    Args:
        symbol (string): Terminal or nonterminal state(s) to find the origin state of.
        processed (dict): Dynamic table with both relationships in the original CFG and those found through processing.
        
    Returns:
        A list of all the origin states.
    """
    if symbol in processed:
        return processed[symbol]
    return []

def find_substrings(string):
    """
    Find all the possible ways to split the given string into 2 strings.
    Args:
        string (string): String to be split up.
    
    Returns:
        A list of lists representing every possible pair of split strings.
    """
    substrings = []
    for index in range(1, len(string)):
        substrings.append([string[:index], string[index:]])
    return substrings

def cartesian_product(symbols1, symbols2):
    """
    Find all possible combinations of two groups of symbols.
    
    Args:
        symbols1 (list): Symbols to be combined with symbols2.
        symbols2 (list): Symbols to be combined with symbols1.
    
    Returns:
        A list of all combinations represented as strings, non-repeating.
    """
    products = []
    for symbol1 in symbols1:
        for symbol2 in symbols2:
            # print(f"symbol 1: {symbol1}")
            # print(f"symbol 2: {symbol2}")
            # product = "AB"
            if isinstance(symbol1, str) and isinstance(symbol2, str):
                product = symbol1 + symbol2
                if product not in products:
                    products.append(product)
    return products