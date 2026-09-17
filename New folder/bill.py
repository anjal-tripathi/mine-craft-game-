print("==============================================================")
print()
print(" SMART CAMPUS UTILITY & ACCESS PASS GENERATOR")
print()
print("==============================================================")
print()

user = int(input(" Select User category ( 1:Student,2:Faculty/Staff ) "))

if user == 1:

    

    course = input("Enter Sub-Category(UG/PG) :")

    CGPA = float(input(" Enter Student CGPA(0.0-10.0): "))


    if CGPA < 0.0 or CGPA > 10.0:
        print("[ERROR]: CGPA must be between 0.0 and 10.0")
        exit()

    Parking_vehicle = input(
        " Select parking Permit(0:None, 2:Two Wheeler, 4:Four Wheeler) "
    )

    if course == "UG":
        Base_Access_Pass_Fess = 500

    elif course == "PG":
        Base_Access_Pass_Fess = 350

    else:
        print("Wrong Input")
        exit()

  
    if CGPA >= 8.5 and CGPA <= 10.0:
        Merit_Discount = Base_Access_Pass_Fess * 0.20
        Base_Access_Pass_Fess = Base_Access_Pass_Fess - Merit_Discount

    elif CGPA >= 7.5 and CGPA <= 8.49:
        Merit_Discount = Base_Access_Pass_Fess * 0.10
        Base_Access_Pass_Fess = Base_Access_Pass_Fess - Merit_Discount

    else:
        Merit_Discount = 0


    Parking_Fee = 0
    Peak_Surcharge = 0

    if Parking_vehicle == "2":
        Parking_Fee = 200

    elif Parking_vehicle == "4":
        Parking_Fee = 600
        Peak_Surcharge = 150

    elif Parking_vehicle == "0":
        Parking_Fee = 0

    else:
        print("Wrong Input")
        exit()

    Base_Access_Pass_Fess = Base_Access_Pass_Fess + Parking_Fee + Peak_Surcharge


elif user == 2:

    Resident_Type = input(
        " enter your resident type \n 1: Resident Faculty | 2: Guest Faculty "
    )

    Years_of_service = int(input(" enter your years of service "))

  
    if Years_of_service < 0:
        print("[ERROR]: Years of Service cannot be negative")
        exit()

    Parking_Vehicle = input( " Select parking Permit(0:none, 2:Two Wheeler, 4:Four Wheeler) ")
    if Resident_Type == "1":
        Base_Access_Pass_Fess = 800

    elif Resident_Type == "2":
        Base_Access_Pass_Fess = 1200

    else:
        print("Wrong Input")
        exit()

  
    if Years_of_service > 10:
        Service_Discount = Base_Access_Pass_Fess * 0.15
        Base_Access_Pass_Fess = Base_Access_Pass_Fess - Service_Discount

    else:
        Service_Discount = 0

  
    Parking_Fee = 0

    if Parking_Vehicle == "1":
        Parking_Fee = 200

    elif Parking_Vehicle == "2":
        Parking_Fee = 600

    elif Parking_Vehicle == "0":
        Parking_Fee = 0

    else:
        print("Wrong Input")
        exit()

    Base_Access_Pass_Fess = Base_Access_Pass_Fess + Parking_Fee

    Peak_Surcharge = 0


else:
    print("Wrong Input")
    exit()

electricity_unit = int(input(" Enter Monthly Electricity  Consumption: "))

if electricity_unit < 0:
    print("[ERROR]: Electricity units cannot be negative")
    exit()


if electricity_unit <= 100:

    electricity_bill = electricity_unit * 3
    fixed_charge = 50

elif electricity_unit <= 300:

    electricity_bill = (100 * 3) + ((electricity_unit - 100) * 5)
    fixed_charge = 100

elif electricity_unit <= 500:

    electricity_bill = (100 * 3) + (200 * 5) + ((electricity_unit - 300) * 7.5)
    fixed_charge = 150

else:

    electricity_bill = (100 * 3) + (200 * 5) + (200 * 7.5) + ((electricity_unit - 500) * 10)
    fixed_charge = 250


electricity_bill = electricity_bill + fixed_charge


Final_Bill = Base_Access_Pass_Fess + electricity_bill


print()
print("----------------------------------------------------------------")
print("              CALCULATED INVOICE BREAKDOWN")
print("----------------------------------------------------------------")

print("Access Pass + Parking Total : ₹", format(Base_Access_Pass_Fess, ".2f"))
print("Electricity Bill            : ₹", format(electricity_bill, ".2f"))
print("Fixed Service Charge        : ₹", format(fixed_charge, ".2f"))

print("----------------------------------------------------------------")
print("TOTAL MONTHLY PAYABLE       : ₹", format(Final_Bill, ".2f"))
print("----------------------------------------------------------------")