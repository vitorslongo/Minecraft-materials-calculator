class Results:
    def __init__(self):
        self.results = {}

    def translate_structure_to_blocks(self):
        # base materials (base item / yields)
        sticks = 2 / 4

        # actual materials (yields / necessary base item)
        # all
        stairs = 6/4
        slabs = 2
        
        # wood
        log = 4   
        fence = 4 + 2 * sticks
        fence_door = 2 + 4 * sticks
        door = 3 / 6
        pressure_plate = 1 / 2

        # other
        glass_pane = 16 / 6
        iron_bars = 16 / 6

        # special
        ladder = 3 / 7 * sticks
        cauldron = 1 / 7
