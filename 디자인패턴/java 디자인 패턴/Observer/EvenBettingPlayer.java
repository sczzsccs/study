public class EvenBettingPlayer extends Player {
    protected EvenBettingPlayer(String name) {
        super(name);
    }

    @Override
    protected void ProcessDiceBetting(int Dice_Num) {
        System.out.println("\nPlayer: " + getPlayer_name());
        if (Dice_Num%2==0) System.out.println("Win!");
        else System.out.println("Lose!");
    }
}
