from nltk.tokenize import TweetTokenizer

class Analyzer():
    """Implements sentiment analysis."""

    def __init__(self, positives, negatives):
        """Initialize Analyzer."""
        self.tokenizer = TweetTokenizer(preserve_case=False, reduce_len=True, strip_handles=True)
        self.positive = set()
        self.negative = set()

        with open(positives, "r") as p:
            for line in p:
                if line[0].isalpha():
                    self.positive.add(line.rstrip('\n'))

        with open(negatives, "r") as neg:
            for line in neg:
                if line[0].isalpha():
                    self.negative.add(line.rstrip('\n'))

    def analyze(self, text):
        """Analyze text for sentiment, returning its score."""
        tokens = self.tokenizer.tokenize(text)
        score = 0
        for txt in tokens:
            if txt.lower() in self.positive:
                score = score + 1
            elif txt.lower() in self.negative:
                score = score - 1

        return score
