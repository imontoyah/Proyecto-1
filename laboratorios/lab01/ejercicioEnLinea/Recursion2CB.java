public boolean groupSum6(int start, int[] nums, int target) {
    if(start >= nums.length){   //C1 = 5 = T(0)
      if(target==0){
        return true;
      }
    }
    else if(nums[start]==6){                      // T(n)= c2 + T(n-1)   C2 = 6
      return groupSum6(start+1, nums, target-6);  // T(n) = C*n +C1
    }
    else{
      return groupSum6(start+1, nums, target) || groupSum6(start+1, nums, target-nums[start]);   // T(n) = C2 + T(n-1) + T(n-1)   C3= C2
    }                                                                                            // T(n)= C(2^n-1) + C1* 2^n-1
    return false;   //C4=1
  }

#%%
public boolean groupNoAdj(int start, int[] nums, int target) {
    if(start >= nums.length){  // C1 = 6 ?
      if(target==0){
        return true;
      }
    }
    
    else{
    return groupNoAdj(start+1, nums, target) || groupNoAdj(start+2, nums, target-nums[start]);  // T(n) = T(n-1) + T(n-2) + C2     C2=2
  }                                                                                             // T(n) = -C + C1*F_n + C2*L_n 
   return false;          // C3 = 1
  }

#%%
public boolean groupSum5(int start, int[] nums, int target) {
    if(start >= nums.length){  // C1 = 6
      if(target==0){
        return true;
      } else{
        return false;       //C2 = 2
      }
    }
    if(nums[start]==1 && start > 0 && nums[start-1]%5==0){  // T(n) = C3 + T(n-1)         C3 = 12
      return groupSum5(start+1, nums, target);
    }
    else if(nums[start]%5==0){                             // T(n) = C4 + T(n-1)         C4 = 7
      return groupSum5(start+1, nums, target-nums[start]); // T(n) = C*n + C1 
    }
    else{                                                                                            // T(n) = C5 + T(n-1) + T(n-1)    C5 = 6
      return groupSum5(start+1, nums, target) || groupSum5(start+1, nums, target-nums[start]);       // T(n)= C(2^n-1) + C1* 2^n-1
    }
  }

#%%
public boolean splitArray(int[] nums) {
    return splitArrayAux(0,nums,0,0);
}
private boolean splitArrayAux(int start,int[] nums,int targetA, int targetB) {
 if(start >= nums.length){ // C0.1 = 5 
     return targetA == targetB; //C1 = 7
 }else{                 
     int x = nums[start];     //C2 = 10
     return splitArrayAux(start+1 ,nums, targetA+ x, targetB) || splitArrayAux(start+1 ,nums, targetA,x+ targetB); // T(n) = T(n-1) + T(n-1) +C2
 }                                                                                                                 // T(n)= C2(2^n-1) +C1*2^(n-1)

    
#%%
public  boolean groupSumClump(int start, int[] nums, int target) {
     if(target == 0 && start == nums.length ) 
          return true;                           //C1 = 6 
      else if (target !=0 && start == nums.length) 
           return false;                           // C2 = 10
      else if(start == nums.length-1)                                              
            return groupSumClump(start +1 ,nums, target-nums[start]) || groupSumClump(start +1 ,nums, target); // C3 = 8      T(n) = T(n-1)+T(n-1) + C3
                                                                                                                //            T(n)=C3(2^n-1) +C1*2^(n-1)  
    
           
       else if(nums[start] == nums[start+1]  && -start+nums.length-1 >= 1)                                     
            return groupSumClump( start+2, nums,  target-2*nums[start])||groupSumClump( start+2, nums,target); //c4 = 16      T(n) = T(n-2) + T(n-2) + C4
                                                                                                               //             T(n)=2^(1/2)*(C2(-1)^(n)+ C1) - c4
             
      else 
         return groupSumClump(start +1 ,nums, target-nums[start]) || groupSumClump(start +1 ,nums, target);   // C5 = 6       T(n) = T(n-1)+T(n-1) + C_5 
                                                                                                             //               T(n)=C5(2^n-1) +C1*2^(n-1)
        
    }
