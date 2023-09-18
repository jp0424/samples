// PaySlip.cs

using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

namespace project{
	class PaySlip{
		// Fields
		private byte month;
		private short year;
		enum MonthsOfYear {JAN = 1, FEB, MAR, APR, MAY, JUN, 
							JUL, AUG, SEP, OCT, NOV, DEC}
							
		// Constructor
		public PaySlip(int payMonth, int payYear){
			this.month = (byte) payMonth;
			this.year = (short) payYear;
		}
		
		// Method
		
		/* GeneratePaySlip method */
		/* Reads myStaff List and generates payslip report for each staff */
		/* Output reports to individual files with staff name as file name */
		
		public void GeneratePaySlip(List<Staff> myStaff){
			string path = "";
			// loop through myStaff
			foreach(Staff f in myStaff){
				// file name => {NameOfStaff}.txt
				path = f.NameOfStaff + ".txt";
				StreamWriter sw = new StreamWriter(path);

				/* Output Sample
				PAYSLIP FOR {MONTH} {YEAR}
				==========================
				Name of Staff: {NAME}
				Hours Worked: {HOURS}
				
				Basic Pay: {BASIC PAY}
				Allowance: {ALLOWANCE} / Overtime Pay: {OVERTIME PAY}
				
				==========================
				Total Pay: {TOTAL PAY}
				==========================
				*/
				sw.WriteLine("PAYSLIP FOR {0} {1}", (MonthsOfYear) month, year);
				sw.WriteLine("===================");
				sw.WriteLine("Name of Staff: {0}", f.NameOfStaff);
				sw.WriteLine("Hours Worked: {0}\n", f.HoursWorked);
				sw.WriteLine("Basic Pay: {0:C}", f.BasicPay);
				// get type of Staff object and check if it is Admin or Manager
				// write appropriate line for each Staff type
				if(f.GetType() == typeof(Admin)){
					sw.WriteLine("Overtime Pay: {0:C}\n", ((Admin)f).Overtime);
				}else if(f.GetType() == typeof(Manager)){
					sw.WriteLine("Allowance: {0:C}\n", ((Manager)f).Allowance);
				}
				sw.WriteLine("===================");
				sw.WriteLine("Total Pay: {0:C}", f.TotalPay);
				sw.WriteLine("===================");
				sw.Close();
			}
		}
		
		public void GenerateSummary(List<Staff> myStaff){
			string path = "summary.txt";
			
			// LINQ query
			// select staff that worked under 10 hours
			
			var hoursQuery = 
							from f in myStaff
							where f.HoursWorked < 10
							orderby f.NameOfStaff ascending
							select new {f.NameOfStaff, f.HoursWorked};
			
			StreamWriter sw = new StreamWriter(path);
			
			/* Output Sample
				Staff with less than 10 working hours
				Name of Staff: {NAME}, Hours Worked: {HOURS}
			*/
			sw.WriteLine("Staff with less than 10 working hours\n");
			foreach(var f in hoursQuery){
				sw.WriteLine("Name of Staff: {0}, Hours Worked: {1}", f.NameOfStaff, f.HoursWorked);
			}
			sw.Close();
		}
	}
}