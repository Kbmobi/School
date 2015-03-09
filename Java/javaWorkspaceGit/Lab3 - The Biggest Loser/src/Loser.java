public class Loser implements Comparable<Loser> {
	private String name;
	private int startWeight;
	private int currentWeight;

	public Loser(String playerName, int startingWeight) {
		name = playerName;
		startWeight = startingWeight;
		currentWeight = startingWeight;
	}

	public String getName() {
		return name;
	}

	public int getStartWeight() {
		return startWeight;
	}

	public int getCurrentWeight() {
		return currentWeight;
	}

	public int getWeightDifference() {
		int weightDifference = startWeight - currentWeight;
		return weightDifference;
	}

	public void setCurrentWeight(int newWeight) {
		if (newWeight <= 100) {
			return;
		}
		currentWeight = newWeight;
	}

	public void lowerWeight() {
		currentWeight--;
	}

	@Override
	public boolean equals(Object what) {
		Loser other = (Loser) what;
		if (!name.equals(other.name)) {
			return false;
		}

		return true;
	}

	@Override
	public String toString() {
		String result = "";

		result += " name " + name;
		result += " startWeight " + startWeight;
		result += " currentWeight " + currentWeight;
		result += " weightDifference " + getWeightDifference();

		return result;
	}

	@Override
	public int compareTo(Loser other) {
		int difference = getWeightDifference() - other.getWeightDifference();
		if (difference != 0) {
			return difference;
		}
		
		difference = name.compareTo(other.name);
		return difference;
	}
}
