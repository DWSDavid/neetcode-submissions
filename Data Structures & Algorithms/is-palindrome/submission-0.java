class Solution {
    public boolean isPalindrome(String s) {
        char[] array = s.toUpperCase().toCharArray();
        ArrayList<Character> list = new ArrayList<>();
        for(int i = 0; i < array.length;i++){
            if(Character.isLetterOrDigit(array[i])){
                list.add(array[i]);
            }
        }
        for(int j = 0; j < list.size()/2;j++){
            if(list.get(j) != list.get(list.size()-1-j)){
                return false;
            }
        }
        return true;
    }
}
