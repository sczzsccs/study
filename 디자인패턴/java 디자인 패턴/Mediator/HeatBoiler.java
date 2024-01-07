public class HeatBoiler extends Participant {
    private boolean bOff = false;
    
    public HeatBoiler(Mediator mediator) {
        super(mediator);
    }

    public void On() {
        bOff = true;
        mediator.participantChange(this);
    }

    public void Off() {
        bOff = false;
        mediator.participantChange(this);
    }

    public boolean isRunning() {
        return bOff;
    }

    @Override
    public String toString() {
        if(bOff) return "# 보일러: 켜짐";
        else return "# 보일러: 꺼짐";
    }
}
