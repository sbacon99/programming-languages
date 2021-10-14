// Sam Bacon
// February 23, 2021
// Classwork: Functional Programming

import java.util.Arrays;
import java.util.Collection;
import java.util.List;
import java.util.stream.Collectors;

public class Main {

	public static void main(String[] args) {
		// Create and test a solution to solve the following problems using
		// functional programming:
		Collection<String> strs = Arrays.asList("elon", "mascot", "phoenix", "clemson", "has", "tiger");
		Collection<Integer> ints = Arrays.asList(1,2,3,4,5,6,7,8);
		
		
		// Problem 1: Given a collection of Strings, create and print a list of strings, but omitting
		// any that contain an "a") given the inputs below, the result should be 
		// a list with ["elon", "phoenix", "clemson", "tiger"]
		
		List<String> names = strs.stream()			// stream through ArrayList
				.filter(x -> !x.contains("a"))		// filter strings that do not have 'a'
				.collect(Collectors.toList());		// collect responses
		
		System.out.println("Problem 1");
		System.out.println(names);					// print answer
		System.out.println();
		
		
		// Problem 2: Given a collection of Strings, create and print a List of Strings, first
		// appending an "i" to the end, then removing any that contain the substring "ni"
		
		List<String> names2 = strs.stream()			// stream through ArrayList
				.map(x -> x + "i")					// append 'i' to end
				.filter(x -> !x.contains("ni"))		// remove any that contain 'ni'
				.collect(Collectors.toList());		// collect remaining
		
		System.out.println("Problem 2");
		System.out.println(names2);					// print answer
		System.out.println();	
		
				
		// Problem 3: Given a collection of Integers, create and print a list with all "teens"
		// omitted (teens are any numbers between 13 and 19)
		
		List<Integer> ages = ints.stream()			// stream through ArrayList
				.filter(x -> x < 13 || x > 19)		// remove teenagers
				.collect(Collectors.toList());		// collect remaining
		
		System.out.println("Problem 3");			
		System.out.println(ages);					// print answer
		System.out.println();
			

		// Problem 4: Given a collection of Integers, omitting any with two or more digits,
		// sum the squares of all numbers and add the product to 42. (In the ints list given,
		// the correct answer should be 42+25+49+4+16 = 136
		
		Integer sum = ints.stream()									// stream through ArrayList
				.filter(x -> Integer.toString(x).length() < 2)		// remove ints with length >= 2
				.map(x -> x*x)										// square remaining
				.reduce(0, (x,y) -> x+y) + 42;						// add squares together, +42 at the end
		
		System.out.println("Problem 4");
		System.out.println(sum);									// print answer
		System.out.println();
		
		
		// Problem 5: Given a collection of Strings, create and print a List of Strings
		// by first removing any with lengths between 4 and 6 (inclusive), then by adding
		// a "z" after the first letter of each remaining word. 
		
		List<String> name3 = strs.stream()							// stream through ArrayList
				.filter(x -> x.length() < 4 || x.length() > 6 )		// remove strings with length between 4 and 6 inclusive
				.map(x -> x.charAt(0) + "z" + x.substring(1))		// add 'z' after first character in remaining strings
				.collect(Collectors.toList());						// collect remaining
		
		System.out.println("Problem 5");
		System.out.println(name3);									// print answer
		System.out.println();
		
		
		// Problem 6: Given a collection of Integers, return a list of the numbers
		// multiplied by 3, omitting any that end in 1
			
		List<Integer> nums = ints.stream()					// stream through ArrayList
				.map(x -> x*3)								// multiply ints * 3
				.filter(x -> x % 10 != 1)					// remove values ending in 1
				.collect(Collectors.toList());				// collect remaining
		
		System.out.println("Problem 6");
		System.out.println(nums);							// print answer
		System.out.println();
		
		
		// Problem 7: Given a collection of Integers, excluding any numbers
		// ending in 7, return the result of 
		// adding together each of the remaining numbers plus an extra 2 every
		// time values are added.
		// EX: From the list above, after numbers ending in 7's are removed,
		// the remaining values would be [5, 2, 4, 15, 90]. The math would result in:
		// (0  + 5 + 2) // Starting at 0, add the first element (5) and 2 extra
		// (7  + 2 + 2)  // Given the 7 from the last step, add 2 plus 2 extra
		// (11 + 4 + 2) // GIven 11 from the prior sum, add 4 plus 2 extra
		// (17 + 15 + 2)// Given 17 from the prior sum, add 15 plus 2 extra
		// (34 + 90 + 2)// Finally, add 90 plus 2 to the running sum to get the result of 126
		// HINT: This is relatively easy to do - requiring only 2 methods after .stream()
		
		Integer sum2 = ints.stream()						// stream through ArrayList
				.filter(x -> x % 2 == 1)					// remove values ending in 7
				.map(x -> x*2)
				.reduce(7, (x,y) -> x+y+3);					// sum remaining, +2 each time
		
		System.out.println("Problem 7");
		System.out.println(sum2);							// print answer
		System.out.println();
		
		
	}

}
