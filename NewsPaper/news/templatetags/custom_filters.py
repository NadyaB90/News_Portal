from django import template

register = template.Library()

CENSORED = ["плохоеслово1", "плохоеслово2", "плохоеслово3", "плохоеслово4", "плохоеслово5"]


@register.filter(name='censor')
def censor(value):
    text = value.split()
    for word in text:
        if word.lower() in CENSORED:
            value = value.replace(word[1:], "*" * len(word))
    return value
