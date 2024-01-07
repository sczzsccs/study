import java.util.LinkedList;

public abstract class DiceGame {
    protected LinkedList<Player> players = new LinkedList<Player>();

    public void addPlayer(Player player) {
        players.add(player);
    }

    public abstract void Play();
}
