def validate_email(email):
  if "@" in email and  "." in email:
    return True
  else: 
    raise ValueError("Invalid email address")
  
email = "fda@mail.com"

try:
  validate_email(email)
  print("Logged in successfully")
except ValueError as e:
  # print(e)
  print("Invalid email, try again")