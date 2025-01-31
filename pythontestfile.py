import inspect, re

cat = {"name":"cat", "balance":"$200", "key":"111"}
car = {"name":"car", "balance":"$200", "key":"222"}
kat = {"name":"kat", "balance":"$200", "key":"333"}
accountsdir = [cat, car, kat]

def varname(p):
  for line in inspect.getframeinfo(inspect.currentframe().f_back)[3]:
    m = re.search(r'\bvarname\s*\(\s*([A-Za-z_][A-Za-z0-9_]*)\s*\)', line)
    if m:
      return m.group(1)
  
while 1 :
    
    func = input("check balance(c) or create new account(n) : ")
    
    if func == "c":
        username = input("username : ")
        password = input("password : ")
        if username == accountsdir[username]:
            user = username
            if password == user["key"]:
                print("name : " , varname(user), "balance : ", user["balance"])
    else : 
        print("function not found")
    