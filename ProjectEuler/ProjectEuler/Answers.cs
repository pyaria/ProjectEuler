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
                default: return "Problem not yet solved/implemented/in system";
            }
        }
        private static int RunProblem1()
        {
            var multiplesOf3 = GetMultiplesBelowANumber(3, 1000);
            var multiplesOf5 = GetMultiplesBelowANumber(5, 1000);
            var distinct = multiplesOf3.Concat(multiplesOf5).Distinct();
            return distinct.Sum();
        }
        private static int RunProblem2()
        {
            var fibonnaciSeq = GetEvenFibonnaci(4000000);
            return fibonnaciSeq.Sum();
        }
        private static int RunProblem3()
        {
            return GetLargestPrimeFactor(600851475143);
        }
    }
}
