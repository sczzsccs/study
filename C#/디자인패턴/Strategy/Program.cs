// See https://aka.ms/new-console-template for more information
// Console.WriteLine("Hello, World!");

SumPrinter sumPrinter = new SumPrinter();
sumPrinter.Printer(strategy:new SimpleSumStrategy(), N:10);
sumPrinter.Printer(strategy:new GaussSumStrategy(), N:10);