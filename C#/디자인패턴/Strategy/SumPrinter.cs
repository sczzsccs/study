public class SumPrinter {
    public void Printer(SumStrategy strategy, int N) { 
        Console.WriteLine("The Sum of 1 - "+ N.ToString()+':'+strategy.get(N).ToString());
    }
}