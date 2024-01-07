import java.util.Iterator;
import java.util.Random;

public class UnfairDiceGame extends DiceGame {
    @Override
    public void Play() {
        Random randint = new Random();
        Iterator<Player> iter = players.iterator();
        int dice_Num = randint.nextInt(20)+1;
        if(dice_Num>6) dice_Num = 4;
        System.out.println("Current Dice Num: " + dice_Num);
        while (iter.hasNext()) iter.next().ProcessDiceBetting(dice_Num);
    }
    
}
