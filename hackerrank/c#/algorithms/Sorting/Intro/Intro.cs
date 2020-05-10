using System;
using System.Collections.Generic;

namespace Intro
{
	public class Intro
	{
		private static int FindIndex(List<int> array, int arraySize, int value)
		{
			for (int i = 0; i < arraySize; i++)
			{
				if (array[i] == value)
					return i;
			}
			return -1;
		}

		public static void Main(String[] args)
		{
			int value = Convert.ToInt32(Console.ReadLine());
			int arraySize = Convert.ToInt32(Console.ReadLine());
			List<string> arrayStrings = new List<string>(Console.ReadLine().Split());
			List<int> array = arrayStrings.ConvertAll(Int32.Parse);
			Console.WriteLine(FindIndex(array, arraySize, value));
		}
	}
}

