public class Acter
{
    int id;
    string name;
    string weapon;
    float strength;
    int level;

    string Talk() { return "��ȭ�� �ɾ����ϴ�."; }

    string HasWeapon() { return weapon; }

    void Level_Up() { level += 1; }
}