
public class Bottle {
	private String contents;
	private int maxCapacity;
	private int minCapacity;
	private int currentCapacity;
	
	public Bottle(int atMaxCapacity, int atMinCapacity, int atCurrentCapacity) {
		maxCapacity = atMaxCapacity;
		contents = "Water";
		minCapacity = atMinCapacity;
		currentCapacity = atCurrentCapacity;		
	}
	
	public String getBottleName() {
		return contents;
	}	
	
	public int getMaxCapacity() {
		return maxCapacity;
	}
	
	public int getMinCapacity() {
		return minCapacity;
	}
	
	public int getCurrentCapacity() {
		return currentCapacity;
	}	
	
	public void fill() {
		if(currentCapacity < maxCapacity) {
			currentCapacity++;
		}
	}
	
	public void dump() {
		if(currentCapacity > minCapacity) {
			currentCapacity--;
		}		
	}
	
	@Override
	public String toString() {
		String result = "";
		
		result += "Bottle Contains: " + contents + " \n";
		result += "Maximum Capacity: " + maxCapacity + "mL \n";
		result += "Current Capacity: " + currentCapacity + "mL \n";
		
		return result;
	}	
		
}

