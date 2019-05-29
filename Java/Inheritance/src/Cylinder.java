/**
 * Created by IntelliJ IDEA.
 * User: leopuglia
 * Date: 28/05/2019
 * Time: 23:17
 */

public class Cylinder extends Circle {

    private double height;

    public Cylinder(double radius, double height) {
        super(radius);
        this.height = (height < 0) ? 0 : height;
    }

    public double getVolume() {
        double volume = getArea()*height;
        return volume;
    }

    public double getHeight() {
        return height;
    }

    public void setHeight(double height) {
        this.height = height;
    }
}
