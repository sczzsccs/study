public class SmartHome implements Mediator {
    public Door door = new Door(this);
    public Window window = new Window(this);
    public CoolAircon aircond = new CoolAircon(this);
    public HeatBoiler boiler = new HeatBoiler(this);


    @Override
    public void participantChange(Participant participant) {
        if((participant == door && door.isDoor()) || 
                (participant == window && window.isWindow())) {
            aircond.Off();
            boiler.Off();
        }
        else if(participant == aircond && aircond.isRunning()) {
            boiler.Off();
            window.Close();
            door.Close();
        }
        else if(participant == boiler && boiler.isRunning()) {
            aircond.Off();
            window.Close();
            door.Close();
        }
    }

    public void report() {
        System.out.println("[집안 상태]");
        System.out.println(door);
        System.out.println(window);
        System.out.println(aircond);
        System.out.println(boiler);
        System.out.println();
    }
}