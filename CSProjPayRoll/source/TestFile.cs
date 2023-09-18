// TestFile.cs

using System;
using System.IO;

/* Dummy program that takes staff.txt as input and rewrites file with randomized staff type and worked hours*/

class Program{
	enum StaffType {Admin = 1, Manager}
	
	public static void Main(string[] args){
		string path = "";
		string fileName = "";
		
		// get full pathname and convert to raw string and pass to fileSubstring
		// fileSubstring returns full path without file extension
		if(args.Length > 0){
			path = @$"{args[0]}";
			fileName = fileSubstring(path);
		}
		
		// if file exist
		// create temporary file using same file name for writing
		// read each line and store to nameOfStaff variable
		// generate random number between 1-2 and store appropriate enum value to staffType
		// generate random number between 0-320 and store to hoursWorked
		// combine output to one string and write to temporary file
		// continue until end of stream is reached
		// close original and temporary files
		// delete original file
		// rename file with .txt extension
		// inform user if file does not exist
		
		Random rand = new Random();
		if(File.Exists(path)){
			StreamReader sr = new StreamReader(path);
			StreamWriter sw = new StreamWriter(fileName + "temp");
			string nameOfStaff = "";
			string staffType = "";
			ushort hoursWorked = 0;
			//do stuff
			while(sr.EndOfStream != true){
				nameOfStaff = sr.ReadLine();
				staffType = ((StaffType) rand.Next(1, 3)).ToString();
				hoursWorked = (ushort) rand.Next(0, 320);
				sw.WriteLine("{0},{1},{2}", nameOfStaff, staffType, hoursWorked);
			}
			sr.Close();
			sw.Close();
			File.Delete(path);
			File.Move(fileName + "temp", fileName + "txt");
		}else{
			Console.WriteLine("File does not exist");
		}
	}
	
	
	/* Reads absolute path and returns a substring from start of string to last */
	/* occuring period (start of file extension) */
	private static string fileSubstring(string path){
		string fileName = path.Substring(0, path.LastIndexOf('.') + 1);
		return fileName;
	}
}