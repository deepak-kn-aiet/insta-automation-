from dataclasses import dataclass


@dataclass
class KeywordRule:
    keyword: str
    response: str
    enabled: bool = True


DEFAULT_RULES = [
    KeywordRule(keyword="hello", response="Hi! Thanks for reaching out."),
    KeywordRule(keyword="price", response="Please check our pricing details in the link below."),
    KeywordRule(keyword="help", response="How can I assist you today?"),
]

# TODO: Move rules to the database and allow admin editing.
