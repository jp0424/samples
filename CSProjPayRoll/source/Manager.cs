// Manager.cs

using System;

namespace project{
	class Manager : Staff{
		// Fields
		private const float managerHourlyRate = 50.0F;
		
		// Properties
		// auto-implemented
		public int Allowance{
			private set;
			get;
		}
		
		// Constructor
		public Manager(string name):base(name, managerHourlyRate){
			// empty
		}
		
		// Methods
		
		/* Override CalculatePay specific to Manager object */
		
		public override void CalculatePay(){
			// calculate base pay using parent function
			base.CalculatePay();
			// add allowance option for Manager class
			if(HoursWorked > MAX_LEGAL_HOURS){
				// set Allowance
				Allowance = 1000;
				// update total pay to add allowance if hours condition is met
				TotalPay = TotalPay + Allowance;
			}
		}
		
		/* ToString override to output object values */
		/* Get output from parent class and add output from Manager class */
		
		public override string ToString(){
			return base.ToString() + $"Allowance: {Allowance:C2}\n";
		}
	}
}