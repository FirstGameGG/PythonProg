inc = float(input())
ex = float(input())

profit =  inc + ex

print("1234567890" * 3)
output_inc = "{0:<13s}{1:+8.2f} baths".format("Total Income", inc)
output_ex = "{0:<13s}{1:+8.2f} bahts".format("Expense", ex)
output_prof = "{0:<13s}{1:008.2f} bahts".format("Profit", profit)
print(output_inc)
print(output_ex)
print(output_prof)