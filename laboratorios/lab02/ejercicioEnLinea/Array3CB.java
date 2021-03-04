public int[] fix34(int[] nums) {
    int temp = 0;
    for(int i = 0; i < nums.length; i++){
        for(int j = 0; j < nums.length; j++){
          if(nums[j] == 3 && nums[i] == 4 ){
            temp = nums[j+1];
            nums[j+1] = nums[i];
            nums[i] = temp;
          } 
        }
     }
     return nums;
    
  }