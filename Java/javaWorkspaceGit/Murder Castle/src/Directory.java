import java.io.Serializable;
import java.util.Comparator;


public class Directory implements Comparable<Directory>, Serializable {
	private String firstName;
	private String lastName;
	private int money;
	private int daysStayed;

	public Directory(String inFirstName, String inLastName, int inMoney) {
		firstName = inFirstName;
		lastName = inLastName;
		money = inMoney;
		daysStayed = 0;
	}

	public Directory() {
	}
	
	public String getFirstName() {
		return firstName;
	}

	public String getLastName() {
		return lastName;
	}

	public int getDaysStayed() {
		return daysStayed;
	}

	public int getMoney() {
		return money;
	}
	
	public void setFirstName(String inFirstName) {
		firstName = inFirstName;
	}

	public void setLastName(String inLastName) {
		lastName = inLastName;
	}

	public void setMoneyInPocket(int inMoney) {
		money = inMoney;
	}


	public void nightlyBilling(int i) {
		int gold = getMoney();
		daysStayed += i;
		gold -= i;
		setMoneyInPocket(gold);
	}

	public boolean getStatus(){
		int gold = getMoney();
		
		if(gold <= 0) {
			return true;
		}
		
		return false;
	}

	@Override
	public int compareTo(Directory other) {
		int myTotalMoney = getMoney();
		int otherTotalMoney = other.getMoney();

		int difference = myTotalMoney - otherTotalMoney;
		if (difference != 0) {
			return difference;
		}

		difference = daysStayed - other.daysStayed;
		if (difference != 0) {
			return difference;
		}

		difference = lastName.compareTo(other.lastName);

		return difference;
	}

	@Override
	public boolean equals(Object what) {
		Directory other = (Directory) what;

		if (!lastName.equals(other.lastName)) {
			return false;
		}

		if (!firstName.equals(other.firstName)) {
			return false;
		}

		return true;
	}

	@Override
	public String toString() {
		String result = "";

		result += "firstName " + firstName;
		result += " lastName " + lastName;
		result += " money " + money;
		result += " daysStayed " + daysStayed;
		
		return result;
	}
	
	public static Comparator<Directory> byLastName() {
		return new Comparator<Directory> () {
			public int compare(Directory aa, Directory bb) {
				Directory a = (Directory) aa;
				Directory b = (Directory) bb;

				int difference = a.lastName.compareTo(b.lastName);
				
				if(difference != 0) {
					return difference;
				}
				
				difference = a.firstName.compareTo(b.firstName);
				
				return difference;
			}
		};
	}
}
