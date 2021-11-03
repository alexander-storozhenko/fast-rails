import sys

user_name = sys.argv[0]

config_path = '/etc/postgresql/9.5/main/pg_hba.conf'
line = '----------------------------------'

def _insert_allowed():
  global config_path, line, user_name

  with open(config_path, "r") as f:
    file_content = f.readlines()
  
  index = file_content.find(line) + len(line)

  file_content.insert(index, f"\n host  all     {user_name}    127.0.0.1/32      trust")
  file_content.insert(index, f"\n host  all     {user_name}    ::1/128      trust")

def allow_hosts():
  _insert_allowed()


if __name__ == "__main__":
  allow_hosts()
  
  
  