
truncate_size = 1000
def generate_message(diff_string,website_name):
    message_string = """
     A change has been detected in the %s website. Please refer to the website for further information. A truncated description of the change can be seen below.

     ****************************Change Log********************************
     %s
     **********************************************************************
    """ % (website_name,diff_string[0:truncate_size])
    return message_string
