import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class LoserDriver {

	public static void main(String[] args) {
		Loser fred = new Loser("Fred", 150);
		Loser jones = new Loser("Jones", 175);
		Loser evilMonkey = new Loser("EvilMonkey", 102);
		Loser rockMonster = new Loser("TheRockMonster", 6000);

		List<Loser> losers = new ArrayList<Loser>();

		losers.add(fred);
		losers.add(jones);
		losers.add(evilMonkey);
		losers.add(rockMonster);

		fred = null;
		jones = null;
		evilMonkey = null;
		rockMonster = null;

		for (Loser who : losers) {
			who.lowerWeight();
			who.lowerWeight();
		}

		for (Loser who : losers) {
			System.out.println(who.getName());
		}

		Loser fetchBitch = new Loser("Fred", 0);
		int foundPosition = losers.indexOf(fetchBitch);
		Loser foundPlayer = losers.get(foundPosition);
		// System.out.println(foundPlayer.toString());
		foundPlayer.setCurrentWeight(123);
		// System.out.println(foundPlayer.toString());
		foundPlayer = null;

		fetchBitch = new Loser("Jones", 0);
		foundPosition = losers.indexOf(fetchBitch);
		foundPlayer = losers.get(foundPosition);
		// System.out.println(foundPlayer.toString());
		foundPlayer.setCurrentWeight(170);
		// System.out.println(foundPlayer.toString());
		foundPlayer = null;

		System.out.println("Biggest Loser is: " + Collections.max(losers));

		Collections.sort(losers);

		for (Loser who : losers) {
			System.out.println(who.getName());
		}

		Loser smallestLoser = losers.get(0);
		for (int i = 1; i < losers.size(); i++) {
			Loser person = losers.get(i);

			if (smallestLoser.getWeightDifference() > person.getWeightDifference()) 
				smallestLoser = person;			
		}
		
		losers.remove(smallestLoser);
		System.out.println("SmallestLoser Name: " +smallestLoser.getName() + 
				" Start Weight: " + smallestLoser.getStartWeight() + 
				" Current Weight: " + smallestLoser.getCurrentWeight() + 
				" Weight Difference: " + smallestLoser.getWeightDifference());

		for (Loser who : losers) {
			System.out.println(who.getName());
		}		
		
	}
}
