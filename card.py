class Card:
    def __init__(self, card_data: dict):
        keys = card_data.keys()

        self.id = card_data['id'] if 'id' in keys else None
        self.name = card_data['name'] if 'name' in keys else None
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