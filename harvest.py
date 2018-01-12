############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

        self.pairings = []

        # Fill in the rest

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""
        self.pairings.append(pairing)
    def add_pairings(self, pairings):
        """Add multiple pairings, provide an iterable"""
        self.pairings.extend(pairings)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""
        self.code = new_code
        # Fill in the rest


def make_melon_types():
    """Returns a list of current melon types."""
    all_melon_types = []

    musk = MelonType('musk', 1998, 'green',
                     False, True, 'Muskmelon')
    musk.add_pairing('mint')
    all_melon_types.append(musk)

    cas = MelonType('cas', 2003, 'orange',
                     True, False, 'Casaba')
    cas.add_pairings(['strawberries', 'mint'])
    all_melon_types.append(cas)

    cren = MelonType('cren', 1996, 'green',
                     True, False, 'Crenshaw')
    cren.add_pairing('proscuitto')
    all_melon_types.append(cren)

    yw = MelonType('yw', 2013, 'yellow',
                     True, True, 'Yellow Watermelon')
    yw.add_pairing('ice cream')
    all_melon_types.append(yw)


    return all_melon_types



def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""
    for melon_type in melon_types:
        pairings = melon_type.pairings
        print "{name} pairs with".format(name=melon_type.name)
        for pair in melon_type.pairings:
            print "-{}".format(pair)
            print

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""
    melon_code = {}
    for melon_type in melon_types:
        melon_code[melon_type.code] = melon_type
    return melon_code



    

############
# Part 2   #
############



class Melon(object):
    """A melon in a melon harvest."""
    def __init__(self, melon_id, melon_type, shape_rating, color_rating, harvested_from, harvested_by):
        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.harvested_from = harvested_from
        self.harvested_by = harvested_by
        self.id = melon_id

    # Fill in the rest
    # Needs __init__ and is_sellable methods
    def is_sellable(self):
        return self.color_rating > 5 and self.shape_rating > 5 and self.harvested_from != 3


def make_melons(melon_types):
    """Returns a list of Melon objects."""
    melons = []
    melon_by_type = make_melon_type_lookup(melon_types)

    melon1 = Melon(1, melon_by_type['yw'], 8, 7, 2, 'Sheila')
    melons.append(melon1)

    melon2 = Melon(2, melon_by_type['yw'], 3, 4, 2, 'Sheila')
    melons.append(melon2)


    melon3 = Melon(3, melon_by_type['yw'], 9, 8, 3, 'Sheila')
    melons.append(melon3)

    melon4 = Melon(4, melon_by_type['cas'], 10, 6, 35, 'Sheila')
    melons.append(melon4)

    melon5 = Melon(5, melon_by_type['cren'], 8, 9, 35, 'Michael')
    melons.append(melon5)

    melon6 = Melon(6, melon_by_type['cren'], 8, 2, 35, 'Michael')
    melons.append(melon6)

    melon7 = Melon(7, melon_by_type['cren'], 2, 3, 4, 'Michael')
    melons.append(melon7)

    melon8 = Melon(8, melon_by_type['musk'], 6, 7, 4, 'Michael')
    melons.append(melon8)

    melon9 = Melon(9, melon_by_type['yw'], 7, 10, 3, 'Sheila')
    melons.append(melon9)

    return melons

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""
    



