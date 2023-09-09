#Create a module named mymodule1.py. Add attributes myage set to your current age, and year set to the current year. Create another module named mymodule2.py.
# Add attributes myage set to 0, and year set to the year you were born.
# Now create a file named namespace_test.py. Import both of the modules above and write the following statement:

import mymodule1
import mymodule2

print( (mymodule2.myage - mymodule1.myage) == (mymodule2.year - mymodule1.year)  )

#Even though there are variables with the same name, there is no problem as they are drawn from which modules.