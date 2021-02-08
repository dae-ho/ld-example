import sys

import ldclient 
from ldclient.config import Config

if __name__ == "__main__":
  ldclient.set_config(Config("sdk-07fa2cd7-147e-48a0-925c-dba94535446f"))

  user = {
  "key": "UNIQUE IDENTIFIER",
  "firstName": "Bob",
  "lastName": "Loblaw",
  "custom": {
    "groups": "beta_testers"
  }
}

show_feature = ldclient.get().variation("hello-feature", user, False)

if show_feature:
  print("Showing your feature")
else:
  print("Not showing your feature")

ldclient.get().close()

