from category import load_categories


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


def main():
    result = same_fusion('フード')
    print(result)


if __name__ == '__main__':
    main()
