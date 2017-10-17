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
            spirit = Spirit(line['name'], line['stuffs'], line['up'], line['down'])
            spirits_list.append(spirit)
        spirits = Spirits(spirits_list)
        return spirits


"""
同種合体で作成される精霊を検索
"""
def same_fusion(name):
    categories = load_categories()
    target = categories.get_category(name)
    spirit_dict = {
        "アーシーズ": set(['妖樹', '魔獣', '地霊', '妖虫', '夜魔']),
        "エアロス": set(['天使', '妖魔', '凶鳥', '妖精', '悪霊']),
        "アクアンズ": set(['妖鳥', '妖獣', '妖鬼', '鬼女', '幽鬼']),
        "フレイミーズ": set(['天女', '龍王', '邪鬼', '堕天使', '邪龍']),
        "ノーム": set(['神樹', '死神', '地母神', '鬼神']),
        "シルフ": set(['霊鳥', '聖獣', '破壊神', '龍王']),
        "ウンディーネ": set(['女神', '邪神', '神獣', '幻魔']),
        "サラマンダー": set(['大天使', '魔神', '魔王', '国津神'])
    }
    if target:
        for key, value in spirit_dict.items():
            if name in value:
                return key
    return False


"""
精霊合体
"""
def spirit_fusion(name, spirit):
    pass


def main():
    spirits = load_spirits()
    categories = load_categories()
    result = spirits.get_up_by('魔獣')
    for category in categories.categories:
        up_list = spirits.get_up_by(category.name)
        if up_list:
            print("{:<4}{}".format(category.name, up_list))




if __name__ == '__main__':
    main()
