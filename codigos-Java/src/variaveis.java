public class variaveis {

    public static void main(String[] args){

        /* Variable: a reusable container for a value
        *            a variable behaves as if it was the value it contains.
        *
        *  Primitive: simple value stored directly in memory (stack)
        *  Reference: memory address (stack) that points to the (heap)
        *
        *  --- Primitive VS Reference ---
        *      ---------    ---------
        *      int          string
        *      double       array
        *      char         object
        *      boolean
        *
        *  There are two steps in order to create a variable:
        *  1. Declaration (like in C, for example)
        *  2. Assignment
        *
        * */

        // Primitive Variables //

        int age = 30; // "int" only accepts whole numbers
        int year = 2025;
        int quantity = 1;

        double price = 19.99; // "double" accept both whole and decimals up to 308 cases. (1e-308).
        double gpa = 3.5;
        double temperature = -12.5; // also accepts negative fluctuating numbers too

        char grade = 'A'; // needs to be between single quotes ' '.
        char symbol = '!'; // "char" is a one-character long type of variable.
        char currency = '$';

        boolean isStudent = false; // can store both true and false statements
        boolean forSale = false; // typically used internally (e.g. if/else statements).
        boolean isOnline = true;

        // Here are some prints to test these primitive variables:

        System.out.println("The year is: " + year); // use plus + to concat
        System.out.println("The price is: " + price);
        System.out.println("Your grade is: " + grade);
        System.out.println("Are you online? " + isOnline);

        // Reference Variables //

        String name = "Lucas"; // Needs to be between double quotes " ".
        String food = "Burger";
        String email = "email12345@example.com"; // Accepts number digits too!
        String car = "Koenigsegg";
        String color = "Blue";

        System.out.println("\n Your email is: " + email);
        System.out.println("You are " + age + " years old");
        System.out.println("My favorite car is: " + car);

        int quantidade = 100;
        double preco = 29.99;
        String moeda = "R$";
        String produto = "Notebook";

        System.out.println("\nO produto é: " + produto + ";\nO preço dele é: " + moeda + preco + ";\nE " + quantidade + " quantidades estão a venda.");
    }
}
