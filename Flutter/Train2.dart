// class Prod{
//   late String name;
//   late int price;
// }

// void main() {
//   Prod product = new Prod();
//   product.name = "감자";
//   product.price = 2000;
// }

// 추상 클래스
abstract class Unit{
  String? name;
  num? ATK, AtSpd, HP, MP, MovSpd, Def, Res, Dis;

  void PrintStats() {}
}

class Champion extends Unit{
  Champion(name, ATK, AtSpd, HP, MP, MovSpd, Def, Res, Dis) {
    this.name = name;
    this.ATK = ATK;
    this.AtSpd = AtSpd;
    this.HP = HP;
    this.MP = MP;
    this.MovSpd = MovSpd;
    this.Def = Def;
    this.Res = Res;
    this.Dis = Dis;
  }

  @override
  void PrintStats() {
    print("챔피언 이름 : ${this.name}");
    print("공격력 : ${this.ATK}");
    print("공격속도 : ${this.AtSpd}");
    print("체력 : ${this.HP}");
    print("마나 : ${this.MP}");
    print("이동속도 : ${this.MovSpd}");
    print("방어력 : ${this.Def}");
    print("마법저항력 : ${this.Res}");
    print("사거리 : ${this.Dis}");
  }
}

/* class Champion implements Unit{ //추상 클래스 상속
  @override
  String? name;
  @override
  num? ATK, AtSpd, HP, MP, MovSpd, Def, Res, Dis;

  Champion(name, ATK, AtSpd, HP, MP, MovSpd, Def, Res, Dis) {
    this.name = name;
    this.ATK = ATK;
    this.AtSpd = AtSpd;
    this.HP = HP;
    this.MP = MP;
    this.MovSpd = MovSpd;
    this.Def = Def;
    this.Res = Res;
    this.Dis = Dis;
  }

  @override
  void PrintStats() {
    print("챔피언 이름 : ${this.name}");
    print("공격력 : ${this.ATK}");
    print("공격속도 : ${this.AtSpd}");
    print("체력 : ${this.HP}");
    print("마나 : ${this.MP}");
    print("이동속도 : ${this.MovSpd}");
    print("방어력 : ${this.Def}");
    print("마법저항력 : ${this.Res}");
    print("사거리 : ${this.Dis}");
  }
}*/

void main() {
  Unit NuNu = new Champion("누누", 12.3, 15, 13, 1.44, 15.5, 7.1, 77, 8);
  NuNu.PrintStats();
}