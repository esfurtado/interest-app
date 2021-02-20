# interest-app

A simple finance calculator of investment interest and loan monthly repayment.
This project is part of the Software Egineering course from Hyperion.

## Start

Use the python command followed by the program name to call it.

```
> python finance_calculators.py
Choose either 'investment' or 'bond' from the menu below to proceed:

investment      - to calculate the amount of interest you'll earn on invested money

bond    - to calculate the amount you'll have to pay on a home loan
```


## Using the interest-app
Once you start the program it will ask you which calculator you want to use: investment or bond.

#### Investment
This calculates the amount earned after interest is applied on an investment over a period of time.
The investment option will ask for further details such as the invested amount and investment time in years. This option will also have another subsection: compound interest or simple interest. The formulas for these are described in the table below. Numerical inputs should NOT include symbols. Once all fields have been answered to it will give the final amount that will be earned.

|      Simple          |        Compound     |
|----------------------|---------------------|
|Total = P(1 + r * t)  |Total = P(1+ r) ^ t  |
|formula abreviations|P - payment, r - rate, t - time in years   |


#### Bond
The bond option is to calculate how much money will be paid on a bank loan. Once this option is selected it will ask for details such as the property cost and interest. Once all fields have been completed the calculator will provide the final bill.

#### Note: This program is not on a loop, so for each calculation call the program.
