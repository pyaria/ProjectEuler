using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ProjectEuler
{
    public static partial class Answers
    {
        private static bool IsPalindrome(int number)
        {
            var str = number.ToString();
            return str == string.Join("", str.Reverse());
        }
    }
}
