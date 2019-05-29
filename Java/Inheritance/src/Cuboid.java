/**
 * Created by IntelliJ IDEA.
 * User: leopuglia
 * Date: 28/05/2019
 * Time: 23:25
 */

public class Cuboid extends Rectangle {

    private double height;

    public Cuboid(double width, double length, double height) {
        super(width, length);
        this.height = (height < 0) ? 0 : height;
    }

    public double getVolume() {
        double volume = getArea() * this.height;
        return volume;
    }

    public double getHeight() {
        return height;
    }
}
