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
    }
}
