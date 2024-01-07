public class SimpleSumStrategy : SumStrategy
{
    public int get(int N)
    {
        int sum = 0;
        for (int i = 0; i <= N; i++) {
            sum+=i;
        }
        return sum;
    }
}