# C# Project - Employee Payslip program

## Background
This is an end of book project for the book Learn C# In One Day and Learn It Well. The program reads a file of different employees and positions and outputs a payslip file for each employee and a summary of employees who worked less than 10 hours.

### Changes from original project
- file input is not hard coded inside FileReader class
    - file input can by done by user input inside main, console argument, or file drag/drop
- staff hours read from file instead of user input

## Changelog

### 09/12/2023
- Program class completed
- minor changes and cleanup on all classes
- all classes completed
- revised parent CalculatePay to account for overtime hours
- good data batch test completed
- basic program requirements completed

### 09/11/2023
- FileReader class completed
- FileReader object creation and method call inside Main completed
- List<Staff> output test in Main completed
- PaySlip GeneratePaySlip and GenerateSummary method test completed

### 09/06/2023
- Program file input (user input, command line, drag/drop) to FileReader completed
- FileReader file input and file read test completed
- Completed FileReader file contents read and string manipulation/array storage
	- creating objects from file and assigning to List not completed
- Staff class completed with basic testing using FileReader
- Manager class completed with basic testing using FileReader
- Admin class completed with basic testing using FileReader

### 09/03/2023
- setup of class fields, methods, properties, constructors completed
- test file input in Program class completed

### 08/29/2023
- class structures and definitions completed
- class files created
- diagrams started
- class test connections completed

### 08/27/2023
- started definition of the project
- setup documentation structure for each class

## Classes

### Staff
>#### Parent class for employee objects
>>##### Contents:
>>>- public virtual method CalculatePay() that calculates and prints pay of each staff
>>>	- assign hWorked * hourlyRate to BasicPay
>>>	- assign BasicPay to TotalPay
>>>- variable hWorked that is a private int
>>>- variable hourlyRate that is a private float
>>>- TotalPay property with a protected float setter and public getter
>>>- BasicPay property with a private float setter and public getter
>>>- NameOfStaff property with a private string setter and public getter
>>>- HoursWorked property with public getter that returns hWorked and setter checks if value > 0 and assigns to hWorked else assigns 0
>>>- Staff constructor with string name and float rate parameters that assigns to instance variables
>>>- ToString method to display values of fields and properties of Staff class
>>##### Class Roles:
>>>-

### Manager
>#### Inherits from Staff class
>>##### Contents:
>>>- variable managerHourlyRate that is private, const, float assigned with value of 50
>>>- Allowance property of type integer with private set method
>>>- Manager constructor with name parameter of type string
>>##### Class Roles:
>>>- on object instantiation, call constructor with name value argument
>>>- override CalculatePay from Staff class
>>>		- call parent CalculatePay using base.CalculatePay() and set value of Allowance to 1000
>>>- add Allowance to TotalPay

### Admin
>#### Inherits from Staff class
>>##### Contents:
>>>- variable overtimeRate that is private, const, float assigned with value of 15.5
>>>- variable adminHourlyRate that is private, const, float assigne with value of 30
>>>- Overtime property of type float with private set method
>>>- Admin constructor with name parameter of type string
>>##### Class Roles:
>>>- on object instantiation, call constructor with name value argument
>>>- call base CalculatePay
>>>	- check if HoursWorked > 160 and update TotalPay if true
>>>- overtime = overtimeRate * (HoursWorked - 150)

### FileReader
>#### Reads a .txt file and creates a list of Staff objects based on the contents of the .txt file
>>##### Contents:
>>>- ReadFile() method that is public and returns a list of Staff objects
>>##### Class Roles:
>>>- read from a text file using ReadFile() that consist of names and positions of staff
>>>- file format: NameOfStaff,PositionOfStaff
>>>	- check if file exist using File.Exists()
>>>		- display message if file does not exist
>>>	- read file line by line using StreamReader
>>>	- split each line using delimeter
>>>	- store separated strings to result array
>>>	- close file stream after reading
>>>- Sample code:
>>>>```c#
>>>>List<Staff> myStaff = new List<Staff>(); 
>>>>string[] result = new string[2];
>>>>string path = "staff.txt"; 
>>>>string[] separator = {","};
>>>>```


### PaySlip
>#### Generates pay slip of each employee
>#### Generates summary of the details of staff who worked less than 10 hours in a month
>>##### Contents:
>>>- variable month that is a private int
>>>- variable year that is a private int
>>>- enum MonthsOfYear where months are JAN = 1, MMM = NN
>>>- PaySlip constructor with parameters int payMonth and int payYear where values are assigned to private fields
>>>- void GeneratePaySlip() method with parameter of <List> Staff
>>>- void GenerateSummary() method that generates summary of employees who worked less than 10 hours on a specified month
>>##### Class Roles:
>>>- GeneratePaySlip()
>>>>- variable path that is a string
>>>>- loop through Staff List
>>>>
>>>>```string path = EmployeeName + ".txt";```
>>>>- create StreamWriter instance to write to file (append not overwrite)
>>>>- Output Format
>>>>```text
>>>>PAYSLIP FOR {MONTH} {YEAR}
>>>>==========================
>>>>Name of Staff: {NAME}
>>>>Hours Worked: {HOURS}
>>>>
>>>>Basic Pay: {BASIC PAY}
>>>>Allowance: {ALLOWANCE} / Overtime Pay: {OVERTIME PAY}
>>>>
>>>>==========================
>>>>Total Pay: {TOTAL PAY}
>>>>==========================
>>>>```
>>>- GenerateSummary()
>>>>- get NameOfStaff, HoursWorked, order by NameOfStaff
>>>>- create instance of StreamWriter to write summary to file (summary.txt)
>>>>- Output Format
>>>>```text
>>>>Staff with less than 10 working hours
>>>>
>>>>Name of Staff: {NAME}, Hours Worked: {HOURS}
>>>>```

### Program
>#### Program entry point
>>##### Contents:
>>>- Main() function
>>>- List of staff objects named myStaff
>>>- FileReader named fr to read input file
>>>- integer variables month and year initialized to 0
>>>- Console.Read() at end of Main() function to prevent window close
>>##### Class Roles:
>>>- get year and month from user with input validation loop
>>>- read file from FileReader object and assign to list of myStaff objects
>>>- call CalculatePay
>>>- output using ToString
>>>- create PaySlip object and pass month and year
>>>- call GenerateSummary from GeneratePaySlip
