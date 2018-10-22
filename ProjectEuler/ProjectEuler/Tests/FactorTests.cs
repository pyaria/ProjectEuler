using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Xunit;

namespace ProjectEuler.Tests
{
    public class FactorTests
    {
        [Fact]
        public void FactorTest()
        {
            Assert.Equal("true", "false");
        }
        [Fact]
        public void NegativeTest()
        {
            Assert.False(true);
        }
    }
}
