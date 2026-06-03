def is_username_available(new_username, existing_usernames):
  existing_usernames_in_set=set(existing_usernames)
  if new_username in existing_usernames_in_set:
    print("Sorry the username is already existing")
    return False
  else:
    print("You can use the username")
    print(new_username)
    return True
  
  existing_usernames=["CodeMaster","PythonNinja","AIExplorer","TechWizard","BugHunter","CodeMaster","PixelCoder","DataDreamer","LogicBuilder","CyberKnight","PythonNinja","FutureDev","ByteCrafter","CodeRunner","SmartThinker"]
  new_username=input("Enter username:")
  is_username_available(new_username,existing_usernames)