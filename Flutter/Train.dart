class Person {
  final String name;
  int num;
  Person(this.name, this.num);

  void SayName() {
    print("My name is ${name} and number ${num}.");
  }
}

class Girl extends Person {
  Girl(super.name, super.num);
  // void SayName() => print("Girl name is ${name}.");
  void SayName(){
    super.SayName();
  }
}

void main() {
  Person girl = Girl("영희", 4);
  girl.SayName();
}