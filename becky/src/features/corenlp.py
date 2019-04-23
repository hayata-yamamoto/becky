import os
from pathlib import Path
from typing import Any, Dict, Optional

from stanfordcorenlp import StanfordCoreNLP


class CoreNLP:
    def __init__(self, corenlp_path: Optional[Path] = None) -> None:
        """
        Args:
            corenlp_path:
        """
        if corenlp_path is None:
            self.nlp = StanfordCoreNLP(os.getenv("CORENLP_HOME"))
        else:
            self.nlp = StanfordCoreNLP(str(corenlp_path))

    def parse_all(self, sentence: str) -> Dict[str, Any]:
        """
        parse sentence by CoreNLP all method
        Args:
            sentence:
        Returns:
        """
        results = {
            "corenlp_tokens": [],
            "corenlp_pos_tags": [],
            "corenlp_named_entity": [],
            "corenlp_constituency": "",
            "corenlp_dependency": [],
            "corenlp_coreference": [],
        }

        if sentence == "":
            return results

        results["corenlp_tokens"] = self.nlp.word_tokenize(sentence)
        results["corenlp_pos_tags"] = self.nlp.pos_tag(sentence)
        results["corenlp_named_entity"] = self.nlp.ner(sentence)
        results["corenlp_constituency"] = self.nlp.parse(sentence)
        results["corenlp_dependency"] = self.nlp.dependency_parse(sentence)
        results["corenlp_coreference"] = self.nlp.coref(sentence)
        return results
