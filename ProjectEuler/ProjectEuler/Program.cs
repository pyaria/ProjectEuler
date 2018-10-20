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
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.";
                default: return $"No description has been entered for problem #{problemNo} yet";
            }
        }

        private static object GetAnswer(int problemNo)
        {
            switch (problemNo)
            {
                case 1:
                    {
                        return RunProblem1();
                    }
                default: return "Problem not yet solved/implemented/in system";
            }
        }

        private static int RunProblem1()
        {
            var multiplesOf3 = GetMultiplesBelowANumber(3, 1000);
            Console.WriteLine(string.Join(", ", multiplesOf3));
            var multiplesOf5 = GetMultiplesBelowANumber(5, 1000);
            Console.WriteLine(string.Join(", ", multiplesOf5));
            var distinct = multiplesOf3.Concat(multiplesOf5).Distinct();
            return distinct.Sum();
        }
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
