import random

from pybrood import BaseAI, game

"""
Example script that gathers available minerals

http://pybrood.readthedocs.io/en/latest/
"""
class Script(BaseAI):
    def prepare(self):
        self.self = game.self()  # to use type annotations: self.self: Player = game.self()
        self.enemy = game.enemy()

        game.print('Starting example script')

    def frame(self):
        visibleMinerals = [m for m in game.getMinerals() if m.isVisible()]

        for unit in self.self.getUnits():
            if not unit.isGatheringMinerals() and visibleMinerals:
                unit.gather(random.choice(visibleMinerals))

    def finished(self):
        pass
