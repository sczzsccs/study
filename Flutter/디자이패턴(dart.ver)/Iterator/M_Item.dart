class M_Item {
  String _name = "";
  int _cost = 0;

  M_Item(String name, int cost){
    this._name = name;
    this._cost = cost;
  }

  @override
  String toString() {
    return "($_name, $_cost)";
  }
}