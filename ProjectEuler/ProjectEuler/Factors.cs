using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ProjectEuler
{
    public static partial class Answers
    {
        private static IEnumerable<int> GetFactors(long number)
        {
            var sqrt = (int)Math.Sqrt(number);
            for (var i = 2; i <= sqrt; i++)
            {
                if (number % i == 0) yield return i;
            }
        }
    }
}
