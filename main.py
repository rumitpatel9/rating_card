vehicle_value = int(input("ple enter vehicle value."))
premium_rate = 5 # in % 
premium_amount = ((vehicle_value * premium_rate)/100)
personal_accident_cover = 0
hospital_cash_cover = 0
loss_of_use_rate = 0.25 # in %
excess_protector_rate =0.25 # in %
levies_tax_rate =0.45 # in %
levies_amount = ((vehicle_value * levies_tax_rate)/100)
stamp_duty_amount =50
loss_of_use_cover_premium = ((vehicle_value * loss_of_use_rate)/100)
excess_protector_premium = ((vehicle_value * excess_protector_rate)/100)
premium_sum =premium_amount+personal_accident_cover+hospital_cash_cover+loss_of_use_cover_premium+excess_protector_premium
premium_with_taxes =premium_sum+levies_amount+stamp_duty_amount

#  This section relates to customers that want to take insurance and pay monthly
interest_rate = 5 # in %
interest_charge = ((premium_with_taxes * interest_rate)/100)
facility_fees_amount =500
excise_duty_rate =2 #in %
excise_duty_amount =((facility_fees_amount * excise_duty_rate)/100)
total_payable =premium_with_taxes +interest_charge+facility_fees_amount+excise_duty_amount
down_payment_rate = 10 # in %
down_payment =((total_payable * down_payment_rate)/100)
net_balance =(total_payable -down_payment)
number_of_installments =int(input("plese enter how many installment you wont to do..."))
monthly_installments =(net_balance/number_of_installments)
commission_rate =10 # in %
commission_amount =((premium_sum * commission_rate)/100)
user =int(input("<-----check Premium with taxes----- enter 1>\n<-----check EMI and down payment and net pay----enter 2>\n<-----check number_of_installments and commission_amount----enter 3: >"))
if user == 1:
    print("<----Premium with taxes--->: ",premium_with_taxes)
elif user ==2:
    print("<----EMI--->: ",total_payable)
    print("<----down_payment--->: ",down_payment)
    print("<----net_balance--->: ",net_balance)
elif user == 3:
    print("<----number_of_installments--->: ",number_of_installments)
    print("<----commission_amount--->: ", commission_amount)
else:
    print("oops!!!!! somthing want wrong..")
