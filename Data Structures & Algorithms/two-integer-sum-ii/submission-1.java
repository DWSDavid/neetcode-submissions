class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int left = 0, right = numbers.length-1;
        while(left < right){
            int sum = numbers[left] + numbers[right];
            if(sum == target){
                int[] result = {left+1,right+1}; //1-indexed
                return result;
            }
            else if(sum < target){
                left++;
            }
            else{
                right--;
            }
        }
        return new int[]{};
    }
}
