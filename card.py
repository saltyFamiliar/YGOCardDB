from typing import Dict, Tuple, List

Limit_Type_Dict: Dict[str, int] = {
    "Standard": 0,
    "Semi-Limited": 1,
    "Limited": 2,
    "Banned": 3,
}

Formats = ["ocg", "tcg", "goat"]


class Card:
    def __init__(self, card_data: dict):
        keys = card_data.keys()

        self.id: int = card_data['id']
        self.name = card_data['name']
        self.type = card_data['type'] if 'type' in keys else None
        self.frameType = card_data['frameType'] if 'frameType' in keys else None
        self.desc = card_data['desc'] if 'desc' in keys else None
        self.race = card_data['race'] if 'race' in keys else None
        self.archetype = card_data['archetype'] if 'archetype' in keys else None
        self.card_sets = card_data['card_sets'] if 'card_sets' in keys else None
        self.card_images = card_data['card_images'] if 'card_images' in keys else None
        self.card_prices = card_data['card_prices'] if 'card_prices' in keys else None
        self.atk = card_data['atk'] if 'atk' in keys else None
        self.def_ = card_data['def'] if 'def' in keys else None
        self.level = card_data['level'] if 'level' in keys else None
        self.attribute = card_data['attribute'] if 'attribute' in keys else None
        self.pend_desc = card_data['pend_desc'] if 'pend_desc' in keys else None
        self.monster_desc = card_data['monster_desc'] if 'monster_desc' in keys else None
        self.scale = card_data['scale'] if 'scale' in keys else None
        self.linkval = card_data['linkval'] if 'linkval' in keys else None
        self.linkmarkers = card_data['linkmarkers'] if 'linkmarkers' in keys else None
        self.banlist_info = card_data['banlist_info'] if 'banlist_info' in keys else None

        self.limits: Dict[str, str] = {}
        banlist_entries = self.banlist_info.keys() if self.banlist_info else {}
        for format_name in Formats:
            banlist_name = f"ban_{format_name}"
            if banlist_name not in banlist_entries:
                self.limits[format_name] = "Standard"
            else:
                self.limits[format_name] = self.banlist_info[banlist_name]

    def get_limit_table_entries(self) -> List[Tuple[int, int, int]]:
        """
        returns an array of entries into the LIMIT table for the card. Every card has a limit for every format
        :return: [(CARD_ID, FORMAT_ID, LIMIT_TYPE_ID), (CARD_ID, FORMAT_ID, LIMIT_TYPE_ID), (CARD_ID, FORMAT_ID, LIMIT_TYPE_ID)]
        """
        result = []
        for format_id, format_name in enumerate(Formats):
            result.append((self.id, format_id, Limit_Type_Dict[self.limits[format_name]]))
        return result
