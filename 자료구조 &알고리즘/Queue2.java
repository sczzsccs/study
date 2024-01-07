import java.util.Scanner;
// import java.util.LinkedList;

public class Queue2 {
    static class Queue {
        private int front, rear, SIZE;
        private int[] queue;
        Queue(int SIZE) {
            front = rear = 0;
            this.SIZE = SIZE;
            queue = new int[SIZE];
        }

        void enQueue(int n) {
            if(front == rear && queue[rear]!=0) {
                System.out.println("큐가 꽉찼습니다.");
                return;
            }
            queue[rear] = n;
            rear++;
            rear %= SIZE;
        }

        int deQueue() {
            // 큐가 비어있는지 확인
            if (front == rear && queue[front] == 0) {
                System.out.println("큐가 비어있습니다.");
                return 0;
            }

            int n = queue[front];
            queue[front] = 0;
            front++;
            front %= SIZE;
            return n;
        }

        void ViewQueue() {
            System.out.println("----  원형 큐 상태 ----");

            System.out.print(queue[0]);
            for (int i = 1; i < SIZE; i++) {
                System.out.print(", "+queue[i]);
            }
            System.out.println();
        }
    };

    public static void main(String[] args) {
        // scanner 선언
        Scanner scanner = new Scanner(System.in);
        // 원형 큐 사이즈 입력
        System.out.print("큐의 사이즈 입력: ");
        int SIZE = scanner.nextInt();
        Queue SircleQueue = new Queue(SIZE);
        for (int i = 1; i < SIZE+4; i++) {
            SircleQueue.ViewQueue();
            SircleQueue.enQueue(i);
        }

        for (int i = 1; i < SIZE+4; i++) {
            System.out.println(SircleQueue.deQueue());
            SircleQueue.ViewQueue();
        }

        SircleQueue.enQueue(1);
        SircleQueue.ViewQueue();
        SircleQueue.enQueue(2);
        SircleQueue.ViewQueue();
        SircleQueue.enQueue(3);
        SircleQueue.ViewQueue();
        SircleQueue.enQueue(4);

        System.out.println(SircleQueue.deQueue());
        System.out.println(SircleQueue.deQueue());
        
        SircleQueue.enQueue(5);
        SircleQueue.ViewQueue();
        SircleQueue.enQueue(6);
        SircleQueue.ViewQueue();

        SircleQueue.ViewQueue();
    }
}
