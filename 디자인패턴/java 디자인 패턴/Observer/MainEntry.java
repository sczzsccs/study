public class MainEntry {
    public static void main(String[] args) {
        DiceGame diceGame = new UnfairDiceGame();
        
        Player player1 = new EvenBettingPlayer("짝궁댕이");
        Player player2 = new nBettigPlayer("홀아비", 3);
        Player player3 = new OddBettingPlayer("홀쭉이");
        
        diceGame.addPlayer(player1);
        diceGame.addPlayer(player2);
        diceGame.addPlayer(player3);

        diceGame.Play();
    }
}