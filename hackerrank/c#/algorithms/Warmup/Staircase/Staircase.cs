using System;

namespace Staircase
{
	public class Staircase
	{
		private static void PrintStaircase(int height)
		{
			for (int i = 1; i <= height; i++)
				Console.WriteLine(String.Concat(new String(' ', height - i), new String('#', i)));
		}

		public static void Main(string[] args)
		{
			int heightInput = Convert.ToInt32(Console.ReadLine());
			PrintStaircase(heightInput);
		}
	}
}

