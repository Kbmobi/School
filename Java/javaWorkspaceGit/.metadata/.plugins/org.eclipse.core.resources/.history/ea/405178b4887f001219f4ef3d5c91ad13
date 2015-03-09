import java.util.Comparator;


public class Instructor implements InstructorInterface {
	private String nickName;
	private int moneyRaised;
	private int dunks;
	
	public Instructor(String inName) {
		nickName = inName;
		moneyRaised = 0;
		dunks = 0;
	}

	@Override
	public int compareTo(InstructorInterface other) {
		int difference = moneyRaised - other.getMoneyRaised();
		if (difference != 0) {
			return difference;
		}

		difference = nickName.compareTo(other.getNickName());

		if (difference != 0) {
			return difference;
		}

		return difference;
	}
	
	@Override
	public boolean equals(Object what) {
		Instructor other = (Instructor) what;

		if (!nickName.equals(other.nickName)) {
			return false;
		}

		return true;
	}

	@Override
	public void addToMoneyRaised(int amount) {
		moneyRaised += amount;
		
	}

	@Override
	public void wasDunked() {
		dunks++;
		
	}

	@Override
	public String getNickName() {
		return nickName;
	}

	@Override
	public int getMoneyRaised() {
		return moneyRaised;
	}

	@Override
	public int getDunks() {
		return dunks;
	}

	public static Comparator<InstructorInterface> iterator() {
		return new Comparator<InstructorInterface>() {
			public int compare(InstructorInterface a, InstructorInterface b) {
				int aVictim = a.getMoneyRaised();
				int bVictim = b.getMoneyRaised();

				if (aVictim > bVictim ) {
					return aVictim;
				}

				return bVictim;
			}
		};
	}
	
}
