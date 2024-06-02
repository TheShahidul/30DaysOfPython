#practise

price = 1000000
good_credit = True

if good_credit:
    down_payment = 0.1 * price
    # print("put down 10%")
else:
    down_payment = 0.2 * price
print(f"Down Payment: ${down_payment}")

#------------------------------------
#logical operators
#if applicant has high income AND good credit Eligible for loan

has_high_income = True
has_good_credit = False #change to True

if has_high_income and has_good_credit:
    print("eligible for loan")

#if applicant has high income OR good credit Eligible for loan

has_high_income = False
has_good_credit = True #change to True

if has_high_income or has_good_credit:
    print("eligible for loan")

#AND: both are true / false
#OR: at least one is true / false
#NOT:


#if applicant has good credit AND doesn't have a criminal record

has_good_credit = True
has_criminal_record = False

if has_good_credit and not has_criminal_record: #false - false it becomes positive
    print("eligible for laon")

#comparative operators

temperature = 30
if temperature > 30:    # => <= == !=
    print("its a hot day")
else:
    print("its not a hot day")

#practise (name must be between 3 to 20 char long)

name = "shahidul islam  "
# name = "msi"
print("name lenght is", len(name))

if len(name) < 5:
    print("name must be at least 3 characters")
elif len(name) > 20:
    print("name must be maximum 20 char")
else:
    print("the name looks good")

#---------------------------end of day 4-------------------------
#----------------------date 2-june-2024--------------------------

