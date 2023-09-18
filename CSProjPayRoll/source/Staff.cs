// Staff.cs
// Parent class for staff objects
// Contains basic information about staff and pay calculation

using System;

namespace project {
	class Staff{
		// Fields
		private int hWorked;
		private float hourlyRate;
		protected const byte MAX_LEGAL_HOURS = 160;
		
		// Constructor
		public Staff(string name, float rate){
			this.hourlyRate = rate;
			// call NameOfStaff property and assign name
			NameOfStaff = name;
		}
		
		// Properties
		// auto-implemented
		public float TotalPay{
			protected set;
			get;
		}
		// auto-implemented
		public float BasicPay{
			private set;
			get;
		}
		// auto-implemented
		public string NameOfStaff{
			private set;
			get;
		}
		
		/* HoursWorked property with input check if value > 0 */
		
		public int HoursWorked{
			set{
				if(value > 0){
					this.hWorked = value;
				}else{
					this.hWorked = 0;
				}
			}
			get{
				return this.hWorked;
			}
		}
		
		// Methods
		
		/* Parent CalculatePay method */
		
		public virtual void CalculatePay(){
			// calculate base pay using hours * rate and assign to TotalPay
			Console.WriteLine("Calculating Pay...");
			if(this.hWorked > MAX_LEGAL_HOURS){
				BasicPay = MAX_LEGAL_HOURS * this.hourlyRate;
			}else{
				BasicPay = this.hWorked * this.hourlyRate;
			}
			TotalPay = BasicPay;
		}
		
		/* ToString override to output object values */
		
		public override string ToString(){
			return($"Employee Name: {NameOfStaff}\nHours Worked: {hWorked}\nHourly Rate: {hourlyRate}\nBasic Pay: {BasicPay:C2}\nTotal Pay: {TotalPay:C2}\n");
		}
	}
}