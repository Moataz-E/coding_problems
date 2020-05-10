using System;
using System.IO;
using System.Collections.Generic;

namespace QHEAP1
{
	public class QHEAP1
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

		private static int MinElement(List<int> numbers)
		{
			int min = Int32.MaxValue;
			foreach (int number in numbers)
			{
				if (number < min)
					min = number;
			}
			return min;
		}

		private static void ExecuteQueries(List<Query> queries)
		{
			int minElement = Int32.MaxValue;
			List<int> heap = new List<int>();
			foreach (Query query in queries)
			{
				if (query.QueryType == 1) {
					minElement = (query.ElementToPush < minElement) ? query.ElementToPush : minElement;
					heap.Add(query.ElementToPush);
				} else if (query.QueryType == 2)
				{
					int indexOfElementToRemove = heap.FindIndex(element => element == query.ElementToPush);
					int elementToRemove = heap[indexOfElementToRemove];
					heap.RemoveAt(indexOfElementToRemove);
					minElement = (elementToRemove == minElement) ? MinElement(heap) : minElement;
				}
				else if (query.QueryType == 3)
					Console.WriteLine(minElement);
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