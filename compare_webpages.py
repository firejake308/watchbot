import difflib as dl
from DiffLibParser import DifflibParser

RIGHT_ONLY = 2
def compare_webpages(list_string1, list_string2):
    diff = DifflibParser(list_string1,list_string2)

    # We only care about additions in the new file at this point
    striped_lines = [d["line"] for d in diff if d["code"] > 0]#RIGHT_ONLY]
    changes = "\n".join(striped_lines)


    return changes






