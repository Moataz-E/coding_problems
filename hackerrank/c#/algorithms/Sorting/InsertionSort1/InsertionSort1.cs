using System;
using System.Collections.Generic;

namespace InsertionSort1
{
	public class InsertionSort1
	{
		private static void InitializeInsertionSort(List<int> array, int arraySize)
		{
			int valueToInsert = array[arraySize - 1];

			for (int i = (arraySize - 2); i >= 0; i--)
			{
				int valueToCompare = array[i];
				if (valueToInsert < valueToCompare)
					array [i + 1] = valueToCompare;
				else 
				{
					Console.WriteLine(String.Join(" ", array));
					return;
				}

				Console.WriteLine(String.Join(" ", array));
				array[i] = valueToInsert;
			}
			Console.WriteLine(String.Join(" ", array));
		}

		public static void Main(string[] args)
		{
			int arraySize = Convert.ToInt32(Console.ReadLine());
			List<string> arrayStrings = new List<string>(Console.ReadLine().Split());
			List<int> array = arrayStrings.ConvertAll(Int32.Parse);
			InitializeInsertionSort(array, arraySize);
		}
	}
}

