// FileReader.cs
// Read a text file and create a list of Staff objects from the text file

using System;
using System.IO;
using System.Collections.Generic;

namespace project{
	class FileReader{
		// Methods
		
		/* Read file from path name and return a List from file contents */
		
		public List<Staff> ReadFile(string path){
			List<Staff> myStaff = new List<Staff>();
			// access file
			// if file exist continue file read
			if(File.Exists(path)){
				StreamReader sr = new StreamReader (path);
				// while line exists
				while(sr.EndOfStream != true){
					// read line, split line using delimeters and store to array
					string[] result = new string[2];
					result = sr.ReadLine().Split(',');
					
					// get value from result[1] and check if value is admin/manager
					// for each staff type
					// create new Admin/Manager object and pass result[0] (Employee Name) to constructor
					//// get value from result[2], parse to float (to accomodate decimal input), then cast to int and assign to instance variable using HoursWorked property
					// assign Staff object to myStaff
					
					if(result[1].ToLower() == "admin"){
						Admin adminObj = new Admin(result[0]);
						adminObj.HoursWorked = (int) (float.Parse(result[2]));
						myStaff.Add(adminObj);
					}else if(result[1].ToLower() == "manager"){
						Manager managerObj = new Manager(result[0]);
						managerObj.HoursWorked = (int) (float.Parse(result[2]));
						myStaff.Add(managerObj);
					}else{
						Console.WriteLine("Input not recognized. Expecting 'Admin' or 'Manager'.");
					}
				}
				sr.Close();
			}
			else{
				Console.WriteLine("File does not exist");
			}
			return myStaff;
		}
	}
}