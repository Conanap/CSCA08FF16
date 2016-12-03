''' note: the question is slightly vague so you should always ask.
Eg: Does the santa have a list of child to gift?
They might say it's up to your design, in which case you have to decide
what is better. Hard code a list in there or dynamically code a list there
(or let it be passed), or utilize another way, eg here we let the child have
what gift they want and the santa asks them for what they want

Don't forget docstrings and comments, i'm lazy so no doc strings.
'''

Elf():
    def __init__(self, filename):
        self._bad = set()
        file = open(filename, 'r')
        for line in file:
            # for each line in the file, split at comma, take the name
            self._bad.add(line.split(',')[0])
        file.close()

    def is_bad(self, name):
        return name in self._bad

Santa():
    def __init__(self):
        pass

    def give_presents(self, children, gifts):
        for child in children:
            if(self._elf.is_bad(name)):
                return None
            else:
                return gifts.get_gift(child.want())

Child():

    def __init__(self, wanted):
        self._wanted = wanted

    def recieve_present(self, gift):
        if(present is None):
            self._gift = 'nothing'
        else:
            self._gift = gift

    def want():
        return self._wanted

    def __str__(self):
        return 'I wanted ' + self._wanted + ' and got ' + self._gift

Sack():
    def __init__(self):
        self._gifts = []

    def add_gift(self, gift):
        self._gifts.append(gift)

    def get_gift(self, gift):
        if(gift in self._gifts):
            self._gifts.remove(gift)
            return gift
        else:
            return None