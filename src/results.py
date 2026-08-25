class Results:
    def __init__(self):
        self.results = {}
        self.define_multipliers()

    def get_structure_to_base_multiplier(self, structure_type:str):
        structure = structure_type.lower()
        
        multiplier = {
            "planks": self.planks,
            "fence": self.fence,
            "fence door": self.fence_door,
            "door": self.door,
            "pressure plate": self.pressure_plate,
            "glass pane": self.glass_pane,
            "iron bars": self.iron_bars,
            "ladder": self.ladder,
            "cauldron": self.cauldron,
        }
        
        return multiplier[structure]

    def get_base_name(self, structure_type: str):
        structure = structure_type.lower()
        return {
            "planks": "logs",
            "stairs": "logs",
            "slabs": "logs",
            "fences": "planks",
            "fence doors": "planks",
            "doors": "planks",
            "pressure plates": "planks",
            "glass panes": "glass",
            "iron bars": "iron ingots",
            "cauldrons": "iron ingots",
            "ladders": "sticks",
        }.get(structure, structure_type)

    def define_multipliers(self):
        # base materials (base item / yields)
        self.sticks = 2 / 4

        # actual materials (yields / necessary base item)
        # all
        self.stairs = 6/4
        self.slabs = 2
        
        # wood
        self.planks = 1/4   
        self.fence = 4 + 2 * self.sticks
        self.fence_door = 2 + 4 * self.sticks
        self.door = 3 / 6
        self.pressure_plate = 1 / 2

        # other
        self.glass_pane = 16 / 6
        self.iron_bars = 16 / 6

        # special
        self.ladder = 3 / 7 * self.sticks
        self.cauldron = 1 / 7
