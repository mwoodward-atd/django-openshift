from .models import Word

VOWELS = ('a', 'e', 'i', 'o', 'u', )


def generate_insult():
    short_adjective = Word.objects.filter(word_type='shortadj').order_by('?')[0].word
    long_adjective = Word.objects.filter(word_type='longadj').order_by('?')[0].word
    noun = Word.objects.filter(word_type='noun').order_by('?')[0].word
    article = 'an' if noun[0].lower() in VOWELS else 'a'

    return 'Thou art {} {} {} {}!'.format(article, short_adjective, long_adjective, noun)
