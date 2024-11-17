package com.company;
public class Main {

    public static void main(String[] args ){

        //creating the necessary variables that u need to fill with the data u need / have
        double delta_t = 0.1 ;
        double time = 0.0;
        double y = 1.5;
        double v = 5.0;
        double a = -9.81;
        double ground = 0.0;

        System.out.println("| " + time + " sec | " + y + " m | " + v + " m/s | " + a + " m/s^2 |");

        //while Loop until the object hits the ground
        while(y > ground){
            time = time + delta_t;
            a = a;
            v = v + a * delta_t;
            y = y + v * delta_t;

            System.out.println("| " + time + " sec | " + y + " m | " + v + " m/s | " + a + " m/s^2 |");
        }
    }
}
