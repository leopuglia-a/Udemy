package com.leopuglia;

public class Main {
    public static void main(String[] args) {

        calculateScore("Leo", 500);
        calculateScore(300);

        calcFeetAndInchesToCentimeters(-6,5);
        calcFeetAndInchesToCentimeters(5);

    }

    public static double calcFeetAndInchesToCentimeters(double feet, double inches) {
        if (feet < 0 || inches < 0 || inches > 12) {
            System.out.println("Invalid feet or inches");
            return -1;
        } else {
            double centimeters = (feet * 12) * 2.54;
            centimeters += inches * 2.54;
            System.out.println(feet + " feet, " + inches + " inches = " + centimeters + " cm");
            return centimeters;
        }
    }

    public static double calcFeetAndInchesToCentimeters(double inches) {
        if (inches < 0) {
            System.out.println("Invalid inches");
            return -1;
        } else {
            double feet = (int) inches /12;
            double remInches = (int) inches % 12;
            System.out.println(inches + " inches = " + feet + " feet and " + remInches + "inches");
            return calcFeetAndInchesToCentimeters(feet,remInches);
        }

    }

    public static int calculateScore(String playerName, int score) {
        System.out.println("Player " + playerName + " scored " + score + " points");
        return score * 1000;
    }

    public static int calculateScore(int score) {
        System.out.println("Unnamed player scored " + score + " points");
        return score * 1000;
    }

    public static int calculateScore() {
        System.out.println("No player name, no player score");
        return 0;
    }
}
