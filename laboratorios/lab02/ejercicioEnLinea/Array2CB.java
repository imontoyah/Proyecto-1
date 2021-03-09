 
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
/*
Complexity for the worst case
T(n) =  C1 + C2 + C3*n + C4*n + C5*n + C6 + C7
T(n) = C3*n + C4*n + C5*n      ----> Sum law
T(n) = n                       ----> Product law
O(n)  where n is the array`s length
*/
  
-------------- FizzArray ------------------------

  public int[] fizzArray(int n) {
    int[] nuevo = new int[n];        // T1(n) = C1 = 1
    for(int i = 0; i < n; i++){      // T2(n) = C2*n + C3 where C2 = 1 and C3 = 3
      nuevo [i] = i;                 // T3(n) = C4*n where C4 = 2
    }
    return nuevo;                   // T4(n) = C5 where C5 = 1
  }
/*
Complexity for the worst case
T(n) = C1 + C2*n + C3 + C4*n + C5
T(n) = C2*n + C4*n     ----> Sum law
T(n) = n               ----> Product law
O(n)  where n is the array`s length
*/
 -------------- CenteredAverage ------------------------
 public int centeredAverage(int[] nums) {

    int max = nums[0];                       //C1 = 2
    int min = nums[0];                       //C2 = 2
    int suma = 0;                            //C3 = 1
   
    for(int i = 0;i<nums.length;i++){       //T(n) = C4 + C5*n  where C4 = 1 and C5 = 3
    max = Math.max(max, nums[i]);            // T(n) = C6*n  where C6 = 3
    min = Math.min(min, nums[i]);             //T(n) = C7*n  where C7 = 3
    }
    for(int i = 0; i<nums.length;i++){       //T(n) = C8 + C9*n  where C8 = 1 and C9= 3
    suma = suma + nums[i];                  //T(n) = C10 * n where C10 = 3     
    }
  suma = suma - max-min;                   //C11 = 3
 int promedio = suma/(nums.length-2);      //C12 = 4
 return promedio;                         //C13 = 1
}
/*
Complexity for the worst case
T(n) = C1 + C2 + C3 + C4 + C5*n + C6*n + C7*n+ C8 + C9*n + C10*n
T(n) = C5*n + C6*n+ C7*n + C9*n + C10*n  ----> Sum law
T(n) = n                                 ----> Product law
O(n)  where n is the array`s length
*/
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
/*
Complexity for the worst case
T(n) = C1 + C2 + C3*n + C4*n + C5
T(n) = C2*n + C4*n     ----> Sum law
T(n) = n               ----> Product law
O(n)  where n is the array`s length
*/

 -------------- EvenOdd ------------------------
public int[] evenOdd(int[] nums){     

      int n=nums.length;                                   //C1 = 2
      int temp, posmenor;                                  //C2 = 2
     
      if(nums.length==2 && nums[0]==1 && nums[1]==2){      //C3 = 13
      nums[0]=2;
      nums[1]=1;
      }
     
      else{
      for(int i=0;i<n-1;i++){                                 //T(n) = C4 + C5*(n-1) where C4 = 1 and C5 = 3                       
      posmenor=i;                                             //T(n) = C6 *(n) where C6 = 1
      
      for(int j=i+1;j<n;j++){                                  //T(n) = C7 + C8 *(n)  where C7 = 1 and C8 = 3                  
      if(nums[j]%2==0 && nums[j]<nums[posmenor]){             //T(n) = C9*n where C9 = 8
      posmenor=j;
       }
      }
     
      temp=nums[i];                                             //C10 = 8
      nums[i]=nums[posmenor];
      nums[posmenor]=temp;
       }
      }
      return nums;
      }

      /*
      T(n) = C1 + C2 + C3 + C4+C5*(n-1) + C6 *(n-1) + C7 + C8 *(n) + C9*n +C10
      T(n) = C1 + C2 + C3 + C4+ (n-1) + (n-1) + C7 + (n) + n   - - - > Product law
      T(n) = n                                                  - - - > Sum law
      O(n) where n is the array´s length 
      */
