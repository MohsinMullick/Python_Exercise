"""17.	Create a list of five random items and
 remove the third item using the del statement.
  Print the updated list."""
items=['books','songs','fruits','glossary','phone number']
del items[2]
print(items)

"""18.	Make a list of five devices you own, 
use pop() to remove the last device,
 and print the removed device and the updated list."""
devices=['laptop','refrigerator','washing machine','tablet','vacuum cleaner']
devices.pop(-1)
print(devices)

"""19.	Create a list of five countries and 
use remove() to delete one country by name.
 Print the modified list."""
country_names=['bangladesh','usa','canada','england','australia']
country_names.remove("usa")
print(country_names)

"""20.	Make a list of four outdoor activities,
 pop the activity at index 1, and
 print a message about why you removed it."""
outdoor_activities=['hiking','running','golf','swimming']
remove_activity=outdoor_activities.pop(1)
print(f"i dont like {remove_activity} because im tried")
print(f"update activity:{outdoor_activities}")
