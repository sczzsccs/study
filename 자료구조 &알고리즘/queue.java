import java.util.LinkedList;
// import java.util.Queue;

public class queue {
    static class Queue {
        private LinkedList<Integer> queue = new LinkedList<>();
        void enQueue(int n) {
            queue.add(n);
        }
        int deQueue () {
            return queue.poll();
        }
    };

    public static void main(String[] args) {
        Queue queue = new Queue();
        queue.enQueue(10);
        queue.enQueue(7);
        queue.enQueue(8);
        
        System.out.println(queue.deQueue());
        System.out.println(queue.deQueue());
        System.out.println(queue.deQueue());
    }

    public static void enQueue(int i) {
    }
}