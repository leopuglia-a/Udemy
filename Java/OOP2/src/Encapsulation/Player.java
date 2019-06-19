package Encapsulation;

/**
 * Created by IntelliJ IDEA.
 * User: leopuglia
 * Date: 14/06/2019
 * Time: 11:34
 */

public class Player {

    public String fullName;
    public int health;
    public String weapon;

    public void loseHealth(int damage) {
        this.health = this.health - damage;
        if (this.health <= 0) {
            System.out.println("Player died");
        }
    }

    public int healthRemaining() {
        return  this.health;
    }
}
