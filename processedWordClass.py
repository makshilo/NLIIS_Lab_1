class ProcessedWord:
    def __init__(self, lemma, pos, correct_prefixes, correct_suffixes):
        self.lemma = lemma
        self.pos = pos
        self.correct_prefixes = correct_prefixes
        self.correct_suffixes = correct_suffixes

    # __str__ method
    def __str__(self):
        return '{} {} {} {}'.format(self.lemma, self.pos, self.correct_prefixes, self.correct_suffixes)

    # __repr__ method
    def __repr__(self):
        return '{} {} {} {}'.format(self.lemma, self.pos, self.correct_prefixes, self.correct_suffixes)

    # properties
    @property
    def lemma(self):
        return self.__lemma

    @lemma.setter
    def lemma(self, value):
        self.__lemma = value

    @property
    def pos(self):
        return self.__pos

    @pos.setter
    def pos(self, value):
        self.__pos = value

    @property
    def correct_prefixes(self):
        return self.__correct_prefixes

    @correct_prefixes.setter
    def correct_prefixes(self, value):
        self.__correct_prefixes = value

    @property
    def correct_suffixes(self):
        return self.__correct_suffixes

    @correct_suffixes.setter
    def correct_suffixes(self, value):
        self.__correct_suffixes = value
