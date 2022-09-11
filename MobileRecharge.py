
def getMethod(method):
    if(method == '1'):
        return "Credit Card"
    elif method == '2':
        return "Debit Card"
    elif method == '3':
        return "upi"
    elif method == '4':
        return "Net Banking"
    elif method == '5':
        return "cash"

def display(pack):
    print("\n*************your bill invoice*************")
    print("Customer Name : " + str(name))
    print("Customer Phone Number: " + phone)
    if (type == 1):
        print("Recahreg of amount ", AmountToPay)
        if (pack == 1):
            print("Your pack is of Full recharge ")
        elif pack == 2:
            print("Your pack is of Talktime only ")
        elif pack == 3:
            print("Your pack is of Data Packs ")

        print("Plan : Prepaid")
        print("Payment Method is " + getMethod(method))
    elif (type == 2):
        print("Plan : PostPaid")
        print("Payment Method is " + getMethod(method))

# def display(type):
#     print("\n*************your bill invoice*************")
#     print("Customer Name : " + str(name))
#     print("Customer Phone Number: " + phone)
#     if (type == 2):
#         print("Plan : PostPaid")
#         print("Payment Method is " + getMethod(method))



recharge = {1: 'Prepaid', 2: 'Postpaid'}

Prepaid = {1: 'Full recharge', 2: 'Talktime only', 3: 'Data packs'}  # Storing the types of recharge

Payment_Method = {'1': 'Credit card', '2': 'Debit card', '3': 'UPI', '4': 'NetBanking',
                  '5': 'Cash'}  # Storing the method of transaction


Circles = {"1": "Andhra Pradesh & Telangana", "2": "Assam", "3": "Bihar & Jharkhand", "4": "Delhi",
                    "5": "Gujrat", "6": "Himachal Pradesh", "7": "Haryana",
                    "8": "Jammu and Kashmir", "9": "Kerela and Lakshadweep", "10": "Karnataka", "11": "Kolkata",
                    "12": "Maharashtra and Goa",
                    "13": "Madhya Pradesh and Chhattisgarh", "14": "Mumbai", "15": "North East", "16": "Orissa",
                    "17": "Punjab", "18": "Rajasthan", "19": "Tamil Nadu", "20": "UP (East)",
                    "21": "UP (West)", "22": "West Bengal", "23": "Ghaziabad and Noida"}

name = input("Enter the name of the customer: ") # Split function is used to remove empty white spaces from both ends.
phone = input("Enter the phone number: ")

if phone.isnumeric() and len(phone) == 10:
    # print("The phone number is valid")
    circle = input("Enter the circle ID. Choose from: \n1.Andhra Pradesh & Telangana\n2.Assam\n3.Bihar & Jharkhand"
                   "\n4.Delhi\n5.Gujrat\n6.Himachal Pradesh\n7.Haryana\n8.Jammu and Kashmir\n9.Kerela and Lakshadweep\n"
                   "10.Karnataka\n11.Kolkata\n12.Maharashtra and Goa\n13.Madhya Pradesh and Chhattisgarh\n14.Mumbai"
                   "\n15.North East\n16.Orissa\n17.Punjab\n18.Rajasthan\n19.Tamil Nadu\n20.UP (East)\n21.UP (West)"
                   "\n22.West Bengal\n23.Ghaziabad and Noida\n")
    # Input for circle ID from list of values is taken
    # The code block is executed only if the circle ID is a valid ID.
    if circle in Circles:
        type = int(input("Enter the type of  recharge 1. Prepaid 2.PostPaid: "))
        if type == 1 and type in recharge:
            pack = int(input(
                "Enter the type of recharge. Choose the 2 letter code from the following:\n1.Full Recharge \n2.Talk Time\n3.Data Pack\n "))
            if pack == 1 and pack in Prepaid :
                amount = int(input(
                    "Enter the amount for Full recharge. Choose between values 1 to 5:"
                    "\n1. Rs. 250 - Unlimited calls(local/national) + 1.5GB data/day + 100 SMS/ day. Val = 28 days\n"
                    "2. Rs. 400 - Unlimited calls(local/national) + 3 GB data/day + 100 SMS/ day. Val = 28 days\n"
                    "3. Rs.450 - Unlimited calls(local/national) + 1.5GB data/day + 100 SMS/ day. Val = 56 days\n"
                    "4. Rs.500 - Unlimited calls(local/national) + 1.5GB data/day + 100 SMS/ day. Val = 70 days\n"
                    "5. Rs.550 - Unlimited calls(local/national) + 1.5GB data/day + 100 SMS/ day. Val = 77days\n"))
                if amount == 1 :
                    AmountToPay = 250
                    print("The amount to be paid is Rs. 250")
                    method = input(
                        "Enter the Enter the method of payment from the following. Choose from \n1.Credit Card\n2.Debit Card\n3.UPI\n"
                        "4.Net Banking\n5.Cash\n")
                    print("Please pay Rs.250 using your " + getMethod(method))
                if amount == 2 :
                    AmountToPay = 400
                    print("The amount to be paid is Rs. 400")
                    method = input(
                        "Enter the Enter the method of payment from the following. Choose from \n1.Credit Card\n2.Debit Card\n3.UPI\n"
                        "4.Net Banking\n5.Cash\n")
                    print("Please pay Rs.400 using your " + getMethod(method))
                if amount == 3 :
                    AmountToPay = 450
                    print("The amount to be paid is Rs. 450")
                    method = input(
                        "Enter the Enter the method of payment from the following. Choose from \n1.Credit Card\n2.Debit Card\n3.UPI\n"
                        "4.Net Banking\n5.Cash\n")
                    print("Please pay Rs.450 using your " + getMethod(method))
                if amount == 4 :
                    AmountToPay = 500
                    print("The amount to be paid is Rs. 500")
                    method = input(
                        "Enter the Enter the method of payment from the following. Choose from \n1.Credit Card\n2.Debit Card\n3.UPI\n"
                        "4.Net Banking\n5.Cash\n")
                    print("Please pay Rs.500 using your " + getMethod(method))
                if amount == 5 :
                    AmountToPay = 550
                    print("The amount to be paid is Rs. 550")
                    method = input(
                        "Enter the Enter the method of payment from the following. Choose from \n1.Credit Card\n2.Debit Card\n3.UPI\n"
                        "4.Net Banking\n5.Cash\n")
                    print("Please pay Rs.550 using your " + getMethod(method))
            elif pack == 2 and pack in Prepaid :
                amount = int(input(
                    "Please enter the value for recharge for talktime\n"
                    "1.Rs.100-Talktime: Rs. 82  Val = 28 days\n"
                    "2.Rs.50-Talktime: Rs. 39  Val = 28 days\n"
                    "3.Rs.30-Talktime: Rs. 22  Val = 28 days\n"
                    "4.Rs.20-Talktime: Rs. 14  Val = 28 days\n"
                    "5.Rs.10-Talktime: Rs. 7  Val = 28 days\n"))
                if amount == 1 :
                    AmountToPay = 100
                    print("The amount to be paid is Rs. 100")
                    method = input(
                        "Enter the Enter the method of payment from the following. Choose from \n1.Credit Card\n2.Debit Card\n3.UPI\n"
                        "4.Net Banking\n5.Cash\n")
                    print("Please pay Rs.100 using your " + getMethod(method))
                if amount == 2 :
                    AmountToPay = 50
                    print("The amount to be paid is Rs. 50")
                    method = input(
                        "Enter the Enter the method of payment from the following. Choose from \n1.Credit Card\n2.Debit Card\n3.UPI\n"
                        "4.Net Banking\n5.Cash\n")
                    print("Please pay Rs.50 using your " + getMethod(method))
                if amount == 3 :
                    AmountToPay = 30
                    print("The amount to be paid is Rs. 30")
                    method = input(
                        "Enter the Enter the method of payment from the following. Choose from \n1.Credit Card\n2.Debit Card\n3.UPI\n"
                        "4.Net Banking\n5.Cash\n")
                    print("Please pay Rs.30 using your " + getMethod(method))
                if amount == 4 :
                    AmountToPay = 20
                    print("The amount to be paid is Rs. 20")
                    method = input(
                        "Enter the Enter the method of payment from the following. Choose from \n1.Credit Card\n2.Debit Card\n3.UPI\n"
                        "4.Net Banking\n5.Cash\n")
                    print("Please pay Rs.20 using your " + getMethod(method))
                if amount == 5 :
                    AmountToPay = 10
                    print("The amount to be paid is Rs. 10")
                    method = input(
                        "Enter the Enter the method of payment from the following. Choose from \n1.Credit Card\n2.Debit Card\n3.UPI\n"
                        "4.Net Banking\n5.Cash\n")
                    print("Please pay Rs.10 using your " + getMethod(method))
                # else:
                #     print("Please select valid option")
            elif pack == 3 and pack in Prepaid:
                amount = int(input(
                    "Enter the amount of recharge for data packs from the following values\n"
                    "1.Rs.1200- 240 GB data Val= 240 days\n"
                    "2.Rs.600- 72 GB data Val= 70 days\n"
                    "3.Rs.250- 50 GB data Val= 28 days\n"
                    "4.Rs.100- 12 GB data Val= 28 days\n"
                    "5.Rs.50-6 GB data Val= 28 days\n"))
                if amount == 1 :
                    AmountToPay = 1200
                    print("The amount to be paid is Rs. 1200")
                    method = input(
                        "Enter the Enter the method of payment from the following. Choose from \n1.Credit Card\n2.Debit Card\n3.UPI\n"
                        "4.Net Banking\n5.Cash\n")
                    print("Please pay Rs.1200 using your " + getMethod(method))
                if amount == 2 :
                    AmountToPay = 600
                    print("The amount to be paid is Rs. 600")
                    method = input(
                        "Enter the Enter the method of payment from the following. Choose from \n1.Credit Card\n2.Debit Card\n3.UPI\n"
                        "4.Net Banking\n5.Cash\n")
                    print("Please pay Rs.600 using your " + getMethod(method))
                if amount == 3 :
                    AmountToPay = 250
                    print("The amount to be paid is Rs. 250")
                    method = input(
                        "Enter the Enter the method of payment from the following. Choose from \n1.Credit Card\n2.Debit Card\n3.UPI\n"
                        "4.Net Banking\n5.Cash\n")
                    print("Please pay Rs.250 using your " + getMethod(method))
                if amount == 4 :
                    AmountToPay = 100
                    print("The amount to be paid is Rs. 100")
                    method = input(
                        "Enter the Enter the method of payment from the following. Choose from \n1.Credit Card\n2.Debit Card\n3.UPI\n"
                        "4.Net Banking\n5.Cash\n")
                    print("Please pay Rs.100 using your " + getMethod(method))
                if amount == 5 :
                    AmountToPay = 50
                    print("The amount to be paid is Rs. 50")
                    method = input(
                        "Enter the Enter the method of payment from the following. Choose from \n1.Credit Card\n2.Debit Card\n3.UPI\n"
                        "4.Net Banking\n5.Cash\n")
                    print("Please pay Rs.50 using your " + getMethod(method))

            display(pack)
        elif type == 2 and type in recharge :

            method = input(
                "Enter the Enter the method of payment from the following. Choose from \n1.Credit Card\n2.Debit Card\n3.UPI\n"
                "4.Net Banking\n5.Cash\n")
            print("Please pay using your " + getMethod(method))
            display(type)
        else:
            print("please select valid type of recharge")

        print("$$$$$$$$$$Thank you$$$$$$$$$$")


    else:
        print("Circle ID is invalid or not available in list")
else:
    print("Phone number is invalid")





