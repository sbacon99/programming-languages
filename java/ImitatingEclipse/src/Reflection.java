/*
 * Sam Bacon
 * February 11, 2021
 * Classwork exercise #1 for CSC 335. This is a support class
 * that takes the name of a class and prints the fields
 * and methods in a formatted list.
 */

import java.lang.reflect.*;
import java.util.ArrayList;
import java.util.Collections;
public class Reflection {

	public void popup(String className) {			

		Class<?> myClass;	
		
		try {
		// Returning METHODS
			
			// Initializing ArrayLists for S/F methods and non-S/F methods
			ArrayList<String> nsfMethods = new ArrayList<String>();
			ArrayList<String> sfMethods = new ArrayList<String>();

			
			// Getting methods
			myClass = Class.forName(className);								
			Method[] methodList = myClass.getMethods();

			
			// Iterating through each method...
			for(int i = 0; i < methodList.length; i++) {
				
				// Initialize method's output string
				String name = "";	
				
				// Getting modifiers...
				int modifiers = methodList[i].getModifiers();						
			
				// Check if it's static/final and update output
				if (Modifier.isStatic(modifiers)) {
				
					if (Modifier.isFinal(modifiers)) {
						name = "SF:";
					}
					else {
						name = "S:";	
					}
				}
				
				// Method name 
				String methodName = methodList[i].getName();
				name += methodName + "(";
				
				// Getting parameters
				Class<?>[] paramList = methodList[i].getParameterTypes();					
				
				// If the method has parameters, iterate through and add them to output string
				if(paramList.length > 0) {
					for(int j = 0; j < paramList.length; j++) {
						name += paramList[j] + " ";
					}			
				}
				
				name += ") : ";

				// Getting return type
				Class<?> returnType = methodList[i].getReturnType();
				name += returnType + " -";
				
				// Getting declaring class
				Class<?> declaringClass = methodList[i].getDeclaringClass();
				name += declaringClass.toString().replace("class", "");				
				
				// Add full string to appropriate arrayList
				
				if(name.startsWith("S:") || name.startsWith("SF:")) {
					sfMethods.add(name);
				}
				else {
					nsfMethods.add(name);
				}
				
			}
			
			// Sort arrayLists
			Collections.sort(sfMethods);
			Collections.sort(nsfMethods);

			// Printing
			System.out.println();
			System.out.println("-------- METHODS --------");
			System.out.println("(Non-Static/Non-Final)");
			System.out.println();
			
			for(int i = 0; i < nsfMethods.size(); i++) {   
			    System.out.println(nsfMethods.get(i));
			}
			
			System.out.println();
			System.out.println("-------- METHODS --------");
			System.out.println("(S = Static, F = Final, SF = Static and Final)");
			System.out.println();
			
			for(int n = 0; n < sfMethods.size(); n++) {   
			    System.out.println(sfMethods.get(n));
			}
			
		// Returning FIELDS
			
			// Initializing ArrayLists for S/F methods and non-S/F methods
			ArrayList<String> nsfFields = new ArrayList<String>();
			ArrayList<String> sfFields = new ArrayList<String>();
			
			Field[] fieldList = myClass.getFields();

			// Iterate through each field
			for(int i = 0; i < fieldList.length; i++) {
				
				// Initialize field's output string
				String name = "";
				
				// Getting modifiers
				int modifiers = fieldList[i].getModifiers();						
			
				// Check if it's static/final and update output
				if (Modifier.isStatic(modifiers)) {
				
					if (Modifier.isFinal(modifiers)) {
						name = "SF:";
					}
					else {
						name = "S:";	
					}
				}

				
				// Update output string with name, type, and declaring class
				name += " " + fieldList[i].getName()  + " : " + fieldList[i].getType() + 
						" - " + fieldList[i].getDeclaringClass().toString().replace("class", ""); 
				
				// Add full string to the appropriate ArrayList
				if(name.startsWith("S:") || name.startsWith("SF:")) {
					sfFields.add(name);
				}
				else {
					nsfFields.add(name);
				}				
			}
			
			// Sort arrayLists
			Collections.sort(sfFields);
			Collections.sort(nsfFields);
			
			// Printing
			System.out.println();
			System.out.println("-------- FIELDS --------");
			System.out.println("(Non-Static/Non-Final)");
			System.out.println();

			
			for(int j = 0; j < nsfFields.size(); j++) {   
			    System.out.println(nsfFields.get(j));
			}	
			
			System.out.println("-------- FIELDS --------");
			System.out.println("(S = Static, F = Final, SF = Static and Final)");
			System.out.println();
			
			for(int k = 0; k < sfFields.size(); k++) {   
			    System.out.println(sfFields.get(k));
			}
			
		} catch (ClassNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();

		}
		
		}

	}

