// See https://aka.ms/new-console-template for more information
Item[] items = {
    new Item(name:"CPU", cost:1000),
    new Item(name:"Keyboard", cost:2000),
    new Item(name:"Mouse", cost:3000),
    new Item(name:"CPU", cost:50)
};

Array array = new Array(items);
Iterator it = array.iterator();

while (it.next())
{
    Item Ones = (Item)it.current();
    Console.WriteLine(Ones.Str_Convert());
}