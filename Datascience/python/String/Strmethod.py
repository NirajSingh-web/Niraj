def StringMethod():
  msg='hello,baby,b'
  print(msg[0:4].upper())
  print(msg.upper())
  print(msg.join(''))
  print(msg.replace("baby","sona"))
  print(msg.index("h"))
  print(msg.find("b"))
  print(msg.capitalize())
  print(msg.count("b"))
  print(msg.endswith("b"))
  print(msg.startswith("h"))
  
StringMethod()