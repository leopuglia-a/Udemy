package com.leopuglia;

public class Main {

    public static void main(String[] args) {
        double a = 20;
        double b = 80;
        double c;
        double rem;

        c = (a + b) * 25;

        rem = c % 40;

        if (rem <= 20) {
            System.out.println("Total was over the limit");
        }
    }
}
