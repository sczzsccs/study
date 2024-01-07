public class Acter
{
    int id;
    string name;
    string weapon;
    float strength;
    int level;

    string Talk() { return "대화를 걸었습니다."; }

    string HasWeapon() { return weapon; }

    void Level_Up() { level += 1; }
}