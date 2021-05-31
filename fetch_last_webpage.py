from db import mydb

def fetch_last_webpage():
  con = mydb.cursor()
  res = con.execute("SELECT * FROM HTMLFile")
  result_string = ""

  # There should only be one. This is kinda hacky but oh well
  if res is not None:
    for r in res:
        result_string = result_string + r

  return result_string

# for testing purposes
if __name__ == "__main__":
    print(fetch_last_webpage())