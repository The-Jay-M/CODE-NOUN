angle_degree = input("Please enter an angle in degrees: ")
angle_degree = int(angle_degree)
angle_minutes = input("Please enter an angle in minutes: ")
angle_minutes = int(angle_minutes)
angle_seconds = input("Please enter an angle in seconds: ")
angle_seconds = int(angle_seconds)
angle_decimal = angle_degree + (angle_minutes / 60) + (angle_seconds / 3600)
angle_decimal = round(angle_decimal, 3)
print(angle_decimal)

# Formatting
print(str(angle_degree)
      + chr(176)
      + str(angle_minutes)
      + chr(39)
      + str(angle_seconds)
      + chr(34), "is equal to",
      str(angle_decimal)
      + chr(176)
      + chr(46))
