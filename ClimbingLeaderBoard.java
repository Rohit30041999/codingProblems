/*
Problem Statement:>> () -> (link to the problem description)
*/

/*
Solution:>>>

Method - I:>> (Binary Search Method)
*/

public class ClimbingLeaderBoard {

    static int searchPlace(ArrayList<Integer> S, int lowIndex, int highIndex, int key) {
        if(lowIndex >= highIndex) {
            return (S.get(lowIndex) > key) ? lowIndex+1: lowIndex;
        }
        int midIndex = (lowIndex+highIndex)/2;
        if(S.get(midIndex) == key) 
            return midIndex;
        if(S.get(midIndex) > key) 
            return searchPlace(S, midIndex+1, highIndex, key);
        if(S.get(midIndex) < key) 
            return searchPlace(S, lowIndex, midIndex, key);
        return -1;
    }
    
    static int[] climbingLeaderboard(int[] scores, int[] alice) {
        ArrayList<Integer> ranks = new ArrayList<Integer>();
        
        ArrayList<Integer> uniqueScores = new ArrayList<Integer>();
        LinkedHashSet<Integer> uniqueScore = new LinkedHashSet<Integer>();

        for(int i=0; i<scores.length; ++i) {
            uniqueScore.add(scores[i]);
        }

        uniqueScores.addAll(uniqueScore);

        for(int i=0; i<alice.length; ++i) {
             ranks.add(searchPlace(uniqueScores, 0, uniqueScores.size()-1, alice[i]));
        }

        int[] leaderBoardPlaces = new int[ranks.size()];
        for(int i=0; i<leaderBoardPlaces.length; ++i) {
            leaderBoardPlaces[i] = ranks.get(i)+1;
        }
        return leaderBoardPlaces;
    }
	
    public static void main(String[] args) throws IOException {
        //input code comes here.
}
