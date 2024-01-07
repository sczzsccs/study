/*using global::System;
using global::System.Collections.Generic;
using global::System.IO;
using global::System.Linq;
using global::System.Net.Http;
using global::System.Threading;
using global::System.Threading.Tasks;*/

namespace ConsoleApp1
{
    // 상속과 다형성, 추상메소드, 추상클래스
    class MyClass
    {
        public MyClass() { }

        private string? _name;
        public string? name { get => _name; set => _name = value; }
        public virtual void Print_name() { } //가상메소드
    }

    class MyClass_Son : MyClass
    {
        public MyClass_Son()
        { Console.WriteLine("Hello, MyClass_Son!"); }
        public override void Print_name() { Console.WriteLine("MyClass_Son name:"+name); }
    }

    internal class Program
    {
        private static void Main(string[] args)
        {
            MyClass MyCC = new MyClass_Son();
            MyCC.name = Console.ReadLine();
            MyCC.Print_name();
        }
    }
}