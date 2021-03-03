public boolean more14(int[] nums) {
    int contador1 = 0;
    int contador4 = 0;
    
    for(int i = 0;i<nums.length;i++){
      if(nums[i] == 1){
        contador1++;
      }if(nums[i]==4){
        contador4++;
      }
    }
    if(contador1 > contador4){
      return true;
    }
      return false;
  }
  
  #%%

  public int[] fizzArray(int n) {
    int[] nuevo = new int[n];
    for(int i = 0;i<n;i++){
      nuevo [i] = i;
    }
    return nuevo;
  }
  