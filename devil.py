from category import load_categories
import json



"""
悪魔情報クラス
"""
class Devil:
    def __init__(self, name, category, level):
        self.name = name
        self.category = category
        self.level = level


"""
悪魔情報操作クラス
"""


class Devils:
    def __init__(self, devils):
        self.devils = devils

    """
    悪魔名検索
    """
    def get_devil(self, name):
        for devil in self.devils:
            if devil.name == name:
                return devil
        return False


    """
    悪魔情報更新
    """
    def update(self):
        devils_list = self.devils
        with open('data/devil.json', mode='w', encoding='utf-8') as f:
            json.dump(devils_list, f, ensure_ascii=False, indent=4)


    """
    悪魔情報新規追加
    """
    def add_devil(self, name, category_name, level):
        devil_data = {}
        categories = load_categories()
        category = categories.get_category(category_name)
        category_id = category.ID
        devil_data['name'] = name
        devil_data['level'] = level
        if not self.devils.setdefault(category_id):
            self.devils[category_id] = []
        self.devils[category_id].append(devil_data)
        self.update()


"""
悪魔情報読み込み関数
"""


def load_devils():
    with open('data/devil.json', encoding='utf-8') as f:
        json_data = json.load(f)
        deviles_list = []
        for cat_id, data_list in json_data.items():
            if data_list:
                for data in data_list:
                    name = data['name']
                    level = data['level']
                    devil = Devil(name, int(cat_id), level)
                    deviles_list.append(devil)
        devils = Devils(deviles_list)
        return devils


def main():
    devils = load_devils()
    devils.add_devil('ハトホル', '女神', 18)


if __name__ == '__main__':
    main()
