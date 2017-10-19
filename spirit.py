from category import load_categories
import json


"""
精霊情報クラス
"""


class Spirit:
    def __init__(self, name, stuffs, up, down):
        self.name = name
        self.stuffs = stuffs
        self.up = up
        self.down = down


"""
精霊情報操作クラス
"""


class Spirits:
    def __init__(self, spirits):
        self.spirits = spirits

    def get_spirit(self, name):
        for spirit in self.spirits:
            if spirit.name == name:
                return spirit

    """
    種族名からランクアップする精霊を取得
    """

    def get_up_by(self, category_name):
        up_list = []
        for spirit in self.spirits:
            if category_name in set(spirit.up):
                up_list.append(spirit.name)
        return up_list


"""
精霊情報読み込み
"""


def load_spirits():
    spirits_list = []
    with open('data/spirit.json', encoding='utf-8') as f:
        json_data = json.load(f)
        for line in json_data:
            spirit = Spirit(line['name'], line['stuffs'],
                            line['up'], line['down'])
            spirits_list.append(spirit)
        spirits = Spirits(spirits_list)
        return spirits


"""
精霊合体
"""


def spirit_fusion(name, spirit):
    pass
