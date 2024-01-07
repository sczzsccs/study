public class DigitFactory {
    private Digit[] pool = new Digit[] {
        null, null, null, null, null, null,
        null, null, null, null, null, null
    };

    public Digit getDigit(int n) {
        if(pool[n] != null) {
            return pool[n];
        }
        else {
            String filename = String.format(".\\deta\\%d.txt", n);
            Digit digit = new Digit(filename);
            pool[n] = digit;
            return digit;
        }
    }
}
