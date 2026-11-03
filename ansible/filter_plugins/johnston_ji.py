import os
import random
import re
from jinja2 import Environment, FileSystemLoader

PRIMES_31 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

NOTE_PATTERN = re.compile(
    r"^([A-G])(#+|b+)?(7+|L+)?(\^+?|v+?)??(3+?|e+?)??"
    r"((?:v17)+|(?:17)+)?((?:v19)+|(?:19)+)?((?:v23)+|(?:23)+)?"
    r"((?:v29)+|(?:29)+)?((?:v31)+|(?:31)+)?(\++|-+)?$"
)


def _parse_ratio(value):
    s = str(value).strip()
    if "/" in s:
        parts = s.split("/", 1)
    else:
        parts = s.split(None, 1)
    return int(parts[0]), int(parts[1])


def jinja2_johnston(ratio_str):
    """Render the 31-limit Ben Johnston note name using pure Jinja2 template logic."""
    x, y = _parse_ratio(ratio_str)
    templates_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "templates")
    env = Environment(loader=FileSystemLoader(templates_dir), autoescape=False)
    template = env.get_template("jinja2_johnston.j2")
    return template.render(numerator=x, denominator=y).strip()


def invert_ratio(ratio_str):
    """Flip a ratio 'x/y' into 'y/x'."""
    x, y = _parse_ratio(ratio_str)
    return f"{y}/{x}"


def smooth_31_ratio(seed):
    """Generate a 31-limit smooth ratio 'x/y' from a seed value."""
    rng = random.Random(seed)
    num = 1
    den = 1
    chosen = rng.sample(PRIMES_31, k=rng.randint(2, 5))
    has_11_without_13 = (11 in chosen) and (13 not in chosen)
    for p in chosen:
        if p >= 17 and has_11_without_13:
            exp = rng.choice([-2, 2])
        else:
            exp = rng.choice([-2, -1, 1, 2])
        if exp > 0:
            num *= p ** exp
        else:
            den *= p ** (-exp)
    return f"{num}/{den}"


def _signed_count(token, pos_sym, neg_sym):
    if not token:
        return 0
    if token.startswith(neg_sym):
        return -(len(token) // len(neg_sym))
    return len(token) // len(pos_sym)


def prime_accidental_vector(note_output):
    """
    Extract the signed prime-limit accidental vector
    [n7, n11, n13, n17, n19, n23, n29, n31] from a formatted Johnston note name.
    """
    first_line = str(note_output).splitlines()[0].strip()
    m = NOTE_PATTERN.match(first_line)
    if not m:
        raise ValueError(f"Unparseable Johnston note name: {first_line!r}")

    _, _, g7, g11, g13, g17, g19, g23, g29, g31, _ = m.groups()
    return [
        _signed_count(g7, "7", "L"),
        _signed_count(g11, "^", "v"),
        _signed_count(g13, "3", "e"),
        _signed_count(g17, "17", "v17"),
        _signed_count(g19, "19", "v19"),
        _signed_count(g23, "23", "v23"),
        _signed_count(g29, "29", "v29"),
        _signed_count(g31, "31", "v31"),
    ]


class FilterModule(object):
    def filters(self):
        return {
            "jinja2_johnston": jinja2_johnston,
            "invert_ratio": invert_ratio,
            "smooth_31_ratio": smooth_31_ratio,
            "prime_accidental_vector": prime_accidental_vector,
        }
