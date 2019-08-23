package Polymorphism;

/**
 * Created by IntelliJ IDEA.
 * User: leopuglia
 * Date: 17/06/2019
 * Time: 13:27
 */

class Movie {
    private String name;

    public Movie(String name) {
        this.name = name;
    }

    public String plot() {
        return "No plot here";
    }

    public String getName() {
        return name;
    }
}

class Jaws extends Movie {
    public Jaws() {
        super("Jaws");
    }
//
//    public Jaws(String name) {
//        super(name);
//    }

    public String plot() {
        return "A shark eats lots of people";
    }
}

class IndependenceDay extends Movie {
    public IndependenceDay() {
        super("Independence Day");
    }

    @Override
    public String plot() {
        return "Aliens attempt to take over earth";
    }
}

class Forgetable extends Movie {
    public Forgetable() {
        super("Forgetable");
    }

    // no plot method
}

public class Main {
    public static void main(String[] args) {

        for (int i = 1; i<6; i++) {
            Movie movie = randomMovie();
            System.out.println("Movie #" + i + " : " +movie.getName()+ "\n" +
                                                "Plot: " + movie.plot()+ "\n");
        }

    }

    public static Movie randomMovie() {
        int randomNumber = (int) (Math.random()* 3) + 1;
        System.out.println("Random number was: " +randomNumber);
        switch (randomNumber) {
            case 1:
                return new Jaws();
            case 2:
                return new IndependenceDay();

            case 3:
                return new Forgetable();
        }

        return null;
    }
}