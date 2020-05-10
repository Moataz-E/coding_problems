using System;
using System.IO;
using System.Collections.Generic;

namespace PlusMinus
{
	public class PlusMinus
	{
		private static Dictionary<string, float> CalculateParityFractions(int count, List<int> numbers)
		{
			float numberOfPositives = 0;
			float numberOfNegatives = 0;
			float numberOfZeroes = 0;

			foreach (int number in numbers)
			{
				if (number > 0)
					numberOfPositives++;
				else if (number < 0)
					numberOfNegatives++;
				else
					numberOfZeroes++;
			}

			Dictionary<string, float> parityFractions = new Dictionary<string, float>();
			parityFractions.Add("positive", numberOfPositives / count);
			parityFractions.Add("negative", numberOfNegatives / count);
			parityFractions.Add("zero", numberOfZeroes / count);

			return parityFractions;
		}

		public static void Main(string[] args)
		{
			int count = Convert.ToInt32(Console.ReadLine());
			List<string> numbersString = new List<string>(Console.ReadLine().Split(' '));
			List<int> numbers = numbersString.ConvertAll (Int32.Parse);
			Dictionary<string, float> parityFractions = CalculateParityFractions(count, numbers);
			Console.WriteLine (parityFractions ["positive"]);
			Console.WriteLine (parityFractions ["negative"]);
			Console.WriteLine (parityFractions ["zero"]);
		}
	}
}

