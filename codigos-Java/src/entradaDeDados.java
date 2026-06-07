import java.util.Scanner;

public class entradaDeDados {

    public static void main(String[] args){

        /* In Java, to accept user input, you'll need to use a Scanner.
        *
        *  A Scanner is a simple text scanner that parses primitive types and strings
        *  However, in order to use it, you need to import the following:
        *  'import java.util.Scanner' at the very top.
        *
        * */

        Scanner scanner = new Scanner(System.in);

        System.out.println("Enter your name: ");
        String name = scanner.nextLine();

        System.out.println("Hello " + name);

        System.out.println("Enter your age: ");
        String age = scanner.nextLine();

        System.out.println("Your age is " + age);

        scanner.close(); // Always set this .close() function at the end, or it could lead to unexpected behavior
    }
}
