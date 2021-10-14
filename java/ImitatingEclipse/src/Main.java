/*
 * Sam Bacon
 * February 11, 2021
 * Classwork exercise #1 for CSC 335. This mimics the
 * Eclipse popup window when using an object
 */

import java.util.Scanner;
public class Main {

	public static void main(String[] args) {
		
		/* Create scanner and reflector */
		Scanner scnr = new Scanner(System.in);
		Reflection reflector = new Reflection();
		
		/* Take user input */
		System.out.print("Enter a class name: ");
		String className = scnr.next();
		
		/* Feed input into reflector */
		reflector.popup(className);
		
		scnr.close(); /* Close the scanner */
	}

}
