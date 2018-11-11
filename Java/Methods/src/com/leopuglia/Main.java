package com.leopuglia;

public class Main {

    public static void main(String[] args) {
        boolean gameOver = true;
        int score = 800;
        int levelCompleted = 5;
        int bonus = 100;
        int result;
        int position;

        result = calculateScore(gameOver,score,levelCompleted,bonus);
        System.out.println("Your final score was: " + result);

        score = 10000;
        levelCompleted = 8;
        bonus = 200;

        result = calculateScore(gameOver,score,levelCompleted,bonus);
        System.out.println("Your final score was: " + result);

        position = calculateHighScorePosition(1500);
        displayHighScorePosition("Leo", position);

        position = calculateHighScorePosition(900);
        displayHighScorePosition("Tim", position);

        position = calculateHighScorePosition(400);
        displayHighScorePosition("Percy", position);

        position = calculateHighScorePosition(50);
        displayHighScorePosition("Gilbert", position);
    }

    public static int calculateScore(boolean gameOver, int score, int levelCompleted, int bonus) {

        if (gameOver) {
            int finalScore = score + (levelCompleted * bonus);
            finalScore += 2000;

            return finalScore;
        } else {
            return -1;
        }
    }

    public static void displayHighScorePosition(String name, int position) {
        System.out.println("Player " + name + " managed to get into position " +
                position + " on the high score table");
    }

    public static int calculateHighScorePosition(int score) {
        if (score >= 1000) {
            return 1;
        }else if (score >= 500) {
            return 2;
        }else if (score >= 100) {
            return 3;
        } else {
            return 4;
        }
    }

}