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
        devil_dict = {}
        categories = load_categories()
        for devil in self.devils:
            category_id = devil.category
            if category_id not in devil_dict.keys():
                devil_dict[category_id] = []
            devil_data = dict(name=devil.name, level=int(devil.level))
            devil_dict[category_id].append(devil_data)
            devil_dict[category_id] = sorted(devil_dict[category_id], key=lambda x:x['level']) # レベル順に並び替え

        # 保存前にカテゴリーID順に並び替え
        sort_key = sorted(devil_dict)
        sort_dict = {}
        for key in sort_key:
            sort_dict[key] = devil_dict[key]
        with open('data/devil.json', mode='w', encoding='utf-8') as f:
            json.dump(sort_dict, f, ensure_ascii=False, indent=4)


    """
    悪魔情報新規追加
    """
    def add_devil(self, name, category_name, level):
        categories = load_categories()
        category = categories.get_category(category_name)
        category_id = category.ID
        if not self.get_devil(name):
            devil = Devil(name, category_id, level)
            self.devils.append(devil)
            self.update()
            return True
        else:
            return False


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


if __name__ == '__main__':
    main()
