using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ProjectEuler
{
    public static partial class Answers
    {
        private static int MultipleNumbers(IEnumerable<int> numbers)
        {
            var multiple = numbers.First();
            foreach (var number in numbers.Skip(1))
            {
                multiple *= number;
            }
            return multiple;
        }
        private static IEnumerable<int> GetMultiplesBelowANumber(int multiplesOfNumber, int belowThisNumber)
        {
            var i = 1;
            while (i * multiplesOfNumber < belowThisNumber)
            {
                yield return i * multiplesOfNumber;
                i++;
            }
        }
        private static IEnumerable<int> GetDistinctMultiples(int startNumber, int endNumber)
        {
            return Enumerable.Range(startNumber, endNumber - startNumber)
                .Reverse()
                .SelectMany(e => TraverseMultiples(startNumber, e));
        }
        private static IEnumerable<int> TraverseMultiples(int startNumber, int endNumber)
        {
            for (var i = endNumber; i >= startNumber; i--)
            {
                yield return endNumber * i;
                if (startNumber == i) break;
            }
        }
        private static int GetLowestCommonMultipleForVariableInts(params int[] ints)
        {
            return ints.Aggregate((currentMultiple, nextNumber) => GetLowestCommonMultipleForTwoInts(currentMultiple, nextNumber));
        }
        private static int GetLowestCommonMultipleForTwoInts(int a, int b)
        {
            var multipleA = a;
            var multipleB = b;
            while (multipleA != multipleB)
            {
                if (multipleA > multipleB) multipleB += b;
                else multipleA += a;
            }
            return multipleA;
        }
    }
}
