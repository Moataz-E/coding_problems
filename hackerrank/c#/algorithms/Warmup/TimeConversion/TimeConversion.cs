using System;
using System.IO;
using System.Collections.Generic;

namespace TimeConversion
{
	public class TimeConversion
	{
		private static string ConvertToMilitaryTime(string timeString)
		{
			List<string> seperatedTime = new List<string>(timeString.Split(':'));
			int hours = Convert.ToInt32(seperatedTime[0]);
			int minutes = Convert.ToInt32(seperatedTime[1]);
			int seconds = Convert.ToInt32(seperatedTime[2].Substring(0, 2));
			string midnight = seperatedTime[2].Substring(2, 2);

			int militaryHours;
			if (hours == 12 && midnight.Equals ("AM"))
				militaryHours = 0;
			else if (hours == 12 && midnight.Equals("PM"))
				militaryHours = 12;
			else if (midnight.Equals("PM"))
				militaryHours = hours + 12;
			else
				militaryHours = hours;

			return String.Format("{0:D2}:{1:D2}:{2:D2}", militaryHours, minutes, seconds);
		}

		public static void Main(string[] args)
		{
			string timeInput = Console.ReadLine();
			string militaryTime = ConvertToMilitaryTime(timeInput);
			Console.WriteLine(militaryTime);
		}
	}
}

