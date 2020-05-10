using System;
using System.IO;
using System.Collections.Generic;

namespace Warmup
{
	public class SimpleArraySum
	{
		private static int SumArray(int count, List<int> numbers)
		{
			if (count != numbers.Count)
				throw new ArgumentException("Provided count must be equal to number of integers in array.");

			int accumulatedSum = 0;
			foreach (int number in numbers) 
			{
				accumulatedSum += number;
			}
			return accumulatedSum;
		}

		public static void Main(String[] args)
		{
			int count = Convert.ToInt32 (Console.ReadLine());
			List<string> numbersString = new List<string>(Console.ReadLine().Split(' '));
			List<int> numbers = numbersString.ConvertAll(Int32.Parse);
			int sum = SumArray(count, numbers);
			Console.WriteLine(sum);
		}
	}
}

