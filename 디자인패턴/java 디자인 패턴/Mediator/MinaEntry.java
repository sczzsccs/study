import java.util.Scanner;

public class MinaEntry {
    public static void main(String[] args) {
        SmartHome smartHome = new SmartHome();
        
        try(Scanner scanner = new Scanner(System.in)) {
            do{
                smartHome.report();

                System.out.println("[1] 문 열기");
                System.out.println("[2] 문 닫기");
                System.out.println("[3] 창문 열기");
                System.out.println("[4] 창문 닫기");
                System.out.println("[5] 에어컨 켜기");
                System.out.println("[6] 에어컨 끄기");
                System.out.println("[7] 보일러 켜기");
                System.out.println("[8] 보일러 끄기");

                System.out.println("명령: ");
                int i = scanner.nextInt();
                System.out.println("\n");

                switch (i) {
                    case 1:
                        smartHome.door.Open();
                        System.out.println("입력된 명령: "+smartHome.door);
                        break;
                    case 2:
                        smartHome.door.Close();
                        System.out.println("입력된 명령: "+smartHome.door);
                        break;
                    case 3:
                        smartHome.window.Open();
                        System.out.println("입력된 명령: "+smartHome.window);
                        break;
                    case 4:
                        smartHome.window.Close();
                        System.out.println("입력된 명령: "+smartHome.window);
                        break;
                    case 5:
                        smartHome.aircond.On();
                        System.out.println("입력된 명령: "+smartHome.aircond);
                        break;
                    case 6:
                        smartHome.aircond.Off();
                        System.out.println("입력된 명령: "+smartHome.aircond);
                        break;
                    case 7:
                        smartHome.boiler.On();
                        System.out.println("입력된 명령: "+smartHome.boiler);
                        break;
                    case 8:
                        smartHome.boiler.Off();
                        System.out.println("입력된 명령: "+smartHome.boiler);
                        break;
                    default: System.out.println("Error! 잘못된 명령");
                        break;
                }
            }while(true);
        }
    }
}