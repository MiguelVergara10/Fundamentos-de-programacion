/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package ejercicios;

// Jesus Miguel Vergara Rodriguez 24040146
import java.util.Scanner;

public class Ejercicio2 {

    // Función para calcular el área de un círculo
    public static double calcularArea(double radio) {
        return Math.PI * Math.pow(radio, 2);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Ingresa el radio del circulo: ");
        double radio = scanner.nextDouble();

        if (radio > 0) {
            double area = calcularArea(radio);
            System.out.printf("El area del circulo con radio %.2f es: %.2f%n", radio, area);
        } else {
            System.out.println("Por favor, ingresa un numero valido mayor que 0.");
        }

        scanner.close();
    }
}
