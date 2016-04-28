def user_info():
  name = input("Enter your name player.")
  age =int(input("Enter your age " + name + " in mmddyyyy format."))
  age_limit = 12311998
  age_check = age - age_limit
  if age_check < 0:
    print "Great! " + name + " Let's Begin."
  else:
    print "No. You should have lied about your age... next time don't snitch on yourself!"
