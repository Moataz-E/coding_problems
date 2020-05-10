using System;
using System.Collections.Generic;

namespace TwoRobots
{
	public class TwoRobots
	{
		private List<Tuple<int, int>> Queries { get; set; }

		public TwoRobots(List<Tuple<int, int>> queries)
		{
			Queries = queries;
		}

		public int nextShortMove(int AccumulatedDistance, int r1Location, int r2Location, int lastQuery,
		                         int notMinimumMoves)
		{
			int r1Distance;
			int r2Distance;
			int totalR1MoveDistance;
			int totalR2MoveDistance;

			// Base case, return accumulated distance if previous query was the last query.
			if (lastQuery >= Queries.Count)
				return AccumulatedDistance;

			if (notMinimumMoves > 5)
				return Int32.MaxValue;

			int fromLocation = Queries[lastQuery].Item1;
			int toLocation = Queries[lastQuery].Item2;

			// -1 denotes a robot that hasn't moved yet.
			if (r1Location == -1)
				r1Distance = Math.Abs(fromLocation - toLocation);
			else
				r1Distance = Math.Abs(r1Location - fromLocation) + Math.Abs(fromLocation - toLocation);

			if (r2Location == -1)
				r2Distance = Math.Abs(fromLocation - toLocation);
			else
				r2Distance = Math.Abs(r2Location - fromLocation) + Math.Abs(fromLocation - toLocation); 

			totalR1MoveDistance = AccumulatedDistance + r1Distance;
			totalR2MoveDistance = AccumulatedDistance + r2Distance;

			int r1Moved;
			int r2Moved;
			if (r1Distance < r2Distance)
			{
				r1Moved = nextShortMove(
					totalR1MoveDistance, toLocation, r2Location, lastQuery + 1, notMinimumMoves);
				r2Moved = nextShortMove(
					totalR2MoveDistance, r1Location, toLocation, lastQuery + 1, notMinimumMoves++);
			}
			else
			{
				r1Moved = nextShortMove(
					totalR1MoveDistance, toLocation, r2Location, lastQuery + 1, notMinimumMoves++);
				r2Moved = nextShortMove(
					totalR2MoveDistance, r1Location, toLocation, lastQuery + 1, notMinimumMoves);
			}
			return Math.Min(r1Moved, r2Moved);
		}

		public static void Main(String[] args)
		{
			int testCases = Convert.ToInt32(Console.ReadLine());
			if (testCases > 50)
				return;

			for (int testCase = 0; testCase < testCases; testCase++)
			{
				List<string> testCaseInfoStr = new List<string>(Console.ReadLine().Split());
				List<int> testCaseInfo = testCaseInfoStr.ConvertAll(Int32.Parse);

				int numberOfContainers = testCaseInfo[0];
				int numberOfQueries = testCaseInfo[1];
				if ((numberOfContainers > 1000) || (numberOfQueries > 1000))
					return;

				// Populate testCase entry in dictionary with queries
				List<Tuple<int, int>> queries = new List<Tuple<int, int>>();
				for (int query = 0; query < testCaseInfo[1]; query++)
				{
					List<string> queryInputStr = new List<string>(Console.ReadLine().Split());
					List<int> queryInput = queryInputStr.ConvertAll(Int32.Parse);
					queries.Add(new Tuple<int, int>(queryInput[0], queryInput[1]));
				}
				TwoRobots twoRobots = new TwoRobots(queries);
				int shortestAccumulatedDistance = twoRobots.nextShortMove(0, -1, -1, 0, 0);
				Console.WriteLine(shortestAccumulatedDistance);
			}
		}
	}
}

