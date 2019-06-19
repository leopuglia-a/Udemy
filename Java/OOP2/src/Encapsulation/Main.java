package Encapsulation;

/**
 * Created by IntelliJ IDEA.
 * User: leopuglia
 * Date: 14/06/2019
 * Time: 11:32
 */

public class Main {
    public static void main(String[] args) {
//        Player player = new Player();
//
//        player.health = 100;
//        player.fullName = "Leo";
//        player.weapon = "Sword";
//
//        int damage = 10;
//        player.loseHealth(damage);
//        System.out.println("Remaining health = " + player.healthRemaining());

//        EnhancedPlayer player = new EnhancedPlayer("Leo", 200, "Sword");
//        System.out.println("initial heal is " + player.getHitPoints());

        Printer printer = new Printer(50, true);
        System.out.println("Initial page count = " +printer.getPagesPrinted());
        int pagesPrinted = printer.printPages(4);
        System.out.println("Pages printed was " + pagesPrinted + "new total print count = " +printer.getPagesPrinted());
        pagesPrinted = printer.printPages(6);
        System.out.println("Pages printed was " + pagesPrinted + "new total print count = " +printer.getPagesPrinted());

    }
}
