public class CoolAircon extends Participant {
    private boolean bOff = false;
    
    public CoolAircon(Mediator mediator) {
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
        if(bOff) return "# 에어컨: 켜짐";
        else return "# 에어컨: 꺼짐";
    }
}