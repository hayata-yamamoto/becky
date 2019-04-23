from typing import Dict, List, Union

import stanfordnlp


class StanfordNLP:
    """
    stanfordnlpを使って文章を解析するクラス
    """

    def __init__(self) -> None:
        self.nlp = stanfordnlp.Pipeline()

    def analyze(self, sentence: str) -> Dict[str, List[Union[int, str]]]:
        """
        Args:
            sentence: target sentence.
        Returns:
            dict: {
                'index': token index of sentence,
                'text': token,
                'lemma': origin of token,
                'treebank_pos': https://www.sketchengine.eu/penn-treebank-tagset/
                'universal_pos': https://universaldependencies.org/u/pos/
                'morphological_relation': https://universaldependencies.org/u/feat/index.html
                'dependency_relation': dependency relation name ex.) discourse, compound, root etc...
                'governor': Describes the governor (regent/head) of the dependency relation.
            }
        """

        result: Dict = {
            "index": [],
            "text": [],
            "lemma": [],
            "treebank_pos": [],
            "universal_pos": [],
            "morphological_feature": [],
            "dependency_relation": [],
            "governor": [],
        }

        if not sentence:
            return result

        for word in self.nlp(sentence).sentences[0].words:
            result["index"].append(word.index)
            result["text"].append(word.text)
            result["lemma"].append(word.lemma)
            result["treebank_pos"].append(word.xpos)
            result["universal_pos"].append(word.upos)
            result["morphological_feature"].append(word.feats)
            result["dependency_relation"].append(word.dependency_relation)
            result["governor"].append(word.governor)

        return result
