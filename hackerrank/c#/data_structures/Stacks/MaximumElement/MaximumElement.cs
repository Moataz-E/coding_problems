using System;
using System.IO;
using System.Collections.Generic;

namespace MaximumElement
{
	public class MaximumElement
	{
		private static Query ParseQuery(string queryString)
		{
			Query query;
			List<string> queryContentString = new List<string>(queryString.Split(' '));
			List<int> queryContent = queryContentString.ConvertAll(Int32.Parse);
			if (queryContent.Count > 1)
				query = new Query(queryContent[0], queryContent[1]);
			else
				query = new Query(queryContent [0]);

			return query;
		}

		private static int MaxElement(List<int> numbers)
		{
			int max = 0;
			foreach (int number in numbers)
			{
				if (number > max)
					max = number;
			}
			return max;
		}

		private static void ExecuteQueries(List<Query> queries)
		{
			int maxElement = 0;
			List<int> stack = new List<int>();
			foreach (Query query in queries)
			{
				if (query.QueryType == 1) {
					maxElement = (query.ElementToPush > maxElement) ? query.ElementToPush : maxElement;
					stack.Add(query.ElementToPush);
				} else if (query.QueryType == 2)
				{
					int elementToRemove = stack [stack.Count - 1];
					stack.RemoveAt(stack.Count - 1);
					maxElement = (elementToRemove == maxElement) ? MaxElement(stack) : maxElement;
				}
				else if (query.QueryType == 3)
					Console.WriteLine(maxElement);
			}
		}

		public static void Main(string[] args)
		{
			int queryCount = Convert.ToInt32(Console.ReadLine());

			List<Query> queries = new List<Query>();
			for (int queryNum = 0; queryNum < queryCount; queryNum++)
			{
				string queryString = Console.ReadLine();
				queries.Add(ParseQuery(queryString));
			}
			ExecuteQueries(queries);
		}
	}

	public class Query
	{
		public int QueryType { get; set; }
		public int ElementToPush { get; set; }

		public Query(int queryType)
		{
			QueryType = queryType;
		}

		public Query(int queryType, int element)
		{
			QueryType = queryType;
			ElementToPush = element;
		}
	}
}