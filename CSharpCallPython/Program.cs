using IronPython.Hosting;
using Microsoft.Scripting.Hosting;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CSharpCallPython
{
    class Program
    {
        static void Main(string[] args)
        {
            ScriptEngine engine = Python.CreateEngine();
            ScriptScope scope = engine.CreateScope();

            ScriptSource script = engine.CreateScriptSourceFromFile(@"..\..\..\PythonApplication1\helloPython.py");

            scope.SetVariable("money1", 1500000);

            var result = script.Execute(scope);

            int b = scope.GetVariable("b");

            Console.WriteLine(b);
            Console.ReadKey();
        }
    }
}
