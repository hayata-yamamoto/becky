import MeCab
from typing import Union


class MecabTokenizer:
    """
    This module is parsing sentence to several tokens.
    For example,
        >>> sentence = '私は、トムです。'
        >>> tokenizer = Tokenizer()
        >>> tokenizer.parse(sentence)
        ['私', 'は', '、', 'トム', 'です', '。']
    """

    def __init__(self, neologd=True):
        """
        Args:
            neologd (True) : mecab-ipadic-neologdを使うかどうか
        """
        if neologd:
            self.tagger = MeCab.Tagger(
                '-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')
        else:
            self.tagger = MeCab.Tagger('-Ochasen')
        self.tagger.parse('')

    def __get_morphemes(self, sentence: str):
        return self.tagger.parseToNode(sentence)

    def parse(self, sentence: str, condition: Union[None, list] = None) -> list:
        """
        文章を分かち書きして、返すメソッド
        infoをTrueにすると、品詞情報も返します。
        Args:
            sentence (str) : 文章
            condition (None or list): 取得したい品詞名
        Returns:
            list
        """

        # todo: 品詞情報のエラー処理を書く
        node = self.__get_morphemes(sentence)
        morphemes = []
        i = 0
        # todo: 再帰関数を使ってかける？
        while node.next:

            # 一行目に形態素は現れない
            if i == 0:
                i += 1
                node = node.next
                continue

            # 品詞情報のフィルターが不要な場合の処理
            # conditionにリストを渡すとここで上に戻る
            if condition is None:
                morphemes.append(node.surface)
                node = node.next
                continue

            # 品詞情報でフィルターをかけたい時
            parts = node.feature.split(',')[0]
            if parts in condition:
                morphemes.append(node.surface)
                node = node.next
                continue
            node = node.next
        return morphemes
