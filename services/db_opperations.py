# Function to insert data into mongo db

# pull creds

#
# def insert():
#     try:
#     employeeId = raw_input('Enter Employee id :')
#     employeeName = raw_input('Enter Name :')
#     employeeAge = raw_input('Enter age :')
#     employeeCountry = raw_input('Enter Country :')
#
#     except Exception, e:
#         print str(e)
#
# # Read Records
# def read():
#     try:
#     users = db.users.find({})
#     print '\n All data from EmployeeData Database \n'
#     for emp in empCol:
#         print emp
#
#     except Exception, e:
#         print str(e)
#
# # Update Records
# def update():
#     try:
#     criteria = raw_input('\nEnter id to update\n')
#     name = raw_input('\nEnter name to update\n')
#     age = raw_input('\nEnter age to update\n')
#     country = raw_input('\nEnter country to update\n')
#
#     db.Employees.update_one(
#         {"id": criteria},
#         {
#         "$set": {
#             "name":name,
#             "age":age,
#             "country":country
#         }
#         }
#     )
#     print "\nRecords updated successfully\n"
#
#     except Exception, e:
#     print str(e)
#
# # Delete User
# def delete_users():
#     try:
#     criteria = raw_input('\nEnter employee id to delete\n')
#         db.Employees.delete_many({"id":criteria})
#     print '\nDeletion successful\n'
#     except Exception, e:
#     print str(e)
