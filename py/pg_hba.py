from optparse import OptionParser
from glob import glob


parser = OptionParser()
parser.add_option("--usr", dest="user_name")

(options, args) = parser.parse_args()

user_name = options.user_name
pg_version = glob("/etc/postgresql/*/")[0].split('/')[0]

config_path = f"/etc/postgresql/{pg_version}/main/pg_hba.conf"
line = '----------------------------------'

def _insert_allowed():
  global config_path, line, user_name

  with open(config_path, "r") as f:
    file_content = f.readlines()
  
  index = file_content.find(line) + len(line)

  file_content.insert(index, f"\n host  all     {user_name}    127.0.0.1/32      trust")
  file_content.insert(index, f"\n host  all     {user_name}    ::1/128      trust")

  with open(config_path, "w") as f:
    f.write(file_content)

def allow_hosts():
  _insert_allowed()


if __name__ == "__main__":
  allow_hosts()