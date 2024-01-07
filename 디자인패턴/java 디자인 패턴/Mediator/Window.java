public class Window extends Participant {
    private boolean bClosed = false;
    
    public Window(Mediator mediator) {
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

    public boolean isWindow() {
        return bClosed;
    }

    @Override
    public String toString() {
        if(bClosed) return "# 창문: 열림";
        else return "# 창문: 닫힘";
    }
}
