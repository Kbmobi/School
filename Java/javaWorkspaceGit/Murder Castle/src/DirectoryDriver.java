import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Iterator;
import java.util.List;
import java.util.Scanner;

public class DirectoryDriver {



	public static void main(String[] args) {
		List<Directory> allClients = new ArrayList<>();

		allClients.add(new Directory("Fred", "Flintstone", 20));
		allClients.add(new Directory("Wilma", "Flintstone", 15));	
		allClients.add(new Directory("Pebbles", "Flintstone", 20));
		allClients.add(new Directory("Dino", "Flintstone", 0));
		allClients.add(new Directory("Baby", "Puss", 5)); 
		allClients.add(new Directory("Barney", "Rubble", 15)); 
		allClients.add(new Directory("Betty", "Rubble", 15)); 
		allClients.add(new Directory("Bamm-Bamm", "Rubble", 15)); 
		allClients.add(new Directory("Hoppy", "Rubble", 8)); 
		allClients.add(new Directory("Mr","Slate", 8)); 
		allClients.add(new Directory("Joe", "Rockhead", 8));
		allClients.add(new Directory("Pearl", "Slaghoople", 8));
		allClients.add(new Directory("Great", "Gazoo", 8));
		allClients.add(new Directory("Tex", "Hardock", 3));
		allClients.add(new Directory("Sam", "SlagHeap", 3));
	

		String fileName = "directory.txt";

		Path file = Paths.get(fileName);

		writeAllClientsToFile(file, allClients);
		
		List<Directory> copyOfClients = readAllClientsFromFile(file);
		
		 System.out.println(".----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.    "); 
		 System.out.println("| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |  ");  
		 System.out.println("| | ____    ____ | || | _____  _____ | || |  _______     | || |  ________    | || |  _________   | || |  _______     | |  ");
		 System.out.println("| ||_   \\  /   _|| || ||_   _||_   _|| || | |_   __ \\    | || | |_   ___ `.  | || | |_   ___  |  | || | |_   __ \\    | |  ");
		 System.out.println("| |  |   \\/   |  | || |  | |    | |  | || |   | |__) |   | || |   | |   `. \\ | || |   | |_  \\_|  | || |   | |__) |   | |  ");
		 System.out.println("| |  | |\\  /| |  | || |  | '    ' |  | || |   |  __ /    | || |   | |    | | | || |   |  _|  _   | || |   |  __ /    | |  ");
		 System.out.println("| | _| |_\\/_| |_ | || |   \\ `--' /   | || |  _| |  \\ \\_  | || |  _| |___.' / | || |  _| |___/ |  | || |  _| |  \\ \\_  | |  ");
		 System.out.println("| ||_____||_____|| || |    `.__.'    | || | |____| |___| | || | |________.'  | || | |_________|  | || | |____| |___| | |  ");
		 System.out.println("| |              | || |              | || |              | || |              | || |              | || |              | |  ");
		 System.out.println("| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |  ");
		 System.out.println("'----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'    ");
		 System.out.println(".----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.    ");
		 System.out.println("| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |  ");
		 System.out.println("| |     ______   | || |      __      | || |    _______   | || |  _________   | || |   _____      | || |  _________   | |  ");
		 System.out.println("| |   .' ___  |  | || |     /  \\     | || |   /  ___  |  | || | |  _   _  |  | || |  |_   _|     | || | |_   ___  |  | |  ");
		 System.out.println("| |  / .'   \\_|  | || |    / /\\ \\    | || |  |  (__ \\_|  | || | |_/ | | \\_|  | || |    | |       | || |   | |_  \\_|  | |  ");
		 System.out.println("| |  | |         | || |   / ____ \\   | || |   '.___`-.   | || |     | |      | || |    | |   _   | || |   |  _|  _   | |  ");
		 System.out.println("| |  \\ `.___.'\\  | || | _/ /    \\ \\_ | || |  |`\\____) |  | || |    _| |_     | || |   _| |__/ |  | || |  _| |___/ |  | |  ");
		 System.out.println("| |   `._____.'  | || ||____|  |____|| || |  |_______.'  | || |   |_____|    | || |  |________|  | || | |_________|  | |  ");
		 System.out.println("| |              | || |              | || |              | || |              | || |              | || |              | |  ");
		 System.out.println("| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |  ");
		 System.out.println(" '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'   ");
		
		System.out.println("\nH.H.Holmes New clients this week: \n---------------------------------------\n");
		Collections.sort(copyOfClients, Directory.byLastName());
		Iterator<Directory> iter = copyOfClients.iterator();
		while(iter.hasNext()){ 	 
			Directory next = iter.next();
			System.out.println(next.getFirstName() + " " + next.getLastName()); 
		}

		List<Directory> firstWeekOfBilling = readAllClientsFromFile(file);		
		
		System.out.println("\nFirst Week Of Billing Victi...Clients:\n---------------------------------------\n");
		for (int i = 0; i < firstWeekOfBilling.size(); i++) {
			Directory client = firstWeekOfBilling.get(i);
			client.nightlyBilling(7);
			System.out.println(client.toString()); 
		}

		List<Directory> eviction = new ArrayList<>();
		
		for (Directory who : firstWeekOfBilling) {
			if(who.getStatus() == true) {
				eviction.add(who);
			}
		}
		
		System.out.println("\nPeople to be Sold to Medical R&D:\n---------------------------------------\n");
		Iterator<Directory> iterator = eviction.iterator();
		while(iterator.hasNext()){ 	 
			Directory next = iterator.next();
			System.out.println(next.getFirstName() + " " + next.getLastName()); 
		}

		for(Directory who : eviction){		
			if(firstWeekOfBilling.contains(who)){
				firstWeekOfBilling.remove(who);
			}
		}
		
		System.out.println("\nNeed another still:\n---------------------------------------\n");
		Directory victim = Collections.min(firstWeekOfBilling);
		if(firstWeekOfBilling.contains(victim)){
			System.out.println(victim.getFirstName() + " " + victim.getLastName() + " was killed for only haveing $" + victim.getMoney() + " left");
			eviction.add(victim);
			firstWeekOfBilling.remove(victim);
		}
		
		System.out.println("\nNeed some quick cash:\n---------------------------------------\n");
		Directory robbed = Collections.max(firstWeekOfBilling);
		if(firstWeekOfBilling.contains(robbed)){
			System.out.println(robbed.getFirstName() + " " + robbed.getLastName() + " was killed and robbed for $" + robbed.getMoney());
			eviction.add(robbed);
			firstWeekOfBilling.remove(robbed);
		}
		
		System.out.println("\nNeed to kill Wilma before she gets suspisious:\n---------------------------------------\n");
		Directory childSlave = new Directory("Wilma", "Flintstone", 8);
		int foundPosition = firstWeekOfBilling.indexOf(childSlave);
		Directory foundPlayer = firstWeekOfBilling.get(foundPosition);
		System.out.println(foundPlayer.getFirstName() + " " + foundPlayer.getLastName() + " was killed and robbed for $" + foundPlayer.getMoney());
		firstWeekOfBilling.remove(foundPlayer);
		
		System.out.println("\nWho do we still have left at the end of the first week:\n---------------------------------------\n");
		Collections.sort(firstWeekOfBilling);
		for (int i = 0; i < firstWeekOfBilling.size(); i++) {
			Directory client = firstWeekOfBilling.get(i);
			System.out.println(client.toString()); 
		}		
		
		
	}

	private static void writeAllClientsToFile(Path file, List<Directory> allClients) {
		Charset charset = Charset.forName("US-ASCII");

		try (BufferedWriter writer = Files.newBufferedWriter(file, charset)) {

			for (Directory who : allClients) {
				writeOneClient(who, writer);
			}
		} catch (IOException e) {
			e.printStackTrace();
		}

	}

	private static void writeOneClient(Directory who, BufferedWriter writer)
			throws IOException {
		String first = who.getFirstName();
		String last = who.getLastName();
		String money = who.getMoney() + "";
		String days = who.getDaysStayed() + "";

		String result = first + " " + last + " " + money + " " + days;

		writer.write(result);
		writer.newLine();
	}

	private static List<Directory> readAllClientsFromFile(Path file) {
		List<Directory> bunchOClients = new ArrayList<>();

		Charset charset = Charset.forName("US-ASCII");

		try (BufferedReader reader = Files.newBufferedReader(file, charset)) {

			String aLine = "";
			while ((aLine = reader.readLine()) != null) {
				Scanner scan = new Scanner(aLine);

				String firstName = scan.next();
				String lastName = scan.next();
				int money = scan.nextInt();

				Directory aClient = new Directory(firstName, lastName, money);
				bunchOClients.add(aClient);
			}
		} catch (IOException e) {
			e.printStackTrace();
		}

		return bunchOClients;
	}

}
