public class Main {
    public static void main(String[] args) {
//        Animal animal = new Animal("Animal", 1, 1, 5, 5);
//
//        Dog dog = new Dog("Yorkee", 8, 20, 2, 4, 1, 20, "Long silky");
//
//        dog.eat();
////        dog.walk();
//        dog.run();

//        Challenge
//        Start with a base class of Vehicle, then create a Car class that inherits from its base class.
//        Finally, create another class, a specific type of Car that inherits from the car class.
//        You should be able to hand steering, changing gears, and moving (speed in other words).
//        You will want to decide where to put the appropriate state and behaviours (fields and methods).
//        As mentioned above, changing gears, increasing/decreasing speed should be included.
//        For you specific type of vehicle you will want to add something specific for that type of car.

        Outlander outlander = new Outlander(36);
        outlander.steer(45);
        outlander.accelerate(30);
        outlander.accelerate(20);
        outlander.accelerate(-42);

    }
}
