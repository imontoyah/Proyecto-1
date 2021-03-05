---------------------------------------Fix34---------------------------
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
---------------------------------------Fix45---------------------------
    public int[] fix45(int[] nums) {
  int temp = 0;
  
  for(int i=0; i<nums.length; i++){
    for(int j=0; j<nums.length; j++){
      if(nums[j] == 4 && nums[i] == 5){
        temp = nums[j+1];
        nums[j+1] = nums[i];
        nums[i] = temp;
    }
   }
 }
 return nums;
}
---------------------------------------canBalance---------------------------
public boolean canBalance(int[] nums) {
  int sum1= 0;
  int sum2 = 0;
  
  for(int i=0; i<nums.length-1; i++)
    sum1 = sum1+nums[i];
    sum2 = nums[nums.length-1];
    
    for(int i=nums.length-2; i>0; i--){
      if(sum1==sum2){
       return true;
      } else{
      sum1 = sum1-nums[i];
      sum2 = sum2+nums[i];
    }
  }
  return (sum1==sum2);
}

---------------------------------------linearIn---------------------------
public boolean linearIn(int[] outer, int[] inner) {
  int cont=0;
 
  for(int i=0; i<inner.length; i++){
    for(int j=0; j<outer.length; j++){
      if(inner[i] == outer[j]){
        cont++;
        break;
      }
  }
}
 if(cont == inner.length){
   return true;
 }
  return false;
}

---------------------------------------CountClump---------------------------
    public int countClumps(int[] nums) {
  int count = 0;
  boolean resultado = false;
  
  if(nums.length == 0){
    return count;
  }
  for(int i = 0; i < nums.length-1; i++){
    if(nums[i] == nums[i+1] && !resultado){
      resultado = true;
      count++;
    }
    else if(nums[i]!=nums[i+1]){
      resultado = false;
    }
  }
  return count;
}
