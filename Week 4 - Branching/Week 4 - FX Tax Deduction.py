# License      : Simplified 2-Clause BSD 
# Developer(s) : Bora Güngören

# In Turkey when you buy Foreign currency there is a very small (0.2 percent) tax.
# When you sell foreign currency there is

# When you buy at a certain rate. Say 1 USD is 8 TL. And you buy 1.000 USD.
# You pay 8.000 TL to the bank for the 1.000 USD. and 8.000 * (0.2 / 100) = 16 TL as tax.
# When you sell at say 8.02, you get 8.020 TL. But your profit is actually (8020 - 8000) - 16 = 4 TL.
# Which is at 4 / 8000 = 0.5 percent.

# If you sell at a very small profit margin, due to tax, you might be at a loss.
# This program will calculate whether you are at profit or at loss

buyingRate = float( input("Please state the buying rate for your transaction:") )
boughtDollars = float (input("How much are you buying in dollars?") )
paidToBank = buyingRate * boughtDollars
taxRate = 0.002 # 0.2 percent
taxPaid = paidToBank * taxRate
print("You paid", paidToBank, "TL to the bank, and also", taxPaid, "TL as tax.")

sellingRate = float( input("Please state the selling rate for your transaction:") )
bankPaysUs = sellingRate * boughtDollars
profitBeforeTax = bankPaysUs - paidToBank
profitAfterTax = profitBeforeTax - taxPaid

if profitAfterTax > 0:
    print("We are at profit")
    margin = profitAfterTax / paidToBank # Not at percentage level i.e. 0.005
    marginPercent = margin * 100 # i.e. 0.5 percent
    print ("Our profit margin was", marginPercent, "percent")
else:
    print("We are at loss due to taxes.")
    
# Decision table:
# -------------------------------------------------
# |  if at profit           | if not at profit    |
# |  defined as profit > 0  | defined as else     |
# |  should calculate profit| should state we are |
# |   margin and display    |   at loss
# |-------------------------|
# | if         | if not     |
# -------------------------------------------------
    
# Flow chart
# ------> Question?  ---Yes (If)---> Action ---|
#           |                            |
#           |                            |
#           No (Else)                    |
#           |                            |
#           --> Alternate action -------> Merge ---->

