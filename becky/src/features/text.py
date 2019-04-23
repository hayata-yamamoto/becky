from nltk import ngrams


def make_ngram(tokens: list, n: int =1) -> list:
    """
    分かち書きされた文章をngramして返す。
    Args:
        tokens (list) : 分かち書きされた文章
        n (int) : ngramのn
    Returns:
    """
    return [token[0] for token in ngrams(tokens, n=n)]
