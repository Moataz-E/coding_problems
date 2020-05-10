using System;
using System.IO;
using System.Collections.Generic;

namespace ArraysDS
{
	public class ArraysDS
	{
		private static string ReverseNumbersList(int count, List<int> numbers)
		{
			if (count != numbers.Count)
				throw new ArgumentException("Provided count must be equal to number of integers in array.");

			List<int> numbersReversed = new List<int>();
			for (int i = (numbers.Count - 1); i >= 0; i--)
			{
				numbersReversed.Add(numbers[i]);
			}

			return String.Join(" ", numbersReversed);
		}

		public static void Main(string[] args)
		{
			int count = Convert.ToInt32(Console.ReadLine());
			List<string> numbersString = new List<string>(Console.ReadLine().Split(' '));
			List<int> numbers = numbersString.ConvertAll(Int32.Parse);
			string numbersReversed = ReverseNumbersList(count, numbers);
			Console.WriteLine(numbersReversed);
		}
	}
}

