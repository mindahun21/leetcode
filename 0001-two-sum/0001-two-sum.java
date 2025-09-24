class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> numsWithIndex =  new HashMap<>();
        for (int i = 0; i<nums.length;i++){
            numsWithIndex.put(i,nums[i]);
        }
        List<Map.Entry<Integer,Integer>> lists = new ArrayList<>(numsWithIndex.entrySet());
        lists.sort(Map.Entry.comparingByValue());
        int s = 0;
        int e = nums.length-1;
        while(s<e){
            if (lists.get(s).getValue() + lists.get(e).getValue() == target){
                return new int[] {lists.get(s).getKey(),lists.get(e).getKey()};
            }
            if(lists.get(s).getValue() + lists.get(e).getValue() > target){
                e-=1;
            }
            else{
                s+=1;
            }
        }
        return new int[] {};
    }
}