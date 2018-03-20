dayup=1
dayfactor=0.01
for i in range(365):
    i = i + 1
    if i % 7 in [1,2,3]:
        dayup=dayup
    else:
        dayup=dayup*(1+dayfactor)
print("最后的能力值:{}".format(dayup))
