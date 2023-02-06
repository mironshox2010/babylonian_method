def main(S, d):
    '''create a babylonian function.
    
    Args:
        S (int): number
        d (int): numnber
        
    Returns:
        float: result
    '''
    a =(( S - d**2)/d*2)
    b =(a + d)
    x =((b - a**2)/b*2)
    return x
print(main(16,4))