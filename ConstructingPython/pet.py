class Pet():
    """ A class to capture useful information regarding my pets, just incase I lose track of them."""

    def __init__(self, height=5):
        self.height = height
        self.is_human = False
        self.owner = 'Kanon'


chubbles = Pet(5)
if chubbles.is_human is False:
    print('Not a human')

print('owner name is: {}'.format(chubbles.owner))
# print(chubbles.__doc__)
print(chubbles.height)
