package Composition;

/**
 * Created by IntelliJ IDEA.
 * User: leopuglia
 * Date: 07/06/2019
 * Time: 17:10
 */

public class Motherboard {

    private String model;
    private String manufacturer;
    private int ramSlots;
    private int cadSlots;
    private String bios;

    public Motherboard(String model, String manufacturer, int ramSlots, int cadSlots, String bios) {
        this.model = model;
        this.manufacturer = manufacturer;
        this.ramSlots = ramSlots;
        this.cadSlots = cadSlots;
        this.bios = bios;
    }

    public void loadProgram(String programName) {
        System.out.println("Program " +programName + " is now loading...");
    }

    public String getModel() {
        return model;
    }

    public void setModel(String model) {
        this.model = model;
    }

    public String getManufacturer() {
        return manufacturer;
    }

    public void setManufacturer(String manufacturer) {
        this.manufacturer = manufacturer;
    }

    public int getRamSlots() {
        return ramSlots;
    }

    public void setRamSlots(int ramSlots) {
        this.ramSlots = ramSlots;
    }

    public int getCadSlots() {
        return cadSlots;
    }

    public void setCadSlots(int cadSlots) {
        this.cadSlots = cadSlots;
    }

    public String getBios() {
        return bios;
    }

    public void setBios(String bios) {
        this.bios = bios;
    }
}

