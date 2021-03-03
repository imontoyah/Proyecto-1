 
-------------- More14 ----------------------
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
  
-------------- FizzArray ------------------------

  public int[] fizzArray(int n) {
    int[] nuevo = new int[n];        // T(n) = C1
    for(int i = 0;i<n;i++){          // T(n) = C2 + n
      nuevo [i] = i;
    }
    return nuevo;                   // T(n) = C3
  }
"""
Complexity for the worst case
T(n) = C2 + n
T(n) = n      ----> Sum law
O(n)  where n is the array`s length
"""
  
