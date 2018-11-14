package com.leopuglia;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

//        int min = Integer.MIN_VALUE;
//        int max = Integer.MAX_VALUE;
        
        Scanner scanner = new Scanner(System.in);

        System.out.println("Enter our year of birth: ");
        boolean hasNextInt = scanner.hasNextInt(); //verify if next read is an int
        if (hasNextInt) {

            int yearOfBirth = scanner.nextInt();
            scanner.nextLine(); // handle next line character (enter)

            System.out.println("Enter our name: ");
            String name = scanner.nextLine();
            int age = 2018 - yearOfBirth;
            if (age >= 0 && age <= 100){
                System.out.println("Your name is: " + name + ", and you are " + age + " years old");

            } else {
                System.out.println("Invalid age");
            }
        } else {
            System.out.println("Unable to parse year of birth");
        }

        scanner.close();

	}
}
