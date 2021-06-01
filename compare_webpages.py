import difflib as dl


def compare_webpages(list_string1, list_string2):
    website_comparison = ""
    for line in dl.context_diff(list_string1,list_string2):
       website_comparison = website_comparison + line
    if website_comparison == "":
        website_comparison = None

    return website_comparison






