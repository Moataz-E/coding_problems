using System;
using System.IO;
using System.Collections.Generic;

namespace Warmup
{
	public class SolveMeFirst
	{
		private static int Sum(int num1, int num2)
		{
			return num1 + num2;
		}

		public static void Main(String[] args)
		{
			int num1 = Convert.ToInt32(Console.ReadLine());
			int num2 = Convert.ToInt32(Console.ReadLine());
			int sum = Sum(num1, num2);
			Console.WriteLine (sum);
		}
	}
}

