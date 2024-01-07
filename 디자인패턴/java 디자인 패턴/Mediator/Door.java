public class Door extends Participant {
    private boolean bClosed = false;
    
    public Door(Mediator mediator) {
        super(mediator);
    }

    public void Open() {
        bClosed = true;
        mediator.participantChange(this);
    }

    public void Close() {
        bClosed = false;
        mediator.participantChange(this);
    }

    public boolean isDoor() {
        return bClosed;
    }

    @Override
    public String toString() {
        if(bClosed) return "# 문: 열림";
        else return "# 문: 닫힘";
    }
}