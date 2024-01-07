public class nBettigPlayer extends Player {
    private int n;
    protected nBettigPlayer(String name, int Num) {
        super(name);
        n = Num;
    }

    @Override
    protected void ProcessDiceBetting(int Dice_Num) {
        System.out.println("\nPlayer: " + getPlayer_name());
        if (Dice_Num == n) System.out.println("You Win!");
        else System.out.println("You Lose!");
    }
}