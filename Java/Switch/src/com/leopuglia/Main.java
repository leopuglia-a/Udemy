package com.leopuglia;

public class Main {

    public static void main(String[] args) {
	    int switchValue = 4;

	    switch (switchValue) {
            case 1:
                System.out.println("Value was 1");
                break;

            case 2: case 3: case 4:
                System.out.println("Was a 2, 3 or 4");
                break;

            default:
                System.out.println("Was not an option");
                break;
        }

        String month = "junE";

	    switch (month.toLowerCase()) {
            case "january" :
                System.out.println("Jan");
                break;

            case "june":
                System.out.println("Jun");
                break;

            default:
                System.out.println("Not sure");
                break;
        }
    }
}
