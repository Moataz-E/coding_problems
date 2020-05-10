using System;
using System.IO;
using System.Collections.Generic;

namespace Warmup
{
	public class DiagonalDifference
	{
		private static int CalculateDiagonalDifference(int rowsCount, List<List<int>> matrix)
		{
			int primaryDiagonalSum = 0;
			int secondaryDiagonalSum = 0;
			for (int rowNum = 0; rowNum < rowsCount; rowNum++)
			{
				primaryDiagonalSum += matrix[rowNum][rowNum];
				secondaryDiagonalSum += matrix[rowNum][rowsCount - rowNum-1];
			}
			return Math.Abs(primaryDiagonalSum - secondaryDiagonalSum);
		}

		public static void Main(string[] args)
		{
			int rowsCount = Convert.ToInt32(Console.ReadLine());
			List<List<int>> matrix = new List<List<int>>(rowsCount);
			for (int rowNum = 0; rowNum < rowsCount; rowNum++)
			{
				List<string> rowStrings = new List<string>(Console.ReadLine().Split(' '));
				matrix.Add (rowStrings.ConvertAll (Int32.Parse));
			}
			int diagonalDifference = CalculateDiagonalDifference(rowsCount, matrix);
			Console.WriteLine(diagonalDifference);
		}
	}
}