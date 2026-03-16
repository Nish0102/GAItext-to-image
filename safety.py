import re

# ---------------------------
# BLOCKED KEYWORDS
# ---------------------------

blocked_keywords = [

# NSFW / sexual
"nsfw","nude","naked","porn","pornography","erotic","sexual",
"sex","lingerie","bikini","topless","boobs","breasts",

# Violence
"gore","blood","murder","kill","stab","torture","corpse",
"behead","decapitate","execution","massacre","shooting",

# Self harm
"suicide","self harm","cutting","hang yourself","kill myself",

# Extremism
"nazi","hitler","terrorist","isis","extremist","bomb making",

# Drugs
"cocaine","heroin","meth","drug abuse",

# Abuse
"rape","molest","sexual assault","child abuse"
]

# ---------------------------
# RACIAL / HATE SPEECH
# (partial filter example)
# ---------------------------

hate_speech_patterns = [
r"\bnigg[a|er]\b",
r"\bfaggot\b",
r"\bretard\b"
]

# ---------------------------
# DANGEROUS ACTIVITY
# ---------------------------

dangerous_patterns = [
r"how to make a bomb",
r"how to kill",
r"how to poison",
r"how to commit suicide"
]

# ---------------------------
# MAIN SAFETY FUNCTION
# ---------------------------

def is_safe(prompt):

    prompt = prompt.lower()

    # Keyword blocking
    for word in blocked_keywords:
        if re.search(rf"\b{word}\b", prompt):
            return False

    # Hate speech
    for pattern in hate_speech_patterns:
        if re.search(pattern, prompt):
            return False

    # Dangerous activity
    for pattern in dangerous_patterns:
        if re.search(pattern, prompt):
            return False

    return True
