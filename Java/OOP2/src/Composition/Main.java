package Composition;

/**
 * Created by IntelliJ IDEA.
 * User: leopuglia
 * Date: 07/06/2019
 * Time: 17:15
 */

public class Main {
    public static void main(String[] args) {
        Dimensions dimensions = new Dimensions(20,2,5);
        Case theCase = new Case("220B", "Dell", "240", dimensions);

        Monitor theMonitor = new Monitor("27inch Beast", "Acer", 27, new Resolution(2540,1440));
        Motherboard theMotherboard = new Motherboard("BJ-200", "Asus", 4 , 6, "v2.44");

        PC thePC = new PC(theCase, theMonitor, theMotherboard);

        thePC.powerUp();
    }
}
