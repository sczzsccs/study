﻿public class Item {
    private String name;
    private int cost;
    public Item(String name, int cost) {
        this.name = name;
        this.cost = cost;
    }
    public String Str_Convert() {
        return "(" + name + ", " + cost.ToString() + ")";
    }
}