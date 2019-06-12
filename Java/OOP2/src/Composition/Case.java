package Composition;

import java.awt.*;

/**
 * Created by IntelliJ IDEA.
 * User: leopuglia
 * Date: 07/06/2019
 * Time: 17:20
 */

public class Case {

    private String model;
    private String manufacturer;
    private String powerSupply;
    private Dimensions dimensions;

    public Case(String model, String manufacturer, String powerSupply, Dimensions dimensions) {
        this.model = model;
        this.manufacturer = manufacturer;
        this.powerSupply = powerSupply;
        this.dimensions = dimensions;
    }

    public void pressPowerButton() {
        System.out.println("Power button pressed");
    }
}
