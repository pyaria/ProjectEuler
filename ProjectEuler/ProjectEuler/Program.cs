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
            var question = Questions.GetQuestion(problemNo);
            var answer = GetAnswer(problemNo);
            Console.WriteLine(question);
            Console.WriteLine(answer);
            Console.Read();
        }
        private static object GetAnswer(int problemNo)
        {
            switch (problemNo)
            {
                case 1: return RunProblem1();
                case 2: return RunProblem2();
                case 3: return RunProblem3();
                default: return "Problem not yet solved/implemented/in system";
            }
        }

        private static int RunProblem3()
        {
            throw new NotImplementedException();
        }

        private static int RunProblem2()
        {
            var fibonnaciSeq = GetEvenFibonnaci(4000000);
            return fibonnaciSeq.Sum();
        }
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
