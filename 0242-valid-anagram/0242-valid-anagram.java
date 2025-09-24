class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()){
            return false;
        }
        Map<Character, Integer> counts = new HashMap<>();
        for (char c :s.toCharArray() ){
            counts.put(c, counts.getOrDefault(c,0)+1);
        }
        for (char c: t.toCharArray()){
            if(!counts.containsKey(c)){
                return false;
            }
            counts.put(c,counts.get(c)-1);
        }

        for (int count: counts.values()){
            if(count!=0){
                return false;
            }
        }
        return true;
    }
}