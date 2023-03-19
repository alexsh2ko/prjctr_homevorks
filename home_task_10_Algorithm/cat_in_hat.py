

def cats_in_hats(num_cats: int, num_rounds: int) -> str:
    '''
    The function counts how many cats will remain in hats, depending on the number of circles
    
    Parameters
    ----------
        num_cats : the variable contains a cat count
        num_rounds: the variable contains a number of rounds

    Returns
    -------
    The list contain the number of cats in hats
    '''
    cats = [0] * num_cats
    for i in range(1, num_rounds + 1):
        for j in range(0, num_cats):
            if (j + 1) % i == 0:       
                cats[j] = not cats[j]
    hatted_cats = [i+1 for i in range(len(cats)) if cats[i]]
    return hatted_cats



