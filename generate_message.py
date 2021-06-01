

def generate_message(diff_string,website_name):
    message_string = """
     A difference has been detected in the %s website. Please
     refer to the website for further information. A full unedited description of the change can be seen below.

     ****************************Change Log********************************
     %s
     **********************************************************************
    """ % (website_name,diff_string)
    return message_string
