using System;
using System.IO;
using System.Collections.Generic;

namespace Warmup
{
	public class AVeryBigSum
	{
		public static long SumArrayBigNumbers(int count, List<long> longNumbers)
		{
			if (count != longNumbers.Count)
				throw new ArgumentException("Provided count must be equal to number of integers in array.");

			long accumulatedSum = 0L;
			foreach (long longNumber in longNumbers)
			{
				accumulatedSum += longNumber;
			}
			return accumulatedSum;
		}

		public static void Main(String[] args)
		{
			int count = Convert.ToInt32(Console.ReadLine());
			List<string> numbersString = new List<string>(Console.ReadLine().Split(' '));
			List<long> longNumbers = numbersString.ConvertAll(long.Parse);
			long sum = SumArrayBigNumbers(count, longNumbers);
			Console.WriteLine(sum);
		}
	}
}

