using System;
using System.Collections.Generic;

namespace FixTheCycles
{
	public class FixTheCycles
	{
		private static Dictionary<string, int> AssociateWithEdge(List<int> weights)
		{
			Dictionary<string, int> edgeWeights = new Dictionary<string, int>();

			edgeWeights.Add("a", weights[0]);
			edgeWeights.Add("b", weights[1]);
			edgeWeights.Add("c", weights[2]);
			edgeWeights.Add("d", weights[3]);
			edgeWeights.Add("e", weights[4]);
			edgeWeights.Add("f", weights[5]);

			return edgeWeights;
		}

		private static int CalculateP(Dictionary<string, int> edgeWeights)
		{
			// A -> C -> D -> A
			int cycle1Sum = edgeWeights["e"] + edgeWeights["d"] + edgeWeights["a"];
			int cycle1Min = Math.Min(edgeWeights["e"], Math.Min(edgeWeights["d"], edgeWeights["a"]));

			// A -> B -> D -> A
			int cycle2Sum = edgeWeights["f"] + edgeWeights["a"] + edgeWeights["b"];
			int cycle2Min = Math.Min(edgeWeights["f"], Math.Min(edgeWeights["a"], edgeWeights["b"]));

			// A -> B -> C -> D -> A
			int cycle3Sum = edgeWeights["b"] + edgeWeights["c"] + edgeWeights["d"] + edgeWeights["a"];
			int cycle3Min = Math.Min(edgeWeights["b"], Math.Min(edgeWeights["c"], 
			                         Math.Min(edgeWeights["d"], edgeWeights["a"])));

			int minCycles12 = Math.Min(cycle1Sum, cycle2Sum);
			int minCycleSum = Math.Min(cycle3Sum, minCycles12);

			if (minCycleSum < 0)
				return Math.Abs(minCycleSum);
			else
				return 0;
		}

		public static void Main(string[] args)
		{
			List<string> weightsInput = new List<string>(Console.ReadLine().Split());
			List<int> weights = new List<int>(weightsInput.ConvertAll(Int32.Parse));
			Dictionary<string, int> edgeWeights = AssociateWithEdge(weights);
			int p = CalculateP(edgeWeights);
			Console.WriteLine(p);
		}
	}
}

