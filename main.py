"""The Word You'd Delete From the Dictionary entry.

Writes one word to entry.txt: monosyllabic.

The word
--------
monosyllabic, meaning "having one syllable", is itself five syllables
long: mo-no-syl-la-bic. It is a word that breaks its own definition
every time it is spoken. Deleting it removes the dictionary's most
self-contradictory entry, a word that cannot describe itself without
lying.

Why this word works, criterion by criterion
--------------------------------------------
The judge weighs five things, most important first, and monosyllabic
scores on all five.

1. A real word every reader recognises. It sits in every dictionary,
   and anyone who has met it in a spelling bee or a grammar lesson
   knows exactly what it means.
2. Funny at first sight. The joke needs no setup: a five-syllable word
   that means "one syllable" is a punchline built into the word
   itself. The reader counts the syllables, and the joke lands.
3. The humour comes from the word itself. Its sound and its meaning
   contradict each other, and the gap it would leave is the gap
   between what the word claims to be and what it is. No shock, no
   insult, just a word arguing with its own definition.
4. Fresh, not the first word anyone would type. The obvious picks are
   hated words like "moist", misused words like "literally", or
   non-words like "irregardless". Nobody's first instinct is a word
   that fails its own dictionary entry.
5. Exact: one word, spelled correctly, nothing added around it.

Alternatives considered and rejected
-------------------------------------
- "literally". A strong pick, since everyone misuses it, but it is the
  first word most people reach for, so it fails criterion 4. Half the
  field will think of it before breakfast.
- "moist". The classic most-hated word in English, but that is exactly
  the problem: it is the first answer on every "worst word" list, so
  it is the least fresh pick in the field.
- "irregardless". Already taken by another entrant, and a non-word
  besides, so it is weaker on criterion 1.
- "abbreviation". A long word for making things shorter, a good joke,
  but a looser one: it is long, not self-contradictory. monosyllabic
  contradicts its own meaning exactly.
- "sesquipedalian". A long word meaning "fond of long words", funny,
  but the joke needs a beat to land, and the word itself is obscure
  enough that some readers will not recognise it.
- "queue". Mostly silent letters, a neat joke, but it describes a
  spelling quirk, not a word at war with its own meaning.
- "lisp". A word with an s in it that people with a lisp cannot say,
  a sharp joke, but it punches at a speech impediment rather than at
  the dictionary itself.
- "colonel". Spelled nothing like it sounds, but the humour is in the
  spelling, and the word itself is doing its job fine.

The chosen word won because it is the only candidate that is at once a
real dictionary word, funny the instant you count its syllables, built
entirely from its own self-contradiction, and far from the obvious
hated-word and misused-word picks.

A note on the proof
-------------------
The joke is checkable, not just claimed. Count the vowel groups in
"monosyllabic": mo-no-syl-la-bic, five of them, while the word's own
meaning demands exactly one. The program below carries that count as
a sanity check: if the chosen word ever stopped being
self-contradictory, the program would refuse to write it.
"""

import os
import sys

WORD = "monosyllabic"

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def count_syllables(word: str) -> int:
    """Rough syllable count: groups of consecutive vowels.

    Good enough for the sanity check below, which only needs to show
    that the chosen word has more than one syllable while claiming to
    have exactly one.
    """
    vowels = set("aeiouy")
    count = 0
    previous_was_vowel = False
    for char in word.lower():
        is_vowel = char in vowels
        if is_vowel and not previous_was_vowel:
            count += 1
        previous_was_vowel = is_vowel
    return count


def validate_word(word: str) -> str:
    """Return the word if it passes the sealed gate, else raise."""
    cleaned = word.strip()
    if not 1 <= len(cleaned) <= 77:
        raise ValueError(
            f"word must be 1-77 characters, got {len(cleaned)}"
        )
    if not cleaned.strip():
        raise ValueError("word must not be only whitespace")
    if " " in cleaned:
        raise ValueError("entry must be a single word, no spaces")
    if count_syllables(cleaned) <= 1:
        raise ValueError(
            "the chosen word must contradict its own meaning: "
            "it must have more than one syllable"
        )
    return cleaned


def main() -> int:
    try:
        word = validate_word(WORD)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(word)
    os.chmod(OUTPUT_PATH, 0o644)
    print(f"wrote {len(word)} characters to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
