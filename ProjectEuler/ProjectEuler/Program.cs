using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ProjectEuler
{
    class Program
    {
        static void Main(string[] args)
        {
            var problemNo = int.Parse(args[0]);
            var question = GetQuestion(problemNo);
            var answer = GetAnswer(problemNo);
            Console.WriteLine(question);
            Console.WriteLine(answer);
            Console.Read();
        }

        private static string GetQuestion(int problemNo)
        {
            switch (problemNo)
            {
                case 1: return $@"If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
\nThe sum of these multiples is 23.\nFind the sum of all the multiples of 3 or 5 below 1000.";
                default: return $"No description has been entered for problem #{problemNo} yet";
            }
        }

        private static object GetAnswer(int problemNo)
        {
            switch (problemNo)
            {
                case 1:
                    {
                        return RunMultiplesOf3And5();
                    }
                default: return "Problem not yet solved/implemented/in system";
            }
        }

        private static int RunMultiplesOf3And5()
        {
            throw new NotImplementedException();
        }
    }
}
