from typing import ClassVar


class Results:
    # Tipos de madeira do Minecraft. Para esses, a cadeia de base vai até "logs".
    WOOD: ClassVar[set] = {
        "oak", "spruce", "birch", "jungle", "acacia",
        "dark oak", "crimson", "warped", "bamboo", "cherry", "mangrove",
    }

    # Para materiais não-madeira (pedra etc.), o material primário é o próprio
    # bloco. Multiplicadores de blocos por item (tipo -> blocos por item).
    SOLID_MULTIPLIERS: ClassVar[dict] = {
        "stair": 6 / 4,
        "slab": 1 / 2,
        "wall": 1,
    }

    def __init__(self):
        self.define_multipliers()

    # Multiplicador de cada tipo quando o material é MADEIRA.
    # Expresso em quantidade de material primário (logs) por item.
    def define_multipliers(self):
        self.planks = 1 / 4         
        self.sticks = 1 / 8         
        self.fence = 5 / 24         
        self.fence_door = 1         
        self.door = 1 / 2           
        self.pressure_plate = 1 / 2 
        self.stairs = 1 / 4         
        self.slabs = 1 / 4          
        self.glass_pane = 6 / 16    
        self.iron_bars = 6 / 16     
        self.ladder = 7 / 24        
        self.cauldron = 7           
        self.trapdoor = 3 / 4        # 6 planks -> 2 trapdoors => 1 trapdoor = 3 planks = 3/4 log

    def _is_wood(self, material: str) -> bool:
        return material.strip().lower() in self.WOOD

    @staticmethod
    def _norm(type_: str) -> str:
        return type_.strip().lower().rstrip("s")

    # ------------------------------------------------------------------
    # Material primário FINAL (usado na tabela de resultados).
    # ------------------------------------------------------------------

    # Retorna quantos materiais primários são necessários para fabricar 1 item.
    # Se material é madeira, converte para logs via receita. Se não é madeira,
    # o primário é o próprio bloco e usamos os multiplicadores de bloco.
    def get_structure_to_base_multiplier(self, structure_type: str, material: str = ""):
        structure = self._norm(structure_type)
        if not self._is_wood(material):
            if structure in self.SOLID_MULTIPLIERS:
                return self.SOLID_MULTIPLIERS[structure]
            return 1
        return {
            "plank": self.planks,
            "stair": self.stairs,
            "slab": self.slabs,
            "fence": self.fence,
            "fence door": self.fence_door,
            "fence gate": self.fence_door,
            "door": self.door,
            "pressure plate": self.pressure_plate,
            "glass pane": self.glass_pane,
            "iron bar": self.iron_bars,
            "ladder": self.ladder,
            "cauldron": self.cauldron,
            "trapdoor": self.trapdoor,
        }.get(structure, 1)

    # Retorna o NOME do material primário (ex: "logs", "glass", ou o próprio material).
    def get_base_name(self, structure_type: str, material: str = ""):
        structure = self._norm(structure_type)
        if not self._is_wood(material):
            return material.strip()
        return {
            "plank": "logs",
            "stair": "logs",
            "slab": "logs",
            "fence": "logs",
            "fence door": "logs",
            "fence gate": "logs",
            "door": "logs",
            "pressure plate": "logs",
            "ladder": "logs",
            "glass pane": "glass",
            "iron bar": "iron ingots",
            "cauldron": "iron ingots",
            "wall": "logs",
            "trapdoor": "logs",
        }.get(structure, structure_type.strip())

    # ------------------------------------------------------------------
    # Base item IMEDIATO (usado na tabela de itens / item requirements).
    # ------------------------------------------------------------------

    # Retorna o NOME do base item imediato. Para madeira usa a receita
    # (fence -> planks), para não-madeira é o próprio material (stone -> stone).
    def get_item_base_name(self, structure_type: str, material: str = ""):
        structure = self._norm(structure_type)
        if not self._is_wood(material):
            return material.strip()
        return {
            "plank": "logs",
            "stair": "planks",
            "slab": "planks",
            "fence": "planks",
            "fence door": "planks",
            "fence gate": "planks",
            "door": "planks",
            "pressure plate": "planks",
            "ladder": "sticks",
            "glass pane": "glass",
            "iron bar": "iron ingots",
            "cauldron": "iron ingots",
            "wall": "planks",
            "trapdoor": "planks",
        }.get(structure, structure_type.strip())

    # Retorna quantos base items IMEDIATOS são necessários para fabricar 1 item.
    def get_item_base_multiplier(self, structure_type: str, material: str = ""):
        structure = self._norm(structure_type)
        if not self._is_wood(material):
            if structure in self.SOLID_MULTIPLIERS:
                return self.SOLID_MULTIPLIERS[structure]
            return 1
        return {
            "plank": 1 / 4,          
            "stair": 1,              
            "slab": 1,               
            "fence": 5 / 6,          
            "fence door": 4,         
            "fence gate": 4,
            "door": 2,               
            "pressure plate": 2,     
            "ladder": 7 / 3,         
            "glass pane": 6 / 16,
            "iron bar": 6 / 16,
            "cauldron": 7,
            "wall": 1,
            "trapdoor": 3,
        }.get(structure, 1)
