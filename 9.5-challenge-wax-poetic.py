import random

# We're writing a script to write a poem from a random selection of words.

def make_poem():

    noun_pool = ["fossil", "horse", "aardvark", "judge", "chef", "mango", "cowboy", "gorilla", "helicopter", "robot", "storm trooper", "jedi"]
    verb_pool = ["kicks", "jingles", "bounces", "slurps", "meows", "explodes", "curdles", "skateboards", "games", "guesses", "prays", "picks"]
    adjective_pool = ["furry", "balding", "incredulous", "fragrant", "exuberant", "glistening", "purple", "high", "good", "new", "first", "last"]
    preposition_pool = ["against", "after", "into", "beneath", "upon", "for", "in", "like", "over", "within", "of", "with", "during"]
    adverb_pool = ["curiously", "extravagantly", "tantalizingly", "furiously", "sensuously", "quietly", "happily"]

    nouns = []
    verbs = []
    adjectives = []
    prepositions = []

    # Select the words we need for our poem.

    while len(nouns) < 3:
        selected_noun = random.choice(noun_pool)
        while selected_noun in nouns:
            selected_noun = random.choice(noun_pool)
            continue
        nouns.append(selected_noun)

    while len(verbs) < 3:
        selected_verb = random.choice(verb_pool)
        while selected_verb in verbs:
            selected_verb = random.choice(verb_pool)
            continue
        verbs.append(selected_verb)

    while len(adjectives) < 3:
        selected_adjective = random.choice(adjective_pool)
        while selected_adjective in adjectives:
            selected_adjective = random.choice(adjective_pool)
            continue
        adjectives.append(selected_adjective)

    while len(prepositions) < 2:
        selected_preposition = random.choice(preposition_pool)
        while selected_preposition in prepositions:
            selected_preposition = random.choice(preposition_pool)
            continue
        prepositions.append(selected_preposition)

    # We only need one adverb, so we'll just randomly select when we build the poem.

    # Set the first word (a/an) correctly.
    vowels = ["a", "e", "i", "o", "u"]
    if adjectives[0][0] in vowels:
        first_word = "An"
    else:
        first_word = "A"
    # Set the second instance of a/an correctly.
    if adjectives[2][0] in vowels:
        second_word = "an"
    else:
        second_word = "a"

    poem = f"""{first_word} {adjectives[0]} {nouns[0]}
        {first_word} {adjectives[0]} {nouns[0]} {verbs[0]} {prepositions[0]} the {adjectives[1]} {nouns[1]}
        {random.choice(adverb_pool)}, the {nouns[0]} {verbs[1]}
        the {nouns[1]} {verbs[2]} {prepositions[1]} {second_word} {adjectives[2]} {nouns[2]}"""

    return poem

print(make_poem())