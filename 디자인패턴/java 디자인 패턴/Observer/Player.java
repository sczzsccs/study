abstract class Player {
    private String name;
    protected Player(String name) {
        this.name = name;
    }

    protected  String getPlayer_name() {
        return name;
    };
    protected abstract void ProcessDiceBetting(int Dice_Num);
}