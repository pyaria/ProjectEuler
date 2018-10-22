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
                default: return "Problem not yet solved/implemented/in system";
            }
        }
        private static int RunProblem1() => GetMultiplesBelowANumber(3, 1000)
            .Concat(GetMultiplesBelowANumber(5, 1000))
            .Distinct()
            .Sum();
        private static int RunProblem2() => GetEvenFibonnaci(4000000).Sum();
        private static int RunProblem3() => GetLargestPrimeFactor(600851475143);
        private static int RunProblem4() => GetDistinctMultiples(100, 1000).Where(IsPalindrome).Max();
        private static int RunProblem5() => GetLowestCommonMultipleForVariableInts(Enumerable.Range(1, 20).ToArray());
    }
}
