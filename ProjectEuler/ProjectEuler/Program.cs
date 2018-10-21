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
            var answer = Answers.GetAnswer(problemNo);
            Console.WriteLine(question);
            Console.WriteLine(answer);
            Console.Read();
        }
    }
}
