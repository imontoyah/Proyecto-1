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
    int temp = 0;                                  //C1 = 1
    for(int i = 0; i < nums.length; i++){          // T(n) = C2 + C3*n   where C2 = 1 , C3 = 3
        for(int j = 0; j < nums.length; j++){      //T(n) = (C4 + C5*n)*n    where C4 = 1 , C5 = 3
          if(nums[j] == 3 && nums[i] == 4 ){      
            temp = nums[j+1];                      //C6*n*n where C6 = 13
            nums[j+1] = nums[i];                   
            nums[i] = temp;
          } 
        }
     }
     return nums;                                  //C7=1
    
  }
/* Complexity worst case
T(n) = C1 + (C2 + C3*n) + [(C4+C5*n)*n] + C6*n*n +C7
T(n) = C3*n + C5*n*n + C6*n*n            ----> Common factor and sum law
T(n) = n + n*n                           ----> Product law
T(n) = n*n                               ----> Sum law
O(n^2) where n is the aray´s length 
*/
---------------------------------------Fix45---------------------------
    public int[] fix45(int[] nums) {
  int temp = 0;                                  //C1 = 1
  
  for(int i=0; i<nums.length; i++){              // T(n) = C2 + C3*n   where C2 = 1 , C3 = 3
    for(int j=0; j<nums.length; j++){            //T(n) = (C4 + C5*n)*n    where C4 = 1 , C5 = 3
      if(nums[j] == 4 && nums[i] == 5){
        temp = nums[j+1];
        nums[j+1] = nums[i];
        nums[i] = temp;                         //C6*n*n where C6 = 13
    }
   }
 }
 return nums;                                  //C7=1
}
/* Complexity worst case
T(n) = C1 + (C2 + C3*n) + [(C4+C5*n)*n] + C6*n*n +C7
T(n) = C3*n + C5*n*n + C6*n*n            ----> Common factor and sum law
T(n) = n + n*n                           ----> Product law
T(n) = n*n                               ----> Sum law
O(n^2) where n is the aray´s length 
*/
---------------------------------------canBalance---------------------------
public boolean canBalance(int[] nums) {
  int sum1= 0;                           // T1(n) = C1    where C1 = 1
  int sum2 = 0;                          // T2(n) = C2    where C2 = 1
  
  for(int i=0; i<nums.length-1; i++)         // T3(n) = C4 + C3*(n-1)  where C4 = 1 , C3 = 3
    sum1 = sum1+nums[i];                     // T4(n) = C5*n   where C5 = 3
    sum2 = nums[nums.length-1];              // T5(n) = C6*n   where C6 = 4
    
    for(int i=nums.length-2; i>0; i--){      // T6(n) = (C7 + C8*(n-3))*n   where C7 = 1 , C8 = 3
      if(sum1==sum2){                        // T7(n) = C9*n*n   where C9 = 3    
       return true;
      } else{
      sum1 = sum1-nums[i];                   // T8(n) = C10*n*n  where C10 = 3
      sum2 = sum2+nums[i];                   // T9(n) = C11*n*n  where C11 = 3
    }
  }
  return (sum1==sum2);                      // T10(n) = C12  where C12 = 2
}
/* Complexity worst case
T(n) = C1 + C2 + C4 + C3*(n-1) + C5*n + C6*n + (C7 + C8*(n-3))*n + C9*n*n + C10*n*n + C11*n*n + C12
T(n) = C3*(n-1) + (C5 + C6)*n + C8*(n-3)*n + (C9 + C10 + C11)*n                 ----> Sum law and common factor
T(n) = (n-1) + n + (n-3)*n + n*n                                                ----> Product law 
T(n) = n + n*n                                                                  ----> Sum law 
T(n) = n*n                                                                      ----> Product law
O(n^2)
Where n is the array`s length
*/

---------------------------------------linearIn---------------------------
public boolean linearIn(int[] outer, int[] inner) {
  int cont=0;                                    // T1(n) = C1    where C1 = 1
 
  for(int i=0; i<inner.length; i++){               // T2(n) = C2 + C3*n   where C2 = 1 , C3 = 3
    for(int j=0; j<outer.length; j++){             // T3(n) = (C4 + C5*n)*m   where C4 = 1 , C5 = 3
      if(inner[i] == outer[j]){                   // T4(n) = C6*n*m   where C6 = 4 
        cont++;                                   // T5(n) = C7*n*m   where C7 = 1
        break;                                   // T6(n) = C8*n*m   where C8 = 1
      }
  }
}
 if(cont == inner.length){                 // T7(n) = C9 where C9.0 = 3
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
  int count = 0;                                    //C1 = 2
  boolean resultado = false;
  
  if(nums.length == 0){                             //C2 = 4
    return count;
  }
  for(int i = 0; i < nums.length-1; i++){           // T(n) = C3 + C4*(n-1)   where C3 = 1 , C4 = 3 
    if(nums[i] == nums[i+1] && !resultado){         //C5*(n-1)  where C5 = 8
      resultado = true;
      count++;
    }
    else if(nums[i]!=nums[i+1]){                    //C6*(n-1) where C6 = 5
      resultado = false;
    }
  }
  return count;                                      //C7 = 1
}
/* Complexity worst case
T(n) = C1 + C2 + (C3 + C4)*(n-1) + C5*(n-1) + C6*(n-1) +C7
T(n) = C4*(n-1) + C5*(n-1) + C6*(n-1)       ----> Common factor and sum law
T(n) = n-1                                  ----> Product law
T(n) = n                                    ----> Sum law
O(n) where n is the aray´s length 
*/
