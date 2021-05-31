from db import mydb
import json

def fetch_last_webpage():
  con = mydb.cursor()
  res = con.execute("SELECT * FROM HTMLFile")
  result_string = ""

  # There should only be one. This is kinda hacky but oh well
  if res is not None:
    for r in res:
        result_string = result_string + r

  # Close the connection
  con.close()
  return json.loads(result_string)


def save_new_version(json_formatted):
    con = mydb.cursor()
    json_string = json.dumps(json_formatted)
    res = con.execute("UPDATE HTMLFile SET WebsiteText=%s WHERE ID=1" % (json_string))
    con.close()




# for testing purposes
if __name__ == "__main__":
    print(fetch_last_webpage())