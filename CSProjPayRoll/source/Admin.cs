// Admin.cs

using System;

namespace project{
	class Admin : Staff{
		// Fields
		private const float overtimeRate = 15.5F;
		private const float adminHourlyRate = 30.0F;
		
		// Properties
		// auto-implemented
		public float Overtime{
			private set;
			get;
		}
		
		// Constructor
		public Admin(string name) : base(name, adminHourlyRate){
			// empty
		}
		
		// Methods
		
		/* Override CalculatePay speicific to Admin object */
		
		public override void CalculatePay(){
			// calculate base pay using parent function
			base.CalculatePay();
			// calculate overtime pay if there is any and add to total pay
			if(HoursWorked > MAX_LEGAL_HOURS){
				Overtime = overtimeRate * (HoursWorked - MAX_LEGAL_HOURS);
				TotalPay = TotalPay + Overtime;
			}
		}
		
		/* ToString override to output object values */
		/* Get output from parent class and add output from Admin class */
		
		public override string ToString(){
			return base.ToString() + $"Overtime Pay: {Overtime:C2}\n";
		}
	}
}
