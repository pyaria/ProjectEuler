using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ProjectEuler
{
    public static partial class Answers
    {
        private static int GetLargestPrimeFactor(long parentNumber)
        {
            return GetFactors(parentNumber).Where(IsPrime).Last();
        }
        private static bool IsPrime(int number)
        {
            return !GetFactors(number).Any();
        }
    }
}
