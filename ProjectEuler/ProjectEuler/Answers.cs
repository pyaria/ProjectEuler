using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ProjectEuler
{
    public static partial class Answers
    {
        public static object GetAnswer(int problemNo)
        {
            switch (problemNo)
            {
                case 1: return RunProblem1();
                case 2: return RunProblem2();
                case 3: return RunProblem3();
                case 4: return RunProblem4();
                case 5: return RunProblem5();
                case 6: return RunProblem6();
                case 7: return RunProblem7();
                default: return "Problem not yet solved/implemented/in system";
            }
        }
        private static int RunProblem1() => GetMultiplesBelowANumber(3, 1000)
            .Concat(GetMultiplesBelowANumber(5, 1000))
            .Distinct()
            .Sum();
        private static int RunProblem2(int fibonnaciUpTo = 4000000) => GetEvenFibonnaci(fibonnaciUpTo).Sum();
        private static int RunProblem3(long number = 600851475143) => GetLargestPrimeFactor(number);
        private static int RunProblem4(int startNumber = 100, int endNumber = 1000) 
            => GetDistinctMultiples(startNumber, endNumber)
            .Where(IsPalindrome)
            .Max();
        private static int RunProblem5(int startNumber = 1, int endNumber = 20) 
            => GetLowestCommonMultipleForVariableInts(Enumerable.Range(startNumber, endNumber).ToArray());
        private static long RunProblem6(int startNumber = 1, int endNumber = 100) 
            => (long)(GetSquareOfSums(startNumber, endNumber) - GetSumOfSquares(startNumber, endNumber));
        private static int RunProblem7(int nthPrime = 10001) => GetNthPrime(nthPrime);
    }
}
