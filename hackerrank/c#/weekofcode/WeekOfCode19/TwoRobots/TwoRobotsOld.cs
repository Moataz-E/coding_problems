using System;
using System.IO;
using System.Collections.Generic;

namespace TwoRobotsOld
{
	public class TwoRobotsOld
	{
		private static List<int> CalculateShortestDistance(Dictionary<int, List<Tuple<int, int>>> testCaseQueries)
		{
			List<int> shortestDistance = new List<int>();

			foreach (List<Tuple<int, int>> testCase in testCaseQueries.Values)
			{
				int r1Location = 0;
				int r2Location = 0;
				int stepNumber = 0;
				int totalDistance = 0;
				foreach (Tuple<int, int> testCaseQuery in testCase)
				{
					int fromLocation = testCaseQuery.Item1;
					int toLocation = testCaseQuery.Item2;

					if (stepNumber == 0)
					{
						totalDistance += Math.Abs(fromLocation - toLocation);
						r1Location = toLocation;
					}
					else if (stepNumber == 1)
					{
						totalDistance += Math.Abs(fromLocation - toLocation);
						r2Location = toLocation;
					} 
					else
					{
						if (Math.Abs(r1Location - fromLocation) < Math.Abs(r2Location - fromLocation))
						{
							totalDistance += Math.Abs(r1Location - fromLocation) + Math.Abs(fromLocation - toLocation); 
							r1Location = toLocation;
						}
						else
						{
							totalDistance += Math.Abs(r2Location - fromLocation) + Math.Abs(fromLocation - toLocation);
							r2Location = toLocation;
						}

					}
					stepNumber++;
				}
				shortestDistance.Add(totalDistance);
			}
			return shortestDistance;
		}

		public static void MainOld(String[] args)
		{
			// Dictionary containing Information regarding each test case, where item1 in tuple is number of containers
			// and item2 is number of queries.
			Dictionary<int, Tuple<int,int>> testCaseInfos = new Dictionary<int, Tuple<int, int>>();

			// Dictionary containing queries associated with each test case.
			Dictionary<int, List<Tuple<int, int>>> testCaseQueries = new Dictionary<int, List<Tuple<int, int>>>();

			int testCases = Convert.ToInt32(Console.ReadLine());
			for (int testCase = 0; testCase < testCases; testCase++)
			{
				List<string> testCaseInfoStr = new List<string>(Console.ReadLine().Split());
				List<int> testCaseInfo = testCaseInfoStr.ConvertAll(Int32.Parse);
				testCaseInfos.Add(testCase, new Tuple<int, int>(testCaseInfo[0], testCaseInfo[1]));

				// Populate testCase entry in dictionary with queries
				List<Tuple<int, int>> queries = new List<Tuple<int, int>>();
				for (int query = 0; query < testCaseInfo[1]; query++)
				{
					List<string> queryInputStr = new List<string>(Console.ReadLine().Split());
					List<int> queryInput = queryInputStr.ConvertAll(Int32.Parse);
					queries.Add(new Tuple<int, int>(queryInput[0], queryInput[1]));
				}
				testCaseQueries.Add(testCase, queries);
			}

			// Print shortest distance needed to travel for each test case.
			List<int> shortestDistances = CalculateShortestDistance(testCaseQueries);
			foreach (int distance in shortestDistances)
			{
				Console.WriteLine(distance);
			}
		}
	}
}