import re

def extract_before(text, before_text):
    pattern = r'(.*?)(?=' + re.escape(before_text) + r')'
    match = re.search(pattern, text, re.DOTALL)
    if match:
        return match.group(1).strip()
    return None

def extract_after(text, after_text):
    pattern = r'(?<=' + re.escape(after_text) + r')(.*)'
    match = re.search(pattern, text, re.DOTALL)
    if match:
        return match.group(1).strip()
    return None

def extract_between(text, before, after):
    pattern = re.escape(before) + r'(.*?)' + re.escape(after)
    match = re.search(pattern, text, re.DOTALL)
    if match:
        return match.group(1)
    return None    

def extract_pattern_matches(text, pattern):
    return text

def modified(text):
    pattern = r'(?<!\.)\n'
    modified_text = re.sub(pattern, ' ', text)
    # modified_text = re.sub(r'\n+$', '', modified_text)
    return modified_text