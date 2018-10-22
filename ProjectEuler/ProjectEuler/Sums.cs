using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ProjectEuler
{
    public static partial class Answers
    {
        private static double GetSumOfSquares(int startNum, int endNum) 
            => Enumerable.Range(startNum, endNum)
                .Select(e => Math.Pow(e, 2))
                .Sum();
        private static double GetSquareOfSums(int startNum, int endNum)
            => Math.Pow(Enumerable.Range(startNum, endNum).Sum(), 2);
    }
}
