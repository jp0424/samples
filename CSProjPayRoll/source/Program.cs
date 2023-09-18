// Program.cs
// main program entry

using System;
using System.Collections.Generic;

namespace project{
	class Program{
		public static void Main(string[] args){
			/* local variable initialization */
			int month = 0, year = 0;
			
			/* Get current pay period month and year from user */
			
			// ask user for month/year input
			// read input and try to parse input to int
			// if exception is thrown, reset values to 0 to restart loop
			while(month == 0){
				Console.Write("Please enter the month (1-12): ");
				try{
					month = int.Parse(Console.ReadLine());
					// check if month is between 1-12
					// reset if outside of range
					if(month < 1 || month > 12){
						Console.WriteLine("Expecting input between 1 - 12. Received {0}\n", month);
						month =0 ;
					}
				}catch(Exception e){
					Console.WriteLine(e.Message);
					month = 0;
				}
			}
			
			while(year == 0){
				Console.Write("\nPlease enter the year: ");
				try{
					year = int.Parse(Console.ReadLine());
					Console.WriteLine();
				}catch(Exception e){
					Console.WriteLine(e.Message);
					year = 0;
				}
			}
			
			/* Get file path */
			/* Basic filepath checker */
			/* Simple check if an argument is passed to main */
			/* No check if argument is valid path/filename */
			
			string path = "";
			
			// if argument length > 0 - arguments are provided in console
			if(args.Length > 0){
				// take argument value, convert to raw string and assign to path
				path = @$"{args[0]}";
			}else if(args.Length == 0){
				// ask user for input if no argument is provided
				string userIn = "";
				Console.WriteLine("Enter filename in same directory or full path");
				Console.Write(">>> ");
				userIn = Console.ReadLine();
				// if input is nonzero assign input to path
				if(userIn.Length > 0){
					path = userIn;
				}
				// else assign an empty string - default value
			}
			
			/* Create FileReader object, process file and output to List */
			
			FileReader fr = new FileReader();
			List<Staff> myStaff = fr.ReadFile(path); //assign output to myStaff

			/* Loop through List, calculate pay for each Staff object and output */
			/* Catch any errors */
			
			for(int i = 0; i < myStaff.Count; i++){
				try{
					myStaff[i].CalculatePay();
					Console.WriteLine(myStaff[i].ToString());
				}
				catch(Exception e){
					Console.WriteLine(e.Message);
					i--;
				}
			}
			
			/* create PaySlip object and pass month and year */
			/* call GeneratePaySlip and GenerateSummary and pass myStaff List */
			
			PaySlip paySlip = new PaySlip(month, year);
			paySlip.GeneratePaySlip(myStaff);
			paySlip.GenerateSummary(myStaff);
			
			Console.Read();
		}
	}
}