---------------------------------------maxSpan---------------------------
public int maxSpan(int[] nums) {                     
 if(nums.length == 0){                           // C1.0 = 3
   return 0;                                     // C1 = 4
 }
 else if(nums[0] == nums[nums.length-1]){       //C2.0 = 6
   return nums.length;                          // C2 = 8
 }
 else{                                          // C3 = 3             
   return nums.length-1;
 }
}
/* Complexity worst case
T(n) = C1 + C2 + C3
T(n) = C
O(1) 
The complexity for the worst case is a constant
*/
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
  int sum1= 0;                           // T1(n) = C1    where C1 = 1
  int sum2 = 0;                          // T2(n) = C2    where C2 = 1
  
  for(int i=0; i<nums.length-1; i++)         // T3(n) = C4 + C3*(n-1)  where C4 = 1 , C3 = 3
    sum1 = sum1+nums[i];                     // T4(n) = C5*n   where C5 = 3
    sum2 = nums[nums.length-1];              // T5(n) = C6*n   where C6 = 4
    
    for(int i=nums.length-2; i>0; i--){      // T6(n) = C7 + C8*(n-2)   where C7 = 1 , C8 = 3
      if(sum1==sum2){                        // T7(n) = C9*n   where C9 = 3    ** no se si si es asiiiii????***
       return true;
      } else{
      sum1 = sum1-nums[i];                   // T8(n) = C10*n  where C10 = 3
      sum2 = sum2+nums[i];                   // T9(n) = C11*n  where C11 = 3
    }
  }
  return (sum1==sum2);                      // T10(n) = C12*n  where C12 = 2
}
/* Complexity worst case
T(n) = C1 + C2 + C4 + C3*(n-1) + 
Where n is the array`s length
*/

---------------------------------------linearIn---------------------------
public boolean linearIn(int[] outer, int[] inner) {
  int cont=0;                                    // T1(n) = C1    where C1 = 1
 
  for(int i=0; i<inner.length; i++){               // T2(n) = C2 + C3*n   where C2 = 1 , C3 = 3
    for(int j=0; j<outer.length; j++){            // T3(n) = (C4 + C5*n)*m   where C4 = 1 , C5 = 3
      if(inner[i] == outer[j]){                  // T4(n) = C6*n*m   where C6 = 4 
        cont++;                                 // T5(n) = C7*n*m   where C7 = 1
        break;                                 // T6(n) = C8*n*m   where C8 = 1
      }
  }
}
 if(cont == inner.length){                // T7(n) = C9 where C9.0 = 3
   return true;                           // C9 = 4
 }
  return false;                          // T8(n) = C10 where C10 = 1
}

/* Complexity worst case
T(n, m) = C1 + C2 + C3*n + (C4 + C5*n)*m  + C6*n*m + C7*n*m + C8*n*m + C9 + C10
T(n, m) = C3*n + C5*n*m  + C6*n*m + C7*n*m + C8*n*m           ----> Common factor and sum law
T(n, m) = n + n*m                                             ----> Product law
T(n, m) = n*m                                                 ----> Sum law
O(n*m) 
Where n is the inner`s length and m is the outer`s length
*/
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
