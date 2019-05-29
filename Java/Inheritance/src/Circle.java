/**
 * Created by IntelliJ IDEA.
 * User: leopuglia
 * Date: 28/05/2019
 * Time: 23:14
 */

public class Circle {
    private double radius;

    public Circle(double radius) {
        this.radius = (radius < 0) ? 0 : radius;
    }

    public double getArea() {
        double area = radius*radius*Math.PI;
        return area;
    }

    public double getRadius() {
        return radius;
    }

    public void setRadius(double radius) {
        this.radius = radius;
    }
}
