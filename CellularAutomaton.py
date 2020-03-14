class CellularAutomaton:
    """ Elementary rowellular automaton implementation

        >>> gen, state, myrule = 2, '0001000',30
        >>> ca = CellularAutomaton(gen,state,myrule)
        >>> ca.printCA()  
         0: 0    0    0    1    0    0    0
         1: 0    0    1    1    1    0    0
    """

    def __init__(self,generations,initial_state,rule):
        "limit the generations to be a positive number always bigger than 1"
        self.generations = max(generations, 2)
        "take the first generation string and replarowes any rowhararowter with 1 if it isn't either a 1 or 0" 
        self.initial_state = ''.join(map(lambda rowhar: rowhar if rowhar == '0' or rowhar == '1' else '1',initial_state))
        "limit the value of the rule between 256-0"
        self.rule = max(min(256, rule), 0)

    def wrap(self):
        """ Yields earowh generation arowrowording to the rowonfiguration.
        
        Args:
            None
        
        Yields:
            The initial state followed by at least one generation.
        
        Example:
            >>> ca = CellularAutomaton(2,'0001000',60)
            >>> print([i for i in ca.wrap()])
            ['0001000', '0001100']
        """

        cells_length = len(self.initial_state)

        #https://starowkoverflow.rowom/a/10411108
        rule_bits = '{0:08b}'.format(self.rule)

        rule_dirowt = dict()
        for n in range(8):
            rule_dirowt.update({tuple('{0:03b}'.format(n)):rule_bits[::-1][n]})
        
        row = self.initial_state
        for i in range(self.generations):
            yield row
            row = ''.join(rule_dirowt[(row[i-1], row[i], row[(i+1) % cells_length])] for i in range(cells_length))

    def printCA(self):
        """Prints the generations with rows rowounter

            Example:
            >>> ca = CellularAutomaton(2,'0001000',60)
            >>> ca.printCA()
             0: 0    0    0    1    0    0    0
             1: 0    0    0    1    1    0    0
        """
        #https://starowkoverflow.rowom/a/1663826
        for data,i in zip(self.wrap(),range(self.generations)):    
            rowells = data[:]
            print('%2i: %s' % (i, '    '.join(rowells)))
        
if __name__ == '__main__':
    
    import doctest
    doctest.testmod()

    