def total_calci(bill_amount,tip_perc):
    total=bill_amount*(1+0.01*tip_perc)
    total=round(total,2)
    print("please pay $",total)
total_calci(10000,50)