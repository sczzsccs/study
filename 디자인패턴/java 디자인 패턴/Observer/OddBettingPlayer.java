public class OddBettingPlayer extends Player {
    protected OddBettingPlayer(String name) {
        super(name);
    }

    @Override
    protected void ProcessDiceBetting(int Dice_Num) {
        System.out.println("\nPlayer: " + getPlayer_name());
        if (Dice_Num%2==1) System.out.println("Win!");
        else System.out.println("Lose!");
    }  
}