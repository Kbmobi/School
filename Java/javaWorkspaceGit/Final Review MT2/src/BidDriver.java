import java.util.Collections;
import java.util.Iterator;


public class BidDriver {

	public static void main(String[] args) {
		AuctionItemInterface diamonds = new AuctionItem("Diamonds", 5);
		
		diamonds.makeBid(new Bid("Fred", 10));
		diamonds.makeBid(new Bid("Chico", 15));
		diamonds.makeBid(new Bid("Barney", 20));
		
		Iterator<Bid> iter = diamonds.byName();
		
		while(iter.hasNext()) {
			Bid aBid = iter.next();
			System.out.println(aBid.getName() + " " + aBid.getAmount());
		}
		
		for(Bid aBid : diamonds) {
			System.out.println(aBid.getName() + " " + aBid.getAmount());
		}	
		
		System.out.println(diamonds.getHighestBid());
	}

}
