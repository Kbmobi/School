
public class Thrower implements ThrowerInterface {
	private int balls;

	public Thrower(int inThrows) {
		balls = inThrows;
	}

	@Override
	public boolean hasNext() {
		if(balls == 0) {
			return false;
		}
		
		return true;
	}

	@Override
	public int next() {
		int ballCount = balls;
		balls -- ;
		return ballCount;
	}
	
	

}
