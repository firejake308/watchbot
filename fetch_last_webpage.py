from db import mydb
import json

def fetch_last_webpage():
  cursor = mydb.cursor(buffered=True)
  cursor.execute("SELECT WebsiteText FROM HTMLFile")
  rows = cursor.fetchall()
  result_string = ""

  # There should only be one. This is kinda hacky but oh well
  if rows is not None:
    for r in rows:
        result_string = result_string + r[0]
  else:
    raise Exception(f"Result string = {result_string}")

  # Close the cursor
  cursor.close()
  print(result_string)
  return json.loads(result_string)


def save_new_version(json_formatted):
    con = mydb.cursor()
    json_string = json.dumps(json_formatted)
    con.execute("UPDATE HTMLFile SET WebsiteText=%s WHERE ID=%s",  (json_string, 1))
    mydb.commit()
    con.close()




# for testing purposes
if __name__ == "__main__":
    print(fetch_last_webpage())