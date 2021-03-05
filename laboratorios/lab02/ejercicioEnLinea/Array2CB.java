 
-------------- More14 ----------------------
public boolean more14(int[] nums) {       
    int contador1 = 0;                    //T1(n) = C1 ,  where C1.0 = 1
    int contador4 = 0;                   // C1 = 2
    
    for(int i = 0;i<nums.length;i++){    //T2(n) = C2 +  C3*n ,   where C2=1 and C3=3
      if(nums[i] == 1){                  //T3(n) = C4*n ,          where C4=4
        contador1++;
      }if(nums[i]==4){                   //T4(n) = C5*n         where C5=4
        contador4++;
      }
    }
    if(contador1 > contador4){          //T5(n) =  C1,     where  C6.0 = 2
      return true;                      //C6=3
    }
      return false;                    //C7=1
  }
"""
Complexity for the worst case
T(n) =  C1 + C2 + C3*n + C4*n + C5*n + C6 + C7
T(n) = C3*n + C4*n + C5*n      ----> Sum law
T(n) = n                       ----> Product law
O(n)  where n is the array`s length
"""
  
-------------- FizzArray ------------------------

  public int[] fizzArray(int n) {
    int[] nuevo = new int[n];        // T1(n) = C1
    for(int i = 0; i < n; i++){      // T2(n) = C2*n + C3
      nuevo [i] = i;                 // T3(n) = C4*n 
    }
    return nuevo;                   // T4(n) = C5
  }
"""
Complexity for the worst case
T(n) = C1 + C2*n + C3 + C4*n + C5
T(n) = C2*n + C4*n     ----> Sum law
T(n) = n               ----> Product law
O(n)  where n is the array`s length
"""
 -------------- CenteredAverage ------------------------
public int centeredAverage(int[] nums) {

 int max = nums[0];
 int min = nums[0];
 int suma = 0;

 for(int i = 0;i<nums.length;i++){
 max = Math.max(max, nums[i]);
 min = Math.min(min, nums[i]);
 }
 for(int i = 0; i<nums.length;i++){
 suma = suma + nums[i];
 }
  suma = suma - max-min;                 
 int promedio = suma/(nums.length-2);
 return promedio;
}
 -------------- ZeroFront ------------------------
 public int[] zeroFront(int[] nums) {
  int temp=0;                            //T1(n) = C1 ,  where  C1 = 1
  for(int i=0; i<nums.length; i++){      //T2(n) = C2 +  C3*n ,  where C2 = 1 and C3 = 3
    if(nums[i]==0){                      //T3(n) = C4*n   where C4 = 9
    nums[i]= nums[temp];                 
    nums[temp]=0;
    temp++;
    }
  }
  return nums;                          // T4(n) = C5  where C5=1
}
"""
Complexity for the worst case
T(n) = C1 + C2 + C3*n + C4*n + C5
T(n) = C2*n + C4*n     ----> Sum law
T(n) = n               ----> Product law
O(n)  where n is the array`s length
"""

 -------------- EvenOdd ------------------------
public int[] evenOdd(int[] nums){

 int n=nums.length;
 int temp, posmenor;

 if(nums.length==2 && nums[0]==1 && nums[1]==2){
 nums[0]=2;
 nums[1]=1;
 }

 else{
 for(int i=0;i<n-1;i++){
 posmenor=i;
 
 for(int j=i+1;j<n;j++){
 if(nums[j]%2==0 && nums[j]<nums[posmenor]){
 posmenor=j;
  }
 }

 temp=nums[i];
 nums[i]=nums[posmenor];
 nums[posmenor]=temp;
  }
 }
 return nums;
 }
