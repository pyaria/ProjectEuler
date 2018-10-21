using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ProjectEuler
{
    public static partial class Answers
    {
        private static IEnumerable<int> GetEvenFibonnaci(int belowThisNumber)
        {
            var fibonnaciSeq = GetFibonnaciWhileLessThan(belowThisNumber);
            foreach (var term in fibonnaciSeq) if (term % 2 == 0) yield return term;
        }
        private static IEnumerable<int> GetFibonnaciWhileLessThan(int belowThisNumber)
        {
            yield return 1;
            yield return 2;
            var prevTwoAway = 1;
            var lastTerm = 2;
            var fibonnaciTerm = GetNextFibonnaciTerm(prevTwoAway, lastTerm);

            while (fibonnaciTerm < belowThisNumber)
            {
                yield return fibonnaciTerm;
                prevTwoAway = lastTerm;
                lastTerm = fibonnaciTerm;
                fibonnaciTerm = GetNextFibonnaciTerm(prevTwoAway, fibonnaciTerm);
            }
        }
        private static int GetNextFibonnaciTerm(int prevTwoAway, int lastTerm)
        {
            return prevTwoAway + lastTerm;
        }
    }
}
