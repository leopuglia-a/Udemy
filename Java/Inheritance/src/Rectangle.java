/**
 * Created by IntelliJ IDEA.
 * User: leopuglia
 * Date: 28/05/2019
 * Time: 23:22
 */

public class Rectangle {

    private double width;
    private double length;

    public Rectangle(double width, double length) {
        this.width = (width < 0) ? 0 : width;
        this.length = (length < 0) ? 0 : length;
    }

    public double getArea() {
        double area = this.width * this.length;
        return area;
    }

    public double getWidth() {
        return width;
    }

    public double getLength() {
        return length;
    }
}
