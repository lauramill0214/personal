import java.util.Random;
import java.util.Scanner;

public class GuessingGame {
    public static void main(String[] args) {
        Random random = new Random();
        int number = random.nextInt(100) + 1;
        int guess = 0;
        int count = 0;
        Scanner scanner = new Scanner(System.in);
        
        while (guess != number) {
            System.out.print("Guess a number between 1 and 100: ");
            guess = scanner.nextInt();
            count++;
            
            if (guess < number) {
                System.out.println("Too low");
            } else if (guess > number) {
                System.out.println("Too high");
            } else {
                System.out.println("You win!");
                System.out.println("Number of guesses: " + count);
            }
        }
        
        scanner.close();
    }
}
